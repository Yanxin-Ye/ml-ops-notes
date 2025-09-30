import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class OutlierAndNaNImputer(BaseEstimator, TransformerMixin):
    """
    For a single numeric column:
      - Threshold is either fixed (upper) or quantile-based (q).
      - Impute NaNs with mean(inliers)
      - Impute values > upper with median(inliers)
    """

    def __init__(self, upper=None, q=None, fallback=0.0):
        if (upper is None) == (q is None):
            raise ValueError("Specify exactly one of 'upper' or 'q'.")
        self.upper = upper
        self.q = q
        self.fallback = fallback

    def fit(self, X, y=None):
        x = np.asarray(X, dtype=float).ravel()

        # decide threshold
        if self.q is not None:
            self.upper_ = np.nanquantile(x, self.q)
        else:
            self.upper_ = float(self.upper)

        inliers = x[(~np.isnan(x)) & (x <= self.upper_)]
        if inliers.size == 0:
            # fallback if all missing or above cutoff
            inliers = x[~np.isnan(x)]
        if inliers.size == 0:  # truly all missing
            self.mean_missing_ = self.fallback
            self.median_outlier_ = self.fallback
        else:
            self.mean_missing_ = float(np.nanmean(inliers))
            self.median_outlier_ = float(np.nanmedian(inliers))
        return self

    def transform(self, X):
        x = np.asarray(X, dtype=float).ravel()
        out = x.copy()
        # 1) NaNs → mean
        nan_mask = np.isnan(out)
        if nan_mask.any():
            out[nan_mask] = self.mean_missing_
        # 2) Outliers → median
        out[out > self.upper_] = self.median_outlier_
        return out.reshape(-1, 1)

    def get_feature_names_out(self, input_features=None):
        if input_features is None:
            return np.array(["feature"])
        return np.asarray(input_features)
