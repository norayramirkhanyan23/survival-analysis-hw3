import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from lifelines import WeibullAFTFitter, LogLogisticAFTFitter, LogNormalAFTFitter

df = pd.read_csv("telco.csv")

if df["churn"].dtype == "O":
    df["churn"] = df["churn"].map({"Yes": 1, "No": 0})

duration_col = "tenure"
event_col = "churn"

cat_cols = [
    "marital", "retire", "gender", "voice", "internet",
    "forward", "custcat", "region", "ed"
]

df_model = pd.get_dummies(df, columns=cat_cols, drop_first=True)

if "ID" in df_model.columns:
    df_model = df_model.drop(columns=["ID"])

aft_models = {
    "Weibull": WeibullAFTFitter(),
    "Log-Logistic": LogLogisticAFTFitter(),
    "Log-Normal": LogNormalAFTFitter(),
}

results = {}
aic_values = {}

for name, model in aft_models.items():
    model.fit(df_model, duration_col=duration_col, event_col=event_col)
    results[name] = model
    aic_values[name] = model.AIC_

best_name = min(aic_values, key=aic_values.get)
best_model = results[best_name]

summary = best_model.summary.copy()

significant_features = []

if isinstance(summary.index, pd.MultiIndex):
    param_level = summary.index.get_level_values(0)
    covar_level = summary.index.get_level_values(1)
    main_param_mask = param_level.isin(["mu_", "lambda_"])
    not_intercept_mask = covar_level != "Intercept"
    p_mask = summary["p"] < 0.05
    sig = summary[main_param_mask & not_intercept_mask & p_mask]
    significant_features = sig.index.get_level_values(1).unique().tolist()
else:
    sig = summary[(summary.index != "Intercept") & (summary["p"] < 0.05)]
    significant_features = sig.index.tolist()

if len(significant_features) == 0:
    final_cols = [duration_col, event_col]
else:
    final_cols = [duration_col, event_col] + significant_features

df_final = df_model[final_cols].copy()

FinalModelClass = type(best_model)
final_model = FinalModelClass()
final_model.fit(df_final, duration_col=duration_col, event_col=event_col)

X_mean = df_model.drop(columns=[event_col]).mean().to_frame().T

plt.figure(figsize=(10, 6))
for name, model in results.items():
    sf = model.predict_survival_function(X_mean)
    times = sf.index.values
    surv = sf.values[:, 0]
    plt.step(times, surv, where="post", label=name)
plt.title("Survival Curves – AFT Models (typical subscriber)")
plt.xlabel("Tenure (time)")
plt.ylabel("Survival probability")
plt.legend()
plt.tight_layout()
plt.savefig("aft_models_survival.png")
plt.show()

revenue_per_month = 10
T = 12

surv_T = final_model.predict_survival_function(df_final, times=[T]).T[T]
df_final["surv_T"] = surv_T
df_final["CLV"] = df_final["surv_T"] * revenue_per_month * T
df_final = df_final.join(df.loc[df_final.index, "custcat"])

print("\nAIC values:", aic_values)
print("\nBest model:", best_name)
print("\nSignificant features:", significant_features)
print("\nAverage CLV by customer category:")
print(df_final.groupby("custcat")["CLV"].mean().sort_values(ascending=False))
