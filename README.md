# Survival Analysis – Telco Churn (Homework 3)

This project analyzes Telco customer churn using **parametric survival models** (AFT models).  
The goal is to understand churn behavior, compare different AFT distributions, interpret the final model, and compute Customer Lifetime Value (CLV).

## 🔧 How to Run
1. Create a virtual environment  
2. Install dependencies:



## 📌 Summary of Results
- Compared **Weibull**, **Log-Logistic**, and **Log-Normal** AFT models  
- **Log-Normal** had the lowest AIC → selected as best model  
- No features were statistically significant at p < 0.05  
- Churn appears driven by overall user behavior rather than individual predictors  
- CLV computed using survival probability at 12 months  
- Customer categories differ in CLV → helpful for retention targeting

See **report.md** for the full analysis, interpretations, and recommendations.
