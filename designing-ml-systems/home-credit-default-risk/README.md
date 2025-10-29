# 🧠 A Classification Problem Workflow

## 1. Check Target Value — Is It Imbalanced?

```python
df.groupby("TARGET").size()
```

---

## 2. Check Predictors

### 2.1 Data Types Overview
```python
df.dtypes.value_counts()
```

### 2.2 Numeric Columns
```python
num_cols = df.select_dtypes(include='number').columns.tolist()
num_cols_nonbinary = [x for x in num_cols if all(words not in x for words in ["FLAG", "NOT"])]
```

### 2.3 Binary Columns
```python
num_cols_binary = [_ for _ in num_cols if _ not in num_cols_nonbinary]
print(len(num_cols_binary))
```

### 2.4 Categorical Columns
```python
df.select_dtypes(include='object').columns.tolist()
```

---

## 2.5 Validate Binary Columns
Check that all numeric binary columns are either 0 or 1.

---

## 2.6 Outliers (for Linear Models)

### Detection Methods
- Human judgement (e.g., placeholder values)
- IQR / Boxplot
- Model-based (e.g., isolation forest)

### Treatment Options
- ✅ True but extreme → consider **tree-based models**
- ❌ Erroneous → remove or **cap (winsorize)** to quantile value
- 🧩 Missing/Unknown → **impute with mode/median**

---

## 3. Handle Missing Values

> **Note:** Tree-based models (e.g., XGBoost) can handle missing values directly,  
> but distance-based or linear models (Regression, SVM, KNN, NN) require imputation.

### 3.1 Categorical Variables
| Missing % | Treatment |
|------------|------------|
| < 5% | Impute with mode |
| ≥ 5% | Create new category `"Unknown"` |

### 3.2 Numeric Variables
| Missing % | Treatment |
|------------|------------|
| < 5% | Impute with median |
| ≥ 5% | Impute with mean + create missing flag column |

---

## 4. Column Transformation

### 4.1 Categorical Variables
- One-hot encoding

### 4.2 Numeric Variables
- Scaling (StandardScaler, MinMax, etc.)
- *(Optional)* PCA with `n_components=0.99`

---

## 5. Feature Engineering

> ⚙️ Feature engineering is domain-specific.  
> I learned many ideas from my friend [@Alan Li](https://github.com/AlanJYLi/project_loan_default_detection).

Typical techniques include:
- Ratio or interaction features
- Group statistics (mean, count, std by category)
- Time-based or lag features (if temporal data)

---

## 6. Model Training

### Key Steps
1. Apply **SMOTE** *after* column transformation, *before* model training  
   - ⚠️ Caveats: Adds training burden and may not always help.
2. Define parameter grid
3. Apply **K-Fold Cross-Validation**
4. *(Optional)* Advanced tuning:
   - **Optuna** (Bayesian optimization + early stopping)
   - **Ray Tune** (ASHA, distributed tuning)

---

📘 **End-to-End Goal:**  
Create a robust, interpretable classification pipeline balancing data quality, feature engineering, and model performance.
