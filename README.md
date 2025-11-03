# trust-free <a href="https://adc-trust-ai.github.io/trust"><img src="assets/TRUST_logo_500x500.png" align="right" height="128" alt="TRUST logo"/></a>

[![PyPI version](https://img.shields.io/pypi/v/trust-free.svg)](https://pypi.org/project/trust-free/)
[![Downloads](https://static.pepy.tech/badge/trust-free)](https://pepy.tech/project/trust-free)
[![License](https://img.shields.io/badge/license-Proprietary-lightgrey.svg)](LICENSE.txt)
[![Python](https://img.shields.io/pypi/pyversions/trust-free.svg)](https://pypi.org/project/trust-free/)
![OS](https://img.shields.io/badge/OS-macOS%20ARM64-blue)

### Model. Explain. TRUST. All in one Python package, for free.

**trust-free** is a Python package for fitting interpretable regression models using Transparent, Robust, and Ultra-Sparse Trees (TRUST™) — a new generation of Linear Model Trees (LMTs) with state-of-the-art accuracy and intuitive explanations. It is based on my peer-reviewed paper [1], **accepted at the 22nd Pacific Rim International Conference on Artificial Intelligence (PRICAI 2025)**.

The package currently supports standard regression and experimental time-series regression tasks. Future releases will also tackle other tasks such as classification.

Note: trust-free is, as its name suggests, a free version, limited to datasets of at most 5,000 rows (instances) and 20 columns (features) — a 'pro' version is under development. 

## Overview
TRUST™ [1] is a next-generation algorithm based on (sparse) **Linear Model Trees** (LMTs), which I developed as part of my Ph.D. in Statistics at the [University of Wisconsin-Madison](https://www.wisc.edu/). **trust-free** is the official Python implementation of the algorithm.

LMTs combine the strengths of two popular interpretable machine learning models: Decision Trees (non-parametric) and Linear Models (parametric). Like a standard Decision Tree, they partition data based on simple decision rules. However, the key difference lies in how they evaluate these splits and model the data. Instead of using a simple constant (like the average) to evaluate the goodness of a split, LMTs fit a Linear Model to the data within each node.

This approach means that the final predictions in the leaves are made by a Linear Model rather than a simple constant approximation. This gives Linear Model Trees both the predictive and explicative power of a linear model, while also retaining the ability of a tree-based algorithm to handle complex, non-linear relationships in the data. This way, LMTs can approximate well any Lp function in Lp norm, i.e. can learn almost any function. Importantly, the resulting fitted model is usually compact, making it easier to interpret.

Compared to existing LMT algorithms such as M5 [2], TRUST™ offers unmatched interpretability while approaching the accuracy of black-box models like Random Forests [3] — a combination that is rare in machine learning.

### References

[1] Dorador, A. (2025). *TRUST: Transparent, Robust and Ultra-Sparse Trees*. [arXiv:2506.15791](https://arxiv.org/abs/2506.15791).

[2] Quinlan, J.R. (1992). *Learning with Continuous Classes*. Australian Joint Conference on AI, 343–348.  

[3] Breiman, L. (2001). *Random Forests*. Machine Learning, 45(1), 5–32.

### Recognition

* **Featured:**
  * [Data Elixir (Issue 546)](https://news.dataelixir.com/t/t-69C03215CCA6CFF02540EF23F30FEDED) (over 60,000 subscribers)
  * [Data Science Weekly (Issue 616)](https://datascienceweekly.substack.com/p/data-science-weekly-issue-616) (over 68,500 subscribers)
  * [University of Wisconsin - Madison Department of Statistics website](https://stat.wisc.edu/2025/05/08/department-of-statistics-celebrates-spring-2025-graduates/) (May 2025)

* **Upcoming Talks & Workshops:**
  * [PRICAI 2025](https://www.pricai.org/2025/index.php) (Nov 2025)
  * [BarcelonaTech, Statistics Department](https://eio.upc.edu/en/seminar) (Dec 2025)

* **Past Talks & Workshops:**
  * [University of Seville, Minerva AI Lab](https://grupo.us.es/minerva/) (Oct 2025) 
    

## Summary of Key Advantages

- 🧠 Combines the flexibility of trees and the power of linear models
- ⚡ Outperforms existing LMTs in accuracy, sparsity and overall interpretability
- 🔍 Full explanation of each prediction
- 🪶 Compact models that are easy to understand and visualize

## Features in Free Version

- Solves regression tasks (including a currently experimental 'time series mode')
- Interpretable models with accuracy comparable to Random Forests
- Visual tree structure and comprehensive, automatically-generated explanations on demand
- Automatically-generated head-to-head comparisons of profiles of interest
- Multiple variable importance methods (Ghost, Permutation, ALE plots, SHAP values)
- Automatic missing value handling that learns from missingness itself
- Automatic detection of potential overfitting.
- Ability to efficiently use continuous and categorical predictor variables
- Prediction confidence intervals *[coming in next release]*
  

## Additional Features in Pro Version

- No dataset size limits *[ready]*
- Large Language Model (LLM) integration for enhanced explanations *[ready]*
- Signed (+/-) variable importance plots *[ready]*
- Out-Of-Distribution detection *[ready]*
- Interaction ALE plots *[planned]*
- Automatic model mismatch detection *[planned]*
- Smart feature selection and engineering *[planned]*
- Further sparsity *[planned]*
- Faster training *[planned]*


## What's new in version 2.0.0?
### TL;DR: Next-level explanation tools, faster training and predictions, enhanced robustness, and reduced memory usage.

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

Check CHANGELOG.md to see all past release notes.

## Installation

You can install this package using pip:

```bash
pip install trust-free
```
> 📦 **Note:** The package name on PyPI is `trust-free`, but the module you import in Python is `trust`.

> ⚠️ Currently, `trust-free` includes a precompiled binary and is only tested and supported for Python 3.11 on macOS 11+ with ARM64 architecture (e.g. M1/M2/M3/M4 chips). Compatibility for other platforms (Intel macOS, Linux, Windows) is planned for future releases.

For a fully reproducible development environment with all dependencies, see SETUP.md.

## Usage

Here are two basic examples of how to use the TRUST™ algorithm:

```python
from trust import TRUST # note the import name is trust, not trust-free
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
```

### 🧪 Example 1: Sparse Synthetic Regression (n=5000, p=20)
```python
X, y, coefs = make_regression(n_samples=5000, n_features=20, n_informative=10, coef=True, noise=0.1, random_state=123)
print(coefs)
# x2 = 80.9
# x3 = 91.4
# x7 = 64.1
# x8 = 44.6
# x10 = 96.2
# x12 = 90.5
# x14 = 45.3
# x17 = 39.8
# x18 = 90.6
# x19 = 33.2

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
# Instantiate and fit your model
model = TRUST()
model.fit(X_train, y_train)
# Predict and print results
y_pred = model.predict(X_test)
print("Predictions:", y_pred[:5])
print("True y values:", y_test[:5])
print("test R\u00B2:", r2_score(y_test, y_pred))
```

```python
# Obtain (conditional) variable importance by Ghost method (based on Delicado and Pena, 2023)
model.varImp(X_test, y_test, corAnalysis=True, filename="Synthetic")
```
![varImp](https://raw.githubusercontent.com/adc-trust-ai/trust-free/main/assets/varImpScores_plot_Synthetic.png)

```python
# Unconditional variable importance by permutation (with added debiasing and uncertainty quantification steps)
model.varImpPerm(X_test, y_test, R=20, B=20, U=10, filename="Synthetic")
```
![varImpPerm](https://raw.githubusercontent.com/adc-trust-ai/trust-free/main/assets/varImpPermScores_plot_Synthetic.png)


```python
# Obtain prediction explanation for first observation
model.explain(X_test[0,:], mode="detailed", actual=y_test[0], filename="Synthetic") 
```
![Explain1](https://raw.githubusercontent.com/adc-trust-ai/trust-free/main/assets/trust-free_explain1.png)

![PieChart](https://raw.githubusercontent.com/adc-trust-ai/trust-free/main/assets/Pie_chart_Synthetic.png)


### 🩺 Example 2: Diabetes Dataset (n=442, p=10)
```python
import pandas as pd
from sklearn import datasets
from sklearn.preprocessing import LabelEncoder

Diabetes = pd.DataFrame(datasets.load_diabetes().data)
Diabetes.columns = datasets.load_diabetes().feature_names
diab_target = datasets.load_diabetes().target
Diabetes.insert(len(Diabetes.columns), "Disease_marker", diab_target)
Diabetes_X = Diabetes.iloc[:,:-1]
# Binary encoding (0/1) for 'sex'
le = LabelEncoder()
Diabetes_X.loc[:, 'sex'] = le.fit_transform(Diabetes_X['sex']).astype(str)
Diabetes_y = Diabetes.iloc[:,-1]
RLT_Diabetes = TRUST(max_depth=1)
RLT_Diabetes.fit(Diabetes_X,Diabetes_y)
y_pred_TRUST = RLT_Diabetes.predict(Diabetes_X)
```
```python
# Tree plotting requires Graphviz to be installed in your system path
# You can use e.g. Homebrew: brew install graphviz or Conda: conda install -c conda-forge graphviz
RLT_Diabetes.plot_tree("Diabetes") #will save "tree_plot_Diabetes.png" in your working directory
```
![tree](https://raw.githubusercontent.com/adc-trust-ai/trust-free/main/assets/tree_plot_Diabetes.png)

```python
# Obtain variable importance with 2 different methods: Ghost and permutation
RLT_Diabetes.varImp(Diabetes_X, Diabetes_y, corAnalysis=True, filename="Diabetes") #Ghost method
RLT_Diabetes.varImpPerm(Diabetes_X, Diabetes_y, filename="Diabetes") #Permutation method
```
![varImp2](https://raw.githubusercontent.com/adc-trust-ai/trust-free/main/assets/varImpScores_plot_Diabetes.png)

![varImp3](https://raw.githubusercontent.com/adc-trust-ai/trust-free/main/assets/varImpPermScores_plot_Diabetes.png)

```python
# Obtain prediction explanation for second observation
RLT_Diabetes.explain(Diabetes_X.iloc[1,:], aim="decrease", actual=Diabetes_y[1], filename="Diabetes")
```
![Explain2](https://raw.githubusercontent.com/adc-trust-ai/trust-free/main/assets/trust-free_explain2.png)

![Explain3](https://raw.githubusercontent.com/adc-trust-ai/trust-free/main/assets/trust-free_explain3.png)

![Explain4](https://raw.githubusercontent.com/adc-trust-ai/trust-free/main/assets/trust-free_explain4.png)

```python
# Compare the second and third observations head-to-head
RLT_Diabetes.compare(Diabetes_X.iloc[1,:], Diabetes_X.iloc[3,:], filename="Diabetes")
```
![Compare1](https://raw.githubusercontent.com/adc-trust-ai/trust-free/main/assets/trust-free_compare1.png)

![Radar](https://raw.githubusercontent.com/adc-trust-ai/trust-free/main/assets/Radar_chart_Diabetes.png)

![Pies](https://raw.githubusercontent.com/adc-trust-ai/trust-free/main/assets/Pie_charts_Diabetes.png)

![Compare2](https://raw.githubusercontent.com/adc-trust-ai/trust-free/main/assets/trust-free_compare2.png)


### More Examples on Kaggle Datasets
- [Medical Insurance Charges (1.8M views, 353K downloads)](https://www.kaggle.com/code/albertdorador/get-0-89-test-r2-with-an-interpretable-trust-tree)
- [Life Satisfaction in the EU (own contribution)](https://www.kaggle.com/code/albertdorador/interpretable-ml-on-life-satisfaction-in-the-eu)

Explore a 40-second interactive demo showcasing the explain() and compare() methods, which generate automated explanation reports for the famous Medical Insurance Charges dataset from Kaggle:

![ExplainCompareGif](https://raw.githubusercontent.com/adc-trust-ai/trust-free/main/assets/trust-free_explain_compare_wm.gif)

## License

This software is provided under a Proprietary - Permissive Binary Only license. See LICENSE.txt for details.

## More Information

For more details, documentation, and information about the full upcoming 'pro' version of the TRUST™ algorithm, please visit our official website:

https://adc-trust-ai.github.io/trust/

Further details about the TRUST™ algorithm can be found in our preprint on arXiv:

https://www.arxiv.org/abs/2506.15791

Copyright © 2025 Albert Dorador Chalar. All rights reserved. TRUST™ is a trademark of Albert Dorador Chalar.
