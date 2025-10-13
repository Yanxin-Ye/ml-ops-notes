import json
import joblib


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
