# E-Commerce RFM Analysis & Customer Segmentation

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

## 📊 Live Dashboard

**[View Interactive Tableau Dashboard →](https://public.tableau.com/app/profile/poorna.venkat.neelakantam/viz/E-CommerceCustomerAnalyticsDashboard/Dashboard1)**

---

## 🎯 Project Overview

Customer segmentation analysis using **RFM (Recency, Frequency, Monetary)** methodology and **K-Means clustering** on 100,000+ e-commerce orders. This project demonstrates data wrangling, feature engineering, and machine learning techniques for customer analytics.

---

## 📓 Notebooks

| Notebook | Description | Key Techniques |
|----------|-------------|----------------|
| `01_data_exploration.ipynb` | Data loading, cleaning, merging | Pandas merge, missing value analysis |
| `02_rfm_analysis.ipynb` | RFM calculation & segmentation | GroupBy, qcut, custom functions |
| `03_customer_segmentation.ipynb` | K-Means clustering | StandardScaler, Elbow method, Silhouette score |

---

## 🔬 Methodology

### 1. Data Exploration & Cleaning

```python
# Merged 5 datasets into master dataframe
master_df = orders.merge(customers, on='customer_id')
                  .merge(order_items, on='order_id')
                  .merge(payments, on='order_id')

# Result: 99,441 records, 17 features
```

**Key Steps:**
- Loaded 5 CSV files (orders, customers, items, payments, reviews)
- Handled datetime conversions
- Addressed 2.98% missing values in delivery dates
- Created unified master dataset

### 2. RFM Analysis

```python
# Calculate RFM metrics
rfm = df_delivered.groupby('customer_id').agg({
    'order_purchase_timestamp': lambda x: (snapshot_date - x.max()).days,  # Recency
    'order_id': 'count',                                                    # Frequency
    'payment_total': 'sum'                                                  # Monetary
})

# Create quartile-based scores
rfm['R_Quartile'] = pd.qcut(rfm['Recency'], 4, labels=['4','3','2','1'])
rfm['F_Quartile'] = pd.qcut(rfm['Frequency'].rank(method='first'), 4, labels=['1','2','3','4'])
rfm['M_Quartile'] = pd.qcut(rfm['Monetary'], 4, labels=['1','2','3','4'])
```

**Customer Segments Created:**
- Champions
- Loyal Customers
- Potential Loyalists
- New Customers
- Promising
- Need Attention
- About to Sleep
- At Risk
- Cannot Lose Them
- Lost

### 3. K-Means Clustering

```python
# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(rfm[['Recency', 'Frequency', 'Monetary']])

# Find optimal clusters using Elbow & Silhouette
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    silhouette_scores.append(silhouette_score(X_scaled, kmeans.labels_))

# Optimal k=3 with silhouette score = 0.485
```

---

## 📈 Results

### RFM Statistics

| Metric | Mean | Std | Min | Max |
|--------|------|-----|-----|-----|
| Recency (days) | 240 | 153 | 1 | 696 |
| Frequency | 1.0 | 0.0 | 1 | 1 |
| Monetary (R$) | 160 | 219 | 9.59 | 13,664 |

### Clustering Performance

| K | Inertia | Silhouette Score |
|---|---------|------------------|
| 2 | 125,045 | 0.448 |
| **3** | **74,831** | **0.485** ✓ |
| 4 | 59,383 | 0.410 |
| 5 | 44,534 | 0.427 |

---

## 📊 Visualizations

### RFM Analysis
![RFM Analysis](./outputs/rfm_analysis.png)

### Customer Clusters (3D)
![3D Clusters](./outputs/customer_clusters_3d.png)

---

## 🛠️ Tech Stack

| Library | Version | Purpose |
|---------|---------|---------|
| pandas | 2.0+ | Data manipulation |
| numpy | 1.24+ | Numerical operations |
| scikit-learn | 1.3+ | K-Means clustering |
| matplotlib | 3.7+ | Visualization |
| seaborn | 0.12+ | Statistical plots |

---

## 📁 Project Structure

```
01-ecommerce-rfm-analysis/
│
├── 📓 01_data_exploration.ipynb
├── 📓 02_rfm_analysis.ipynb
├── 📓 03_customer_segmentation.ipynb
│
├── 📂 data/
│   ├── raw/                    # Original Kaggle CSVs
│   └── processed/
│       ├── master_dataset.csv
│       └── rfm_analysis_with_id.csv
│
├── 📂 outputs/
│   ├── rfm_analysis.png
│   └── customer_clusters_3d.png
│
└── README.md
```

---

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/poornavenkatn08/Python_Pandas-Data-Analysis-Portfolio.git
cd Python_Pandas-Data-Analysis-Portfolio/01-ecommerce-rfm-analysis

# Install dependencies
pip install pandas numpy scikit-learn matplotlib seaborn jupyter

# Launch notebooks
jupyter notebook
```

---

## 🔗 Related Work

| Link | Description |
|------|-------------|
| 📊 [Tableau Dashboard](https://public.tableau.com/app/profile/poorna.venkat.neelakantam/viz/E-CommerceCustomerAnalyticsDashboard/Dashboard1) | Interactive visualization |
| 🗃️ [SQL Project](https://github.com/poornavenkatn08/SQL-Projects/tree/main/02-Ecommerce-Customer-Analytics) | Complete project with SQL queries |
| 📈 [Dashboard Portfolio](https://github.com/poornavenkatn08/dashboards-portfolio) | All Tableau dashboards |

---

## 📊 Dataset

**Source:** [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

- 100,000+ orders
- 96,477 unique customers
- Period: September 2016 - August 2018

---

## 👤 Author

**Poorna Venkat Neelakantam**
- [LinkedIn](https://linkedin.com/in/pneelakantam)
- [GitHub](https://github.com/poornavenkatn08)
- [Tableau Public](https://public.tableau.com/app/profile/poorna.venkat.neelakantam)

---

## 📄 License

This project is for educational and portfolio purposes. Dataset provided by Olist under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
