## 3.0.0 (2026-02-20)
- Added:
  1. **New models in leaves:** Renet (SOTA Relaxed Elastic Net) and a custom implementation of Adaptive Elastic Net, offering slightly different accuracy-sparsity profiles
  2. **New Direct and Systemic Variable Importance** estimation: an upgrade to the traditional permutation feature importance
  3. **New Minimum Description Length** mode for leaves: simplest plausible leaf model when Renet gives OLS estimates.
  4. More public classes and methods (can be used as **standalone tools**): Renet, AdaptiveNetCV, FeatureImportance, turbosolve (method).
  5. Optional display of leaf model equation in tree plot
- Changed:
  1. Much **faster training** (5-20x)
  2. Small enhancements to explain() and Ghost Variable Importance estimation
  3. __init__ and fit method signatures changed to accomodate new capabilities and to align closer with scikit-learn conventions. This **breaks backward compatibility**, so it may require adapting existing pipelines accordingly for some users.
  4. Renamed the TRUST class as TRUSTRegressor (TRUSTClassifier is coming soon...). The TRUST class will still be around until version 4.0.0 to help transition.
  5. Minor bug fixes
- Removed:
  1. Traditional Permutation Feature Importance option (superseded by faster, more robust and 100% deterministic alternative, see second "Added" item)

## 2.1.4 (2025-11-16)
- Added:
  1. **Expanded compatibility (new platforms will be sequentially added)**
  2. Axis values in radar chart (compare method).
  3. Greedy feature order optimization (instead of exhaustive) in radar charts with more than 9 features.
  4. Pie and radar charts and saved to device in explain and compare method retain feature names when run in Jupyter too.
  5. Visual cues to convey training performance more easily.
  6. Automatic detection of potential overfitting.
- Changed:
  1. Changed prediction logic from recursive to iterative (more efficient).
  2. Reversed color scheme for bar chart in detailed mode for the compare method.
  3. Sorted dumbell plot from largest to smallest feature difference in compare method.
  4. Fixed bug in explain method for rare cases where no feature was statistically relevant.
  5. More accurate expected time to training completion after cross-validation.
  6. Swapped cosine similarity for angular similarity in compare() for more intuitive scaling.
  7. Other minor enhancements in explain() and compare() methods.

## 2.0.0 (2025-10-16)
- Added:
  1. **New compare() method** to allow head-to-head comparisons of data points.
  2. Automatic reporting and removal of duplicate columns.
  3. Automatic check for missing target values and corresponding removal of rows in training dataset.
  4. Automatic check for highly imbalanced categorical variables and switch from robust to standard scaling in those cases.
  5. Fallback to (TRUST-flavored) standard Lasso in leaf if all Relaxed Lasso coefficients are zero due to excessive regularization.
  6. Method show_leaf_coefficients(leaves = "all", enc_table = True, rnd = 2) to print coefficient summary tables for the selected leaves.
  7. Explicit node id, also in tree plot (leaves only).
- Changed:
  1. **Revamped explain() method** to be even more powerful *and* user friendly.
  2. Improved handling of categorical variables in Shap's waterfall plot
  3. Fixed bug in print_model() in absence of significant features.
  4. Threshold for 'large' lowered from 0.6 to 0.55, and threshold for 'intermediate' increased from 0.4 to 0.45.
  5. More efficient retrieval of encoded values: before it was O(n) now it's O(1). Should speedup prediction (and even fitting) noticeably.
  6. Internal method _fill_NAs now takes the feature matrix X instead of the complete dataset as input.
  7. df_X_train_original_withID for the all-complete df_Leaf_X_train_original_Y_Yhat.
  8. Faster prediction for depth-0 trees, and in general (iterative vs recursive approach).
  9. Faster variable importance calculation (both permutation and Ghost method).
  10. Formatting improvements (e.g. progress bar in cross-validation step).
- Removed:
  1. Redundant attributes (dataset_noNAs, dataset, df_X_train_original, df_Y_train_original, df_train_original).
  2. Redundant LT parameter in importance scoring functions. This **breaks backward compatibility**, so it may require **adapting existing pipelines** accordingly for some users.

## 1.1.2 (2025-08-25)
- Added:
  1. Version attribute.
- Changed:
  1. Fixed small typos in 2 package names listed as dependencies.
  2. Updated documentation.
  3. Use newer (compatible) versions for some dependencies.

## 1.1.1 (2025-08-19)
- Added:
  1. Automatic handling of de facto numeric columns, i.e. of object type but that can be coerced to float.
  2. Automatic handling in ALE plots of cases with many categorical levels.
  3. Automatic display of tree plot in embedded Plots pane or inline in a Jupyter notebook.
- Changed:
  1. Fixed bug in a print statement.
  2. Minor formatting improvements.
  3. Clarified some aspects in README.md, e.g. python 3.11 support.

## 1.0.0 - 1.0.1 (2025-08-11)
- Changed:
  1. Swapped alibi package by PyALE, which is fully open source. PyALE provides confidence intervals and a separate treatment for discrete features.
  2. Improved the automatic discrete feature detection mechanism in PyALE.
  3. Improved handling of bounded target variables.
  4. Multiple formatting improvements.
  5. Version 1.0.1 simply fixed an issue displaying the OS badge.

## 0.9.3 (2025-07-30)
- Added:
  1. Explicit limitations of free version.
  2. Plot-saving functionality for permutation importance scores and waterfall plot.
- Changed: Improved default naming of saved plots.

## 0.9.0 - 0.9.2 (2025-07-21)
- Changed: Made several minor improvements on PyPI page and documentation, including the one below.
- Removed: Statement of support for python 3.12 and 3.13, as some dependencies do not currently support them.
