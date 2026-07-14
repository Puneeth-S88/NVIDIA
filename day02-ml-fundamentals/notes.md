# Day 2: ML Fundamentals on GPU (Titanic Dataset Pipeline)

## Dataset
Titanic dataset — 891 rows, 15 columns (loaded via Seaborn with a raw
GitHub CSV fallback). Also briefly tested loading Tips and Iris datasets.

## What I did (pipeline order)
1. **Data loading** — tested 3 sources (GitHub CSV, Seaborn, sklearn).
2. **Data cleaning** — filled missing `age` (median), `embarked`/`embark_town`
   (mode), handled missing `deck`, removed 110 duplicate rows.
3. **EDA & outliers** — boxplots for fare/age; IQR method found 102 fare
   outliers, Z-score method (threshold=3) found 20.
4. **Survival analysis** — countplots by class/gender, age KDE by survival.
   Females had ~74% survival rate vs ~19% for males.
5. **Correlation heatmap** — strongest correlations: pclass vs fare (-0.55),
   survived vs pclass (-0.33).
6. **Feature engineering** — created `family_size` and `is_alone`.
7. **Encoding** — label-encoded `sex`, one-hot encoded `embarked`, ordinal
   mapped `class`.
8. **Scaling** — compared StandardScaler, MinMaxScaler, RobustScaler on
   age/fare.
9. **Feature selection** — SelectKBest (k=4) and RFE (n=4) to find top
   predictive features.
10. **PCA** — reduced features to 2 components for visualization.
11. **Train/test split** — 80/20, stratified by survival.
12. **Cross-validation** — 5-fold KFold on Logistic Regression.
13. **Class imbalance** — attempted SMOTE (imblearn), fallback to manual
    oversampling if not installed.
14. **Regression models** (target=fare) — Linear, Polynomial (deg 2),
    Decision Tree, Random Forest.
15. **Classification models** (target=survived) — Logistic Regression,
    KNN, Decision Tree, Random Forest, SVM, Naive Bayes.
16. **Clustering** — K-Means (elbow method), Agglomerative, DBSCAN on
    age/fare.
17. **Evaluation** — accuracy/precision/recall/F1 table, confusion matrix
    (Random Forest), ROC curves comparing all classifiers.

## Key commands used today
- Worked entirely inside JupyterHub (browser) after `kubectl exec` +
  `jupyter notebook --NotebookApp.token='...'` from Day 1 setup.
- No new kubectl/terminal commands — all work was in notebook cells.

## Issues / notes
- `imblearn` may not be pre-installed on the container — code has a
  manual oversampling fallback for that case.
- `ci=None` in `sns.barplot` may show a deprecation warning depending on
  seaborn version — safe to ignore for this run.

## AI tool disclosure
Used Claude to help debug JupyterHub/kubectl access issues and to
organize today's notebook code into structured, documented script files
for the GitHub repo.