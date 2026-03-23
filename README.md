# 🐍 Python Data Analysis Portfolio

A collection of Python-based data analysis projects demonstrating end-to-end analytics capabilities, from data wrangling and statistical analysis to machine learning and visualization.

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🚀 Featured Projects

### 1. [SaaS Customer Churn Prediction & Retention Analytics](./03_Saas_Churn_Prediction/)

**Focus:** Churn Prediction, Classification Models, Feature Engineering, Business Analytics

📊 **[View Interactive Dashboard](https://public.tableau.com/app/profile/poorna.venkat.neelakantam/viz/SaaSCustomerChurnAnalyticsDashboard/Homepage)**

* **Problem:** RavenStack, an AI SaaS startup, was experiencing 22% churn across 500 accounts, losing $1.2M in monthly recurring revenue before public launch.
* **Solution:** Built end-to-end churn prediction system — engineered 10 behavioral features from 5 relational tables (33K+ records), trained 3 classification models, and generated ranked at-risk customer lists for proactive retention.
* **Key Results:**
  * Achieved **85.73% AUC-ROC** with Random Forest (92.31% Precision)
  * Identified **$1.1M MRR at risk** from 123 active medium-risk accounts
  * Discovered **error rate is #1 churn driver** — not support quality (contradicting initial assumptions)
  * Found **DevTools Enterprise** churns at 45.5% vs 22% overall
  * Event referrals churn **3x more** than partner referrals (34.5% vs 12.8%)
* **Tech:** Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, Seaborn

**Sample Code - Feature Engineering & Model Training:**
```python
# Engineer behavioral features from 5 raw tables
master_df['error_rate'] = (
    master_df['total_errors'] / master_df['total_usage_count'].replace(0, 1)
).round(4)

master_df['engagement_score'] = MinMaxScaler().fit_transform(
    master_df[['distinct_features_used', 'total_usage_count', 'avg_usage_duration_secs']]
).mean(axis=1).round(4)

master_df['mrr_per_seat'] = (
    master_df['latest_mrr'] / master_df['seats'].replace(0, 1)
).round(2)

# Train Random Forest with class imbalance handling
from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(
    n_estimators=200, max_depth=10,
    class_weight='balanced',  # handles 22% vs 78% imbalance
    random_state=42
)
rf_model.fit(X_train_scaled, y_train)
# Result: AUC 85.73%, Precision 92.31%
```

**Model Comparison:**
| Model | Accuracy | Precision | Recall | F1 Score | ROC AUC |
|-------|----------|-----------|--------|----------|---------|
| Logistic Regression | 66.67% | 35.71% | 58.82% | 44.44% | 64.91% |
| **Random Forest** | **84.67%** | **92.31%** | **35.29%** | **51.06%** | **85.73%** |
| XGBoost | 80.67% | 60.87% | 41.18% | 49.12% | 82.96% |

**Notebooks:**
| Notebook | Description |
|----------|-------------|
| `01_data_exploration.py` | Data loading, quality assessment, EDA, 11 visualizations |
| `02_churn_prediction.py` | Feature engineering, 3 ML models, evaluation, at-risk scoring |

---

### 2. [E-Commerce Customer Analytics & RFM Segmentation](./02_Ecommerce-Customer-Analytics/)

**Focus:** Customer Segmentation, RFM Analysis, K-Means Clustering

📊 **[View Interactive Dashboard](https://public.tableau.com/app/profile/poorna.venkat.neelakantam/viz/E-CommerceCustomerAnalyticsDashboard/Dashboard1)**

* **Problem:** E-commerce company needed to segment 96,477 customers to optimize marketing spend and reduce churn.
* **Solution:** Built RFM (Recency, Frequency, Monetary) scoring model and validated segments using K-Means clustering with Scikit-learn.
* **Key Results:**
  * Identified R$2.9M revenue opportunity from churned customers
  * Segmented customers into 10 actionable groups (Champions, At-Risk, Lost, etc.)
  * Achieved 0.485 silhouette score with optimal 3-cluster solution
* **Tech:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn

**Sample Code - RFM Calculation:**
```python
# Calculate RFM metrics for 96,477 customers
rfm = df_delivered.groupby('customer_id').agg({
    'order_purchase_timestamp': lambda x: (snapshot_date - x.max()).days,  # Recency
    'order_id': 'count',                                                    # Frequency
    'payment_total': 'sum'                                                  # Monetary
})

# Create quartile-based scores
rfm['R_Quartile'] = pd.qcut(rfm['Recency'], 4, labels=['4','3','2','1'])
rfm['F_Quartile'] = pd.qcut(rfm['Frequency'].rank(method='first'), 4, labels=['1','2','3','4'])
rfm['M_Quartile'] = pd.qcut(rfm['Monetary'], 4, labels=['1','2','3','4'])

# K-Means clustering validation
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(rfm[['Recency', 'Frequency', 'Monetary']])
kmeans = KMeans(n_clusters=3, random_state=42)
rfm['Cluster'] = kmeans.fit_predict(X_scaled)
```

**Notebooks:**
| Notebook | Description |
|----------|-------------|
| `01_data_exploration.ipynb` | Data loading, cleaning, merging 5 datasets |
| `02_rfm_analysis.ipynb` | RFM calculation & customer segmentation |
| `03_customer_segmentation.ipynb` | K-Means clustering & validation |

---

### 3. [Data Analysis Toolkit](./01-Data-Analysis-Toolkit/)
**Focus:** Web Scraping, Data Cleaning (ETL), Exploratory Data Analysis

A modular Python framework designed for end-to-end data processing, including targeted web scraping, automated data cleaning, and comprehensive exploratory data analysis (EDA).

Built with a **controller-logic architecture**, allowing individual modules to run independently or as a unified pipeline via a master script.

#### 🏗️ System Architecture

The toolkit follows a professional **ETL (Extract, Transform, Load)** pattern:

| Module | Capability | Use Case |
|--------|------------|----------|
| `webscraper.py` | Parses HTML using BeautifulSoup4 | Fortune 500 Financial Data extraction |
| `data_Cleaner.py` | OOP-based ETL with Regex standardization | Tech Layoffs dataset (99.8% retention) |
| `eda_analyzer.py` | Statistical engine with Seaborn/Matplotlib | Automated outlier detection, correlations |

#### 🚀 The Master Pipeline

```bash
# Run the full pipeline: Scrape → Clean → Analyze
python master_pipeline.py

# Or run individual modules
python webscraper.py      # Scrape Fortune 500 data
python data_Cleaner.py    # Clean layoffs dataset
python eda_analyzer.py    # Perform EDA
```

#### 📊 Performance Metrics
* **Data Cleaning:** 99.8% retention rate on 2,300+ records
* **EDA Speed:** < 2 seconds for comprehensive statistical profiling
* **Accuracy:** Scipy-backed calculations for skewness, kurtosis, correlations

---

## 📊 Project Summary

| Project | Dataset Size | Key Techniques | Business Impact |
|---------|--------------|----------------|-----------------|
| SaaS Churn Prediction | 33K+ records (5 tables) | Random Forest, XGBoost, Feature Engineering | $1.1M MRR at risk identified, 85.73% AUC |
| E-Commerce RFM Analysis | 100K+ orders | RFM, K-Means, Pandas | R$2.9M revenue opportunity |
| Data Analysis Toolkit | 2,300+ records | ETL, Web Scraping, EDA | 99.8% data retention |

---

## 🛠️ Technical Toolkit

| Category | Technologies |
|----------|--------------|
| **Data Manipulation** | Pandas, NumPy |
| **Machine Learning** | Scikit-learn (Random Forest, Logistic Regression, K-Means, StandardScaler) |
| **Gradient Boosting** | XGBoost (with class imbalance handling) |
| **Visualization** | Matplotlib, Seaborn |
| **Web Scraping** | BeautifulSoup4, Requests |
| **Statistics** | SciPy (Skewness, Kurtosis, Pearson) |
| **Model Evaluation** | ROC-AUC, Precision-Recall, Confusion Matrix, Cross-Validation |
| **Development** | Jupyter Notebook, Git |

---



---

## 🚀 Installation & Usage

### Requirements
```bash
pip install pandas numpy scikit-learn xgboost matplotlib seaborn scipy beautifulsoup4 requests jupyter
```

### Running SaaS Churn Prediction
```bash
cd 03-saas-churn-prediction
jupyter notebook
# Run: 01_data_exploration.py → 02_churn_prediction.py
```

### Running E-Commerce Analysis
```bash
cd 01-ecommerce-rfm-analysis
jupyter notebook
# Run notebooks in sequence: 01 → 02 → 03
```

### Running Data Toolkit Pipeline
```bash
cd 02-data-analysis-toolkit
python master_pipeline.py
```

---

## 🔗 Related Repositories

| Repository | Description |
|------------|-------------|
| 📊 [Dashboard Portfolio](https://github.com/poornavenkatn08/dashboards-portfolio) | Tableau & Power BI visualizations |
| 🗃️ [SQL Projects](https://github.com/poornavenkatn08/SQL-Projects) | MySQL analytics & data engineering |

---

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 📬 Contact

**Poorna Venkat Neelakantam**

📧 [pvneelakantam@gmail.com](mailto:pvneelakantam@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/pneelakantam/)  
💻 [GitHub](https://github.com/poornavenkatn08)  
📊 [Tableau Public](https://public.tableau.com/app/profile/poorna.venkat.neelakantam)
