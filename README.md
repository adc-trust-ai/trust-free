# trust-free <a href="https://adc-trust-ai.github.io/trust"><img src="assets/TRUST_logo_500x500.png" align="right" height="128" alt="TRUST logo"/></a>

[![PyPI version](https://img.shields.io/pypi/v/trust-free.svg)](https://pypi.org/project/trust-free/)
[![Downloads](https://static.pepy.tech/badge/trust-free)](https://pepy.tech/project/trust-free)
[![License](https://img.shields.io/badge/license-Proprietary-lightgrey.svg)](LICENSE.txt)
[![Python](https://img.shields.io/pypi/pyversions/trust-free.svg)](https://pypi.org/project/trust-free/)
![OS](https://img.shields.io/badge/OS-macOS%20ARM64-blue)

> ⚠️ **Note:** Currently, `trust-free` is only tested and supported on macOS ARM64 (e.g. M1/M2/M3/M4 chips). Compatibility for other platforms (Intel macOS, Linux, Windows) is planned for future releases.

**trust-free** is a Python package for fitting interpretable regression models using Transparent, Robust, and Ultra-Sparse Trees (TRUST) — a new generation of Linear Model Trees (LMTs) with state-of-the-art accuracy and intuitive explanations. This is a free version — a pro version is planned in the future.

## Overview
TRUST [1] is a new-generation algorithm based on (sparse) **Linear Model Trees** (LMT). It was developed during my Ph.D. in Statistics at the University of Wisconsin-Madison, a department founded by the celebrated statistician George Box ("all models are wrong but some are useful").

LMT combine the strengths of two popular interpretable machine learning models: Decision Trees (non-parametric) and Linear Models (parametric). Like a standard Decision Tree, they partition data based on simple decision rules. However, the key difference lies in how they evaluate these splits and model the data. Instead of using a simple constant (like the average) to evaluate the goodness of a split, LMT fit a Linear Model to the data within each node.

This approach means that the final predictions in the leaves are made by a Linear Model rather than a simple constant approximation. This gives Linear Model Trees both the predictive and explicative power of a linear model, while also retaining the ability of a tree-based algorithm to handle complex, non-linear relationships in the data. This way, LMT can approximate well any Lp function in Lp norm, i.e. can learn almost any function. Importantly, the resulting fitted model is usually compact and hence easier to interpret.

Compared to other LMT algorithms, such as M5 [2], the TRUST algorithm delivers a new level of interpretability through enhanced sparsity and a host of specialized methods. To the best of our knowledge, it is also the most accurate LMT algorithm currently available. These two aspects — its advanced interpretability and state-of-the-art accuracy — establish TRUST as the leading LMT algorithm today, having an overall accuracy comparable to the well-known blackbox model Random Forest [3] — while remaining fully interpretable.

[1] Dorador, A. (2025). "TRUST: Transparent, Robust and Ultra-Sparse Trees". [Link to arXiv preprint](https://arxiv.org/abs/2506.15791).

[2] Quinlan, J.R. (1992). "Learning with Continuous Classes". Proceedings of Australian Joint Conference on Artificial Intelligence, Hobart 16-18 November 1992, 343-348.

[3] Breiman, L. (2001). "Random Forests". Machine Learning, 45, 5-32.

Currently designed only for regression tasks. Future releases will also tackle other tasks e.g. classification.

The free version is slower and is limited to datasets of at most 5,000 rows and 20 columns. It does not include premium functionality like:
- Large Language Model (LLM) integration for enhanced explanations
- Signed (+/-) variable importance plots
- Interaction ALE plots
- Prediction confidence intervals
- Out-Of-Distribution detection

## Installation

You can install this package using pip:

```bash
pip install trust-free
```

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
