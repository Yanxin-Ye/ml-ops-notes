import json
import joblib
import pandas as pd
import numpy as np
from sklearn.metrics import make_scorer, roc_auc_score, f1_score, confusion_matrix, precision_recall_curve

def save_best_model(grid, output_path):
    best_model = grid.best_estimator_
    joblib.dump(best_model, output_path)
    print(f"✅ Model saved to {output_path}")

    # --- Step 5: Save metadata (optional but recommended) ---
    meta = {
        "best_params": grid.best_params_,
        "best_cv_auc": grid.best_score_
    }
    json_path = output_path.split(".")[0] + "_meta.json"
    with open(json_path, "w") as f:
        json.dump(meta, f, indent=2)

    print(f"✅ Metadata saved to {json_path}")


#Testing scores, confusion matrix
def model_performance(y_test,y_pred,y_pred_pr):
    print("f1_score: ", f1_score(y_test, y_pred))
    print("confusion matrix", confusion_matrix(y_test,y_pred))
    print("roc_auc_score: ", roc_auc_score(y_test,y_pred_pr))


#print result, draw bar graph for feature importance for non-pca method
def print_result(model,x_test):
    print(model)
    feat_importances = pd.Series(model.best_estimator_.feature_importances_, index=x_test.columns)
    feat_importances.nlargest(15).plot(kind='barh')
    return pd.DataFrame(model.cv_results_)

