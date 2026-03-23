# SaaS Customer Churn Prediction & Retention Analytics — Python ML Analysis

## 📊 Project Overview

Built an **end-to-end churn prediction system** for RavenStack, an AI SaaS startup, using Python to perform exploratory data analysis, engineer 10+ predictive features from 5 relational tables, and train classification models achieving **85.73% AUC-ROC**, identifying **$1.1M+ MRR at risk** from active customers.

**Dataset:** RavenStack SaaS Subscription & Churn Analytics (by River @ Rivalytics)  
**Tools:** Python, Pandas, Scikit-learn, XGBoost, Matplotlib, Seaborn  
**Records:** 33,100+ across 5 tables → 500-row master analytics dataset  

---

## 🔬 Analysis Pipeline

```
Data Loading (5 CSVs)
    ↓
Data Quality Assessment (missing values, type checking)
    ↓
Exploratory Data Analysis (distributions, correlations, comparisons)
    ↓
Feature Engineering (10 new features from raw data)
    ↓
ML Model Training (3 models compared)
    ↓
Model Evaluation (AUC, Precision, Recall, F1)
    ↓
At-Risk Customer Scoring (ranked probability list)
```

---

## 🧪 Model Performance

| Model | Accuracy | Precision | Recall | F1 Score | ROC AUC |
|-------|----------|-----------|--------|----------|---------|
| Logistic Regression | 66.67% | 35.71% | 58.82% | 44.44% | 64.91% |
| Random Forest | 84.67% | 92.31% | 35.29% | 51.06% | **85.73%** |
| XGBoost | 80.67% | 60.87% | 41.18% | 49.12% | 82.96% |

**🏆 Best Model: Random Forest (AUC: 85.73%)**
- 92.31% Precision — when it flags a churner, it's right 92% of the time
- Used `class_weight='balanced'` to handle 22% vs 78% class imbalance
- 5-fold stratified cross-validation confirmed robust performance

---

## 🔧 Feature Engineering

Engineered **10 new features** from 5 raw tables to capture business-meaningful behavioral signals:

| Feature | Formula | Why It Predicts Churn |
|---------|---------|----------------------|
| `mrr_per_seat` | MRR ÷ seats | Value perception — low = might switch to cheaper alternative |
| `critical_ticket_ratio` | Critical tickets ÷ total tickets | High urgency = high frustration |
| `error_rate` | Total errors ÷ total usage events | **#1 churn driver** — buggy experience drives customers away |
| `beta_adoption_ratio` | Beta events ÷ total events | Innovation engagement level |
| `tickets_per_month` | Total tickets ÷ tenure months | Support intensity over time |
| `features_per_month` | Distinct features ÷ tenure months | Feature discovery velocity |
| `engagement_score` | Normalized composite (features × usage × duration) | Overall product engagement health |
| `is_enterprise` | Binary flag for Enterprise tier | Plan-level risk indicator |
| `is_us` | Binary flag for US-based customers | Geographic risk factor |
| `has_support_interaction` | Any support tickets filed | Support engagement indicator |

---

## 🎯 Top Churn Drivers (Feature Importance)

From Random Forest model:

| Rank | Feature | Importance | Business Implication |
|------|---------|------------|---------------------|
| 1 | **error_rate** | 0.0895 | Product bugs are the #1 reason customers leave |
| 2 | **avg_usage_duration_secs** | 0.0769 | Low engagement time = low perceived value |
| 3 | **avg_resolution_hours** | 0.0652 | Slow support correlates with churn risk |
| 4 | **total_usage_count** | 0.0632 | Lower activity signals disengagement |
| 5 | **latest_mrr** | 0.0624 | Revenue level affects churn patterns |
| 6 | **mrr_per_seat** | 0.0607 | Value perception per user matters |
| 7 | **total_errors** | 0.0594 | Cumulative error count compounds frustration |
| 8 | **seats** | 0.0544 | Team size influences stickiness |
| 9 | **distinct_features_used** | 0.0528 | Broader adoption = stronger retention |
| 10 | **critical_ticket_ratio** | 0.0435 | High urgency tickets signal risk |

---

## ⚠️ At-Risk Customer Identification

Model scored all 390 active customers with churn probability:

| Risk Level | Active Accounts | MRR at Risk |
|-----------|----------------|-------------|
| Low | 454 | $3,454,399 |
| Medium | 123 | $1,140,793 |
| High | 1 | $7,164 |
| Critical | 0 | $0 |

**Top at-risk account:** Company_159 (FinTech, Pro) — 58.70% churn probability, $7,164 MRR, satisfaction score 1.57/5.0

---

## 📊 Visualizations Generated

| Chart | What It Shows |
|-------|--------------|
| Churn Distribution (pie/donut) | 22% churn rate overview |
| Numeric Distributions | Revenue, usage, satisfaction spreads |
| Churn by Segments (plan, industry) | Which segments bleed most |
| Churned vs Retained Box Plots | Behavioral comparison across metrics |
| Churn Reasons (count + MRR) | Budget and support cost most revenue |
| Correlation Heatmap | Feature relationships with churn |
| Feature Importance (3 models) | What drives churn — side by side |
| Confusion Matrices | Model accuracy breakdown |
| ROC Curves | Model comparison on single chart |
| At-Risk Distribution | Risk level counts + MRR at risk |
| Engagement Score Histogram | Clear churn pattern at low engagement |

---

## 🛠️ Technical Skills Demonstrated

- **Pandas:** Multi-table merges, groupby aggregations, feature engineering, null handling
- **Scikit-learn:** Logistic Regression, Random Forest, StandardScaler, train/test split, cross-validation
- **XGBoost:** Gradient boosting with class imbalance handling (scale_pos_weight)
- **Matplotlib + Seaborn:** 11+ publication-quality visualizations
- **ML Best Practices:** Stratified splitting, data leakage prevention (excluded post-churn columns), proper scaling (fit on train only)
- **Business Thinking:** Translated model outputs into actionable at-risk customer lists and retention recommendations

---

## 📈 Key Insights

1. **Error rate is the #1 churn predictor** — product quality drives retention more than support or pricing
2. **Low engagement strongly predicts churn** — customers with engagement scores below 0.40 are high risk
3. **Support metrics show NO significant difference** between churned and retained — churn is NOT a support problem
4. **Retained customers upgrade 64% vs churned 58.8%** — upgrades signal commitment
5. **Random Forest achieves 92.31% precision** — highly reliable when flagging at-risk accounts

---

## 🔗 Related Work

- **SQL Analysis:** [SQL-Projects](https://github.com/poornavenkatn08/SQL-Projects)
- **Tableau Dashboard:** [dashboards-portfolio](https://github.com/poornavenkatn08/dashboards-portfolio)
- **Live Dashboard:** [View on Tableau Public](https://public.tableau.com/app/profile/poorna.venkat.neelakantam/viz/SaaSCustomerChurnAnalyticsDashboard/Homepage)

---

## 📁 Files

```
SaaS-Churn-Prediction/
├── notebooks/
│   ├── 01_data_exploration.py          # EDA + Feature Engineering
│   └── 02_churn_prediction.py          # ML Model Training + Evaluation
├── data/
│   ├── raw/                            # 5 original CSVs
│   └── processed/
│       ├── master_engineered.csv       # ML-ready dataset
│       ├── at_risk_customers.csv       # Scored customer list
│       ├── model_comparison.csv        # 3-model results
│       └── feature_importance.csv      # Ranked feature importance
├── dashboards/                         # 15 PNG visualization exports
├── requirements.txt
└── README.md
```

---

**Dataset Credit:** RavenStack dataset by River @ Rivalytics (MIT License, fully synthetic)
