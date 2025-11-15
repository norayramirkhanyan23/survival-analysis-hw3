# Survival Analysis Report – Telco Customer Churn

## 1. Introduction
The objective of this project is to analyze customer churn behavior in a Telco service provider using **Survival Analysis**, specifically **Accelerated Failure Time (AFT)** models. The analysis focuses on modeling customer lifetime, comparing several parametric survival models, interpreting the results, and estimating Customer Lifetime Value (CLV). Understanding churn dynamics allows the business to identify valuable customer segments and design effective retention strategies.

The dataset includes 1,000 subscribers with demographic, service usage, and behavioral variables. The key survival variables are **tenure** (customer lifetime) and **churn** (event indicator: 1 = churned, 0 = active).

---

## 2. Data Preparation
Before modeling, all categorical variables—such as marital status, gender, internet usage, customer category, region, and education level—were transformed into numerical dummy variables using one-hot encoding. No missing values were present in the dataset.

After encoding, the modeling dataset consisted of **20 predictors**, along with the survival time (`tenure`) and event indicator (`churn`). The data was fully clean and ready for fitting parametric AFT models.

---

## 3. Model Building and Comparison
Three parametric AFT models were fitted:

- **Weibull AFT**
- **Log-Logistic AFT**
- **Log-Normal AFT**

The performance of each model was evaluated using **Akaike Information Criterion (AIC)**, where a lower value indicates a better fit.

**AIC Results (approximate):**
- Weibull: ~2964  
- Log-Logistic: ~2956  
- **Log-Normal: ~2954 (Best Model)**  

The **Log-Normal AFT model** demonstrated the lowest AIC and was selected as the best-performing model.

---

## 4. Interpretation of the Final Model
The coefficient summary for the Log-Normal AFT model showed that **none of the covariates were statistically significant at the 5% level**. This result suggests that:

- No individual behavioral or demographic characteristic has a strong effect on the timing of churn.
- Churn behavior appears to follow an overall population trend rather than feature-specific patterns.
- The dataset likely represents a scenario where churn varies randomly rather than being strongly driven by specific predictors.

This phenomenon is common in synthetic Telco datasets, where churn markers are not intentionally tied to meaningful behavioral variables.

---

## 5. Survival Curve Analysis
Survival curves were generated for all three AFT models. The Log-Normal curve decays the slowest, indicating that it predicts longer customer retention compared to the Weibull and Log-Logistic models. The Weibull model predicts the fastest churn, and the Log-Logistic curve lies between the two.

These patterns align with the AIC comparison and further support choosing the **Log-Normal AFT model** as the final model for interpretation and downstream analysis.

---

## 6. Customer Lifetime Value (CLV) Estimation
CLV was calculated using survival probabilities predicted by the final Log-Normal model. The formula used was:

**CLV = Survival Probability at 12 Months × Monthly Revenue × 12**

A placeholder monthly revenue of **10 units** was used for demonstration.

CLV was computed for every customer, then aggregated by customer category. Customer categories with higher survival probabilities naturally showed higher CLV. These customers represent the most valuable segments for the company.

This type of segmentation helps the business determine which groups are most profitable to invest in when planning retention strategies.

---

## 7. Conclusion
The analysis shows that the **Log-Normal AFT model** provides the best fit for modeling Telco churn. Although no single feature had a statistically significant effect on churn time, the survival and CLV analyses offer valuable insights:

- The overall churn behavior follows a general lifetime distribution rather than being feature-driven.
- Customer categories differ meaningfully in their predicted CLV.
- High-CLV segments should be prioritized for retention investments.
- Survival modeling combined with CLV estimation provides a quantitative foundation for designing data-driven retention strategies.

This approach supports more efficient allocation of the annual retention budget and allows the company to focus on the customers who are most likely to generate long-term value.




