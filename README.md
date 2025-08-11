# trust-free <a href="https://adc-trust-ai.github.io/trust"><img src="assets/TRUST_logo_500x500.png" align="right" height="128" alt="TRUST logo"/></a>

[![PyPI version](https://img.shields.io/pypi/v/trust-free.svg)](https://pypi.org/project/trust-free/)
[![Downloads](https://static.pepy.tech/badge/trust-free)](https://pepy.tech/project/trust-free)
[![License](https://img.shields.io/badge/license-Proprietary-lightgrey.svg)](LICENSE.txt)
[![Python](https://img.shields.io/pypi/pyversions/trust-free.svg)](https://pypi.org/project/trust-free/)
![OS](https://img.shields.io/badge/OS-macOS%20ARM64-blue)


**trust-free** is a Python package for fitting interpretable regression models using Transparent, Robust, and Ultra-Sparse Trees (TRUST) — a new generation of Linear Model Trees (LMTs) with state-of-the-art accuracy and intuitive explanations. Currently supports standard regression and experimental time-series regression tasks. Future releases will also tackle other tasks such as classification. This is a free version, limited to datasets of at most 5,000 rows and 20 columns — a pro version is under development. 

## Overview
TRUST [1] is a next-generation algorithm based on (sparse) **Linear Model Trees** (LMTs), which I developed as part of my Ph.D. in Statistics at the University of Wisconsin-Madison.

LMTs combine the strengths of two popular interpretable machine learning models: Decision Trees (non-parametric) and Linear Models (parametric). Like a standard Decision Tree, they partition data based on simple decision rules. However, the key difference lies in how they evaluate these splits and model the data. Instead of using a simple constant (like the average) to evaluate the goodness of a split, LMTs fit a Linear Model to the data within each node.

This approach means that the final predictions in the leaves are made by a Linear Model rather than a simple constant approximation. This gives Linear Model Trees both the predictive and explicative power of a linear model, while also retaining the ability of a tree-based algorithm to handle complex, non-linear relationships in the data. This way, LMTs can approximate well any Lp function in Lp norm, i.e. can learn almost any function. Importantly, the resulting fitted model is usually compact, making it easier to interpret.

Compared to existing LMT algorithms such as M5 [2], TRUST offers unmatched interpretability and accuracy, approaching that of black-box models like Random Forests [3] — while remaining fully transparent.

### References

[1] Dorador, A. (2025). *TRUST: Transparent, Robust and Ultra-Sparse Trees*. [arXiv:2506.15791](https://arxiv.org/abs/2506.15791).

[2] Quinlan, J.R. (1992). *Learning with Continuous Classes*. Australian Joint Conference on AI, 343–348.  

[3] Breiman, L. (2001). *Random Forests*. Machine Learning, 45(1), 5–32.


## Summary of Key Advantages

- 🧠 Combines the flexibility of trees and the power of linear models
- ⚡ Outperforms existing LMTs in accuracy, sparsity and overall interpretability
- 🔍 Full explanation of each prediction
- 🪶 Compact models that are easy to understand and visualize

## Features in Free Version

- Solves regression tasks (including a currently experimental 'time series mode')
- Interpretable models with accuracy comparable to Random Forests
- Visual tree structure and comprehensive, automatically-generated explanations on demand
- Multiple variable importance methods (Ghost, Permutation, ALE plots, SHAP values)
- Automatic missing value handling that learns from missingness itself
- Ability to efficiently use continuous and categorical predictor variables
  

## Additional Features in Pro Version

- Large Language Model (LLM) integration for enhanced explanations *[ready]*
- Signed (+/-) variable importance plots *[ready]*
- Out-Of-Distribution detection *[ready]*
- Interaction ALE plots *[planned]*
- Prediction confidence intervals *[planned]*
- Further sparsity *[planned]*
- Faster training *[planned]*


## What's new in version 1.0.0

1. Swapped alibi package by PyALE, which is fully open source. PyALE provides confidence intervals and a separate treatment for discrete features.
2. Improved handling of bounded target variables.
3. Multiple formatting improvements.

Check CHANGELOG.md to see all past release notes.

## Installation

You can install this package using pip:

```bash
pip install trust-free
```
> 📦 **Note:** The package name on PyPI is `trust-free`, but the module you import in Python is `trust`.

> ⚠️ Currently, `trust-free` includes a precompiled binary and is only tested and supported on macOS 11+ on ARM64 (e.g. M1/M2/M3/M4 chips). Compatibility for other platforms (Intel macOS, Linux, Windows) is planned for future releases.

## Usage

Here are two basic examples of how to use the TRUST algorithm:

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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
# Instantiate and fit your model
model = TRUST()
model.fit(X_train, y_train)
# Predict and print results
y_pred = model.predict(X_test)
print("Predictions:", y_pred[:5])
print("True y values:", y_test[:5])
print("test R\u00B2:", r2_score(y_test, y_pred))
# Obtain prediction explanation for first observation
model.explain(X_test[0,:], y_pred[0], actual=y_test[0]) 
# Obtain (conditional) variable importance by Ghost method (Delicado and Pena, 2023)
model.varImp(X_test, y_test, model, corAnalysis=True)
```

### 🩺 Example 2: Diabetes Dataset (n=442, p=10)
```python
import pandas as pd
from sklearn import datasets

Diabetes = pd.DataFrame(datasets.load_diabetes().data)
Diabetes.columns = datasets.load_diabetes().feature_names
diab_target = datasets.load_diabetes().target
Diabetes.insert(len(Diabetes.columns), "Disease_marker", diab_target)
Diabetes_X = Diabetes.iloc[:,:-1]
Diabetes_y = Diabetes.iloc[:,-1]
RLT_Diabetes = TRUST(max_depth=1)
RLT_Diabetes.fit(Diabetes_X,Diabetes_y)
y_pred_TRUST = RLT_Diabetes.predict(Diabetes_X)
# Tree plotting requires Graphviz to be installed in your system path
# You can use e.g. Homebrew: brew install graphviz or Conda: conda install -c conda-forge graphviz
RLT_Diabetes.plot_tree("Diabetes") #will save "tree_plot_Diabetes.png" in your working directory
# Obtain prediction explanation for first observation
RLT_Diabetes.explain(Diabetes_X.iloc[0,:], y_pred_TRUST[0], actual=Diabetes_y.to_list()[0])
# Obtain variable importance with 2 different methods: Ghost and permutation
RLT_Diabetes.varImp(Diabetes_X, Diabetes_y, RLT_Diabetes, corAnalysis=True) #Ghost method
RLT_Diabetes.varImpPerm(Diabetes_X, Diabetes_y, RLT_Diabetes) #Permutation method
```

## License

This software is provided under a Proprietary - Permissive Binary Only license. See `LICENSE.txt` for details.

## More Information

For more details, documentation, and information about the full upcoming pro (paid) version of the TRUST algorithm, please visit our official website:

https://adc-trust-ai.github.io/trust/

Further details can be found in our preprint on arxiv:

https://www.arxiv.org/abs/2506.15791
