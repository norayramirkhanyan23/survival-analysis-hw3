# Survival Analysis Report – Telco Customer Churn

## 1. Introduction
The objective of this analysis is to understand customer churn behavior in a Telco service provider using **Survival Analysis**, specifically **Accelerated Failure Time (AFT)** models.  
The project includes:

- Building multiple AFT parametric models  
- Comparing model fit using AIC  
- Interpreting coefficients of the final model  
- Plotting survival curves  
- Computing Customer Lifetime Value (CLV)  
- Identifying valuable customer segments for targeted retention  

The dataset contains 1,000 subscribers with demographic, service, and behavioral characteristics.

---

## 2. Data Preparation
The target variables for survival modeling are:

- **tenure** – customer lifetime (time until churn or censoring)  
- **churn** – event indicator (1 = churned, 0 = censored)

All categorical variables (`marital`, `retire`, `gender`, `voice`, `internet`, `forward`, `custcat`, `region`, `ed`) were encoded using one-hot encoding.  
No missing values were present.

The final modeling dataset contained 20 predictors.

---

## 3. Model Building and Comparison
Three parametric AFT models were fitted:

- **Weibull AFT**
- **Log-Logistic AFT**
- **Log-Normal AFT**

### AIC Results
| Model          | AIC   |
|----------------|--------|
| Weibull        | ~2964 |
| Log-Logistic   | ~2956 |
| **Log-Normal** | **~2954** |

**Log-Normal** exhibited the lowest AIC → selected as the best model.

---

## 4. Interpretation of the Final Model
The Log-Normal model summary showed that **none of the covariates were statistically significant at p < 0.05**.  
This means:

- Individual demographic or service variables do **not** strongly explain churn timing.
- Churn behavior follows an overall population trend.
- The survival curve reflects general customer lifetime rather than feature-specific variation.

This behavior is common in synthetic Telco datasets with random churn patterns.

---

## 5. Survival Curves
A combined survival plot of all AFT models was generated and saved as:


Observations:
- Log-Normal decays the slowest → higher predicted survival.
- Weibull decays faster → more pessimistic churn estimates.
- Log-Logistic lies between the two.

---

## 6. Customer Lifetime Value (CLV)
CLV was computed using:

