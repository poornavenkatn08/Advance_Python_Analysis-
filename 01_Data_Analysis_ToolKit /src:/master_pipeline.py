import os
import sys
from webscraper import FortuneCompanyScraper
from data_Cleaner import CustomerDataCleaner
from eda_analyzer import ComprehensiveEDA

def run_pipeline():
    print("🚀 STARTING DATA ANALYSIS TOOLKIT PIPELINE")
    print("=" * 60)

    # 1. SETUP DIRECTORIES
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, 'data')
    reports_dir = os.path.join(base_dir, 'reports')
    
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(reports_dir, exist_ok=True)

    # ==========================================
    # PHASE 1: WEB SCRAPING (Fortune 500 Use Case)
    # ==========================================
    print("\n[PHASE 1] Executing Web Scraper...")
    scraper = FortuneCompanyScraper()
    fortune_file = os.path.join(data_dir, 'fortune_500_data.csv')
    
    try:
        scraped_data = scraper.scrape_and_export(fortune_file)
        if scraped_data is not None:
            print(f"✅ Scraping Successful! Saved to {fortune_file}")
            scraper.display_summary()
        else:
            print("⚠️ Scraping returned no data (Check internet connection).")
    except Exception as e:
        print(f"⚠️ Scraping skipped due to error: {e}")

    # ==========================================
    # PHASE 2: DATA CLEANING (Layoffs Use Case)
    # ==========================================
    print("\n[PHASE 2] Executing Data Cleaning Pipeline...")
    cleaner = CustomerDataCleaner()
    
    raw_layoffs = os.path.join(data_dir, 'layoffs_Raw.csv')
    clean_layoffs = os.path.join(data_dir, 'layoffs_Cleaned.csv')

    if os.path.exists(raw_layoffs):
        # Run cleaning
        if cleaner.clean_all(raw_layoffs):
            cleaner.save_cleaned_data(clean_layoffs)
            print("✅ Cleaning Successful!")
            print(cleaner.generate_cleaning_report())
        else:
            print("❌ Cleaning Failed.")
    else:
        print(f"❌ Error: {raw_layoffs} not found. Please add the CSV file.")

    # ==========================================
    # PHASE 3: EXPLORATORY DATA ANALYSIS (EDA)
    # ==========================================
    print("\n[PHASE 3] Executing Automated EDA...")
    eda = ComprehensiveEDA()
    
    # We prioritize the CLEANED data from Phase 2, fallback to Raw if needed
    target_file = clean_layoffs if os.path.exists(clean_layoffs) else raw_layoffs

    if os.path.exists(target_file):
        print(f"📊 Analyzing data from: {os.path.basename(target_file)}")
        if eda.load_data(target_file):
            # Run Analysis
            eda.run_complete_eda()
            
            # Save Report
            report_path = os.path.join(reports_dir, 'final_analysis_report.txt')
            eda.generate_comprehensive_report(report_path)
            print(f"📄 Final Report generated at: {report_path}")
        else:
            print("❌ EDA Failed to load data.")
    else:
        print("⚠️ Skipping EDA: No data file found to analyze.")

    print("\n" + "=" * 60)
    print("🎉 PIPELINE EXECUTION COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    run_pipeline()
