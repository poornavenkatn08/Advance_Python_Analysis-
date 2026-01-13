# Data Analysis Toolkit 🔍

A modular Python framework designed for end-to-end data processing, including targeted web scraping, automated data cleaning, and comprehensive exploratory data analysis (EDA). 

This toolkit is built with a **controller-logic architecture**, allowing individual modules to run independently for specific tasks or as a unified pipeline via a master script.

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🏗️ System Architecture

The toolkit follows a professional **ETL (Extract, Transform, Load)** pattern. Data flows seamlessly from web-based sources into a standardized, cleaned state, followed by deep statistical profiling.



### 1. Web Extraction Engine (`webscraper.py`)
* **Capability**: Parses and extracts structured data from complex HTML environments using `BeautifulSoup4`.
* **Applied Use Case**: Configured for **Fortune 500 Financial Data**, extracting the largest US companies by revenue from Wikipedia and converting financial string notations into analysis-ready numeric formats.

### 2. Data Engineering Pipeline (`data_Cleaner.py`)
* **Capability**: An OOP-based ETL pipeline that implements **Regex-driven standardization** and business logic validation.
* **Applied Use Case**: Validated on **Tech Layoffs & Contact Datasets**, utilizing automated deduplication and phone/address parsing to achieve a **99.8% data retention rate**.

### 3. Automated EDA Suite (`eda_analyzer.py`)
* **Capability**: A statistical engine that generates high-fidelity reports and visualizations using `Seaborn` and `Matplotlib`.
* **Analysis Suite**: Performs automated outlier detection (IQR method), identifies strong correlations (|r| > 0.7), and calculates distribution metrics (Skewness/Kurtosis).

---

## 🚀 The Master Pipeline

The project features a `master_pipeline.py` script that automates the entire data lifecycle. It features **OS-agnostic pathing** (using Python's `os` module), ensuring the code runs flawlessly on Windows, macOS, or Linux.

### **Pipeline Workflow:**
1.  **Scrape**: Extracts raw corporate data from Wikipedia into the `/data` folder.
2.  **Clean**: Processes raw CSVs (e.g., Tech Layoffs), standardizes formats via Regex, and outputs validated versions.
3.  **Analyze**: Consumes the cleaned data to produce statistical summaries and visual plots in the `/reports` folder.

--- 

## 🛠️ Installation & Usage
1. Requirements

Install the necessary data science stack via terminal:

Bash
pip install pandas requests beautifulsoup4 seaborn matplotlib numpy scipy
2. Running the Full Pipeline

To execute the end-to-end workflow (Scrape → Clean → Analyze) automatically:

Bash
python master_pipeline.py
3. Running Individual Modules

Modules can also be run standalone for specific localized tasks:

Bash
# To scrape Fortune 500 data
python webscraper.py

# To clean the layoffs dataset
python data_Cleaner.py

# To perform EDA on existing data
python eda_analyzer.py
## 📊 Sample Performance Metrics
Data Cleaning: Achieved a 99.8% retention rate on 2,300+ record datasets by implementing intelligent duplicate detection.

EDA Speed: Processes comprehensive statistical profiling for multi-dimensional data in < 2 seconds.

Accuracy: Utilizes Scipy-backed statistical calculations for high-precision skewness, kurtosis, and Pearson correlations.

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

📬 Contact
Poorna Venkat Neelakantam 📧 pvneelakantam@gmail.com

🔗 LinkedIn Profile
