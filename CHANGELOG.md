## 2.0.0 (2025-10-??)
- Added:
  1. **New compare() method** to allow head-to-head prediction comparisons.
  2. Automatic reporting and removal of duplicate columns.
  3. Fallback to (TRUST-flavored) standard Lasso in leaf if all Relaxed Lasso coefficients are zero due to excessive penalty.
  4. Automatic check for missing target values and corresponding removal of rows in training dataset.
  5. Method show_leaf_coefficients(leaves = "all", rnd = 2) to print coefficient summary tables for the selected leaves.
  6. Explicit node id, also in tree plot (leaves only).
- Changed:
  1. **Revamped explain() method** to be even more powerful *and* user friendly.
  2. Fixed bug in print_model() in absence of significant features.
  3. Threshold for 'large' lowered from 0.6 to 0.55, and threshold for 'intermediate' increased from 0.4 to 0.45.
  4. More efficient retrieval of encoded values: before it was O(n) now it's O(1). Should speedup prediction (and even fitting) noticeably.
  5. Internal method _fill_NAs now takes the feature matrix X instead of the complete dataset as input.
  6. df_X_train_original_withID for the all-complete df_Leaf_X_train_original_Y_Yhat.
  7. Faster variable importance calculation (both permutation and Ghost method).
  8. Slightly faster prediction for depth-0 trees.
  9. Formatting improvements (e.g. progress bar in cross-validation step).
- Removed:
  1. Redundant attributes (dataset_noNAs, dataset, df_X_train_original, df_Y_train_original, df_train_original).
  2. Redundant LT parameter in importance scoring functions.

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
