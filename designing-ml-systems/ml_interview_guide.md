# 1. Your model failed. Why?

**Model Assumptions**  
**Poor implementation of model**  
**Poor choice of hyperparameters**  
**Data problems**  
**Poor choice of features**  

**Some thing you can do?** No scientific approach to debug ML model  
Start simple and gradually add more components  
Overfit a single batch  
Set a random seed  

---

# 2. What is data leakage and how to prevent it?

Data leakage is when a form of label leaks into the set of features used for making predictions, but the same info is not available during model inference.  

- Measure the prediction power of each feature or a set of features. If a feature has unusually high correlation, investigate.  
- Measure importance of features. If removing a feature or a set of features cause model performance to deteriorate significantly, investigate.  
- Be careful with your test split. Test split should only be used to report a model’s final performance.  

---

# 3. Explain precision, recall, and the F1 score, AUC-ROC score.

All three help us get a better understanding of how well a model performed in a classification model.  
No one number can tell us if a model is good or not, so we often have to look at a confusion matrix to make our assessment.
  
1. **Precision:** Measures how well a model makes a positive prediction. It is the number of TP/(TP+FP). Looking at precision is vital when the cost of a false positive is high, e.g., spam email classification prefers high precision.  
2. **Recall:** Measures how well a model makes a negative prediction. It is the number of TP/(TP+FN). Looking at recall is vital when the cost of a false negative is high, e.g., detecting lung cancer from x-ray prefers high recall.  
3. **F1 Score:** A function of precision and recall. It gives us a more balanced understanding of how well our model performs, especially if we started with imbalanced training data.  
F1 = 2*Precision*Recall/(Precision+Recall)  
4. **AUC-ROC:** The probability that a randomly chosen positive sample gets a higher predicted score than a randomly chosen negative sample.  
ROC:  
   - X-axis: False Positive Rate (FPR) = FP / (FP + TN)  
   - Y-axis: True Positive Rate (TPR) = TP / (TP + FN)  

AUC-ROC score measures the probability that a randomly chosen positive sample gets a higher predicted score than a randomly chosen negative sample.

---

# 4. Handle skewed data.

| Type | Example | What Skew Looks Like | Typical Fix |
|------|----------|----------------------|--------------|
| Regression | Sales, income, duration | Long-tailed (non-symmetric) | Log/Box-Cox transform |
| Classification | Fraud/Churn | One class dominates | Re-sampling or class weighting |

## 4.1 Long-tailed data in continuous data
**Why it matters:**  
- Many models (like linear regression) assume residuals are normally distributed.  
- Skewness can cause the model to fit poorly to the majority of data and overemphasize outliers.  

In the right-skewed distribution: Mode < Median < Mean  
In the left-skewed distribution: Mean < Median < Mode  

## 4.2 Imbalance data in a classification problem
Usually when a class is less than 10% of total data, it can be considered as an imbalanced dataset.  

**Why it matters:**  
If only 1% transactions are fraud, a model can predict `no fraud` all the time and still gets a 99% accuracy.

### a) Data level:
- Collect more data in minority class  
- Undersample: might remove important data  
- Oversample: might overfit (SMOTE), add a lot of training burdens  

**To mitigate:**  
- Two-phase learning: train on resampled data, fine tune on original data  
- Dynamic sampling: oversample the low-performing class and undersample the high performing class during training.  

### b) Metric level:
Check precision/recall, f1, AUC-ROC score  

### c) Algorithm level:
Add stronger penalty on misclassifying the minority class in loss function:

**In logistic regression:**  
```
L1, L2, elastic_net in `soga` solver
set clf_class_weight = "balanced" and let CV choose
```

**In XGBoost:**  
```
pos = int(np.sum(y_train == 1))
neg = int(np.sum(y_train == 0))
spw = neg / max(pos, 1)
scale_pos_weight=spw
```

---

# 5. How to determine if a feature is good?

a) **Feature importance:**  
Built-in feature importance in classic models such as XGBoost.  
Shapley value  

b) **Feature generalization:** does the feature generalize to unseen data  
Bad examples: user_id in predicting hate speech,  
Domain knowledge  

c) **Coverage of feature:** how many data are missing  
**Feature value distribution:** if the train data has a set of values with no overlap with that of test data, the feature won’t generalize.

