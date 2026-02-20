# trust-free <a href="https://adc-trust-ai.github.io/trust"><img src="assets/TRUST_logo_500x500.png" align="right" height="128" alt="TRUST logo"/></a>

[![PyPI version](https://img.shields.io/pypi/v/trust-free.svg)](https://pypi.org/project/trust-free/)
[![Python](https://img.shields.io/pypi/pyversions/trust-free.svg)](https://pypi.org/project/trust-free/)
[![Downloads](https://static.pepy.tech/badge/trust-free)](https://pepy.tech/project/trust-free)
[![License](https://img.shields.io/badge/license-Proprietary-lightgrey.svg)](LICENSE.txt)
[![User Manual](https://img.shields.io/badge/docs-User_Manual-blue)](https://github.com/adc-trust-ai/trust-free/blob/main/MANUAL.md)
![OS](https://img.shields.io/badge/OS-Windows%20-blue)
![OS](https://img.shields.io/badge/OS-macOS%20-blue)
![OS](https://img.shields.io/badge/OS-Linux%20-blue)
![Kaggle Compatible](https://img.shields.io/badge/Kaggle-Compatible-blue?logo=kaggle&logoColor=white)
![Colab Compatible](https://img.shields.io/badge/Google%20Colab-Compatible-blue?logo=googlecolab&logoColor=white)

### Model. Explain. TRUST. All in one package.

**trust-free** is a Python package for fitting interpretable regression models using Transparent, Robust, and Ultra-Sparse Trees (TRUST™) — a new generation of Linear Model Trees (LMTs) with Random-Forest accuracy and intuitive explanations. It is based on my peer-reviewed paper [1], **presented at the 22nd Pacific Rim International Conference on Artificial Intelligence (PRICAI 2025) and to appear in Springer Nature (Lecture Notes in Artificial Intelligence)**.

It includes a **state-of-the-art explainability suite**, providing comprehensive, automatically-generated explanation reports. To see it in action, here's a 30-second demo showcasing the explain() and compare() methods applied to the famous [Medical Insurance Charges](https://www.kaggle.com/datasets/mirichoi0218/insurance) dataset from Kaggle:

<img src="https://raw.githubusercontent.com/adc-trust-ai/trust-free/main/assets/trust-free_explain_compare_wm.gif" alt="ExplainCompareGif" width="100%" style="display: block; margin: auto;" />

### Proven Performance: Accuracy + Full Interpretability (60 Datasets)

| Model                   | **Test R² ↑** | **Interpretable?** |
|-------------------------|---------------|--------------------|
| **TRUST™**              | **0.67**      | ✅ Yes             |
| Random Forest (RF)      | 0.62          | ❌ No              |
| Lasso                   | 0.57          | ✅ Yes             |
| CART                    | 0.49          | ✅ Yes             |
| Node Harvest (NH)       | 0.47          | ✅ Yes             |
| M5' (Linear Model Tree) | 0.36          | ⚠️ Partially       |

> In the table above, **TRUST™ is the only fully interpretable model statistically above 0.6 test R²** across varied benchmark datasets — and **6× sparser** than M5' (*17 vs 109 coefficients* on average).  
> *Source: PRICAI 2025 (Springer LNAI)*

Try it now: `pip install trust-free`. In **Google Colab**: `%pip install trust-free`.
See full benchmarks in the [PRICAI 2025 paper](https://arxiv.org/abs/2506.15791)

---

The package currently supports standard regression and experimental time-series regression tasks. Future releases will also tackle other tasks such as classification.

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

* **Past Talks & Workshops:**
  * [BarcelonaTech, Statistics Department](https://eio.upc.edu/en/seminar) (Dec 2025)
  * [PRICAI 2025](https://www.pricai.org/2025/index.php) (Nov 2025) 
  * [University of Seville, Minerva AI Lab](https://grupo.us.es/minerva/) (Oct 2025) 
    

## Key Advantages: RF Accuracy ⟡ Tree Transparency ⟡ Linear Interpretability

- **Hybrid power**: Trees to capture non-linearity & interactions + sparse linear (Adaptive or Relaxed Elastic Net) models in leaves
- **Superior accuracy**: RF-level accuracy, proven on 60 benchmark datasets
- **Full transparency**: Every prediction is auditable via tree path + leaf equation
- **Inclusive**: Explanation reports written in natural language accessible to all audiences
- **Compliant by design**: 100% Compliant with the EU AI Act and the OECD AI Principles — ideal for high-stakes domains like finance and healthcare

### About this edition
- ℹ️ Free-tier Dataset Limits: ≤ 5,000 rows and ≤ 20 columns (intended for proof-of-concept, R&D and teaching)
- ✅ Full Functionality: All core features are fully functional within these bounds
- ✅ Standalone Tools: Relaxed Net (Renet™), Adaptive Net, TurboSolve (fastest OLS/ridge solver), Direct & Systemic Feature Importance
- ⭐ No-Limit Utilities: TurboSolve, Feature Importance methods, and our open-source Synthetic Dataset Generators (Toeplitz, Block-Correlated) can be used **without restriction** as standalone tools
- 🚀 Ready to Level Up? Unlimited scale and [additional features](https://github.com/adc-trust-ai/trust-free/blob/main/trust-pro.md) in the forthcoming **trust-pro** edition

**Want early access to trust-pro?**  
- Join the [waitlist](https://forms.gle/Gsti4kZ7yG5ZTNqu7) (completely anonymous & GDPR-compliant)
- Star ⭐ this repo to stay updated!

### Features in this edition

- Solves regression tasks (including a currently experimental 'time series mode')
- Interpretable models with accuracy comparable to Random Forests
- Visual tree structure and comprehensive, automatically-generated explanations on demand
- Automatically-generated head-to-head comparisons of profiles of interest
- Multiple variable importance methods (SOTA Permutation, Ghost Variables, ALE plots, SHAP values)
- Automatic missing value handling that learns from missingness itself
- Automatic detection of potential overfitting.
- Ability to efficiently use continuous and categorical predictor variables
- Prediction confidence intervals *[coming in next release]*
- Novel method to warn about risky predictions on the fly *[coming in next release]*
- Even faster training *[coming in next release]*


## What's new in version 3.0.0?
### TL;DR: 5-20x faster training, new models in leaves (Adaptive or Relaxed Elastic Net), new Direct and Systemic Feature Importance, and more!

## 3.0.0 (2026-02-20)
- Added:
  1. **New models in leaves:** Renet (SOTA Relaxed Elastic Net) and a custom implementation of Adaptive Elastic Net, offering slightly different accuracy-sparsity profiles
  2. **New Direct and Systemic Variable Importance** estimation: an upgrade to the traditional permutation feature importance
  3. **New Minimum Description Length** mode for leaves: simplest plausible leaf model when Renet gives OLS estimates.
  4. **New open-source datasets module**: make regression datasets with different correlation structures (plain, block, or Toeplitz)
  5. More public classes and methods (can be used as **standalone tools**): Renet, AdaptiveNetCV, FeatureImportance, turbosolve, and the datasets module.
  6. Optional display of leaf model equation in tree plot
- Changed:
  1. Much **faster training** (5-20x)
  2. Small enhancements to explain() and Ghost Variable Importance estimation
  3. __init__ and fit method signatures changed to accomodate new capabilities and to align closer with scikit-learn conventions. This **breaks backward compatibility**, so it may require adapting existing pipelines accordingly for some users.
  4. Renamed the TRUST class as TRUSTRegressor (TRUSTClassifier is coming soon...). The TRUST class will still be around until version 4.0.0 to help transition.
  5. Minor bug fixes
- Removed:
  1. Traditional Permutation Feature Importance option (superseded by faster, more robust and 100% deterministic alternative, see second "Added" item)

Check CHANGELOG.md to see all past release notes.

Coming up in the next release: **TurboSolve**, a smart OLS solver that is always at least as fast as your favorite OLS solver but usually 2x to 10x faster.
TurboSolve will serve as the high-performance engine for the TRUST algorithm in `trust-free`. Additionally, it will be available as a *standalone, free utility* for OLS problems of any scale, without any constraints on dataset size.
### 🚀 Performance Benchmarks: TurboSolve vs. Scikit-Learn

The following benchmarks compare **TurboSolve** against `sklearn.linear_model.LinearRegression`. 
Tests were conducted across 100 repetitions with a range of dataset geometries. 

<div align="center">
<img src="https://raw.githubusercontent.com/adc-trust-ai/trust-free/main/assets/TurboSolve_benchmarks.png" alt="TurboSolve_vs_Sklearn" width="90%" style="display: block; margin: auto;" />
</div>

**TurboSolve** is designed for efficiency across all data geometries. As shown above, the performance gap widens significantly as dataset size increases, reaching nearly 10x faster execution than standard implementations for large-scale problems.

| Scenario ($n \times p$) | TurboSolve (ms) | Sklearn (ms) | Speedup | Mean Rel. Error (%) | Global Max Error (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tall & Lean** ($5k \times 20$) | 0.54 ± 0.20 | 1.54 ± 0.08 | **2.85x** | $2.41 \times 10^{-12}$ | $4.45 \times 10^{-11}$ |
| **Underdetermined** ($50 \times 200$)* | 0.20 ± 0.02 | 0.76 ± 0.06 | **3.80x** | $3.43 \times 10^{-4}$ | $0.0129$ |
| **Big Data** ($100k \times 100$) | 27.86 ± 1.24 | 273.96 ± 2.68 | **9.83x** | $9.54 \times 10^{-13}$ | $2.04 \times 10^{-11}$ |

*\*Note: In the n << p case, **TurboSolve** utilizes a data-driven micro-ridge penalty to maintain stability and speed, accounting for the slight increase in relative error.*

## Installation

You can install this package using pip:

```bash
pip install trust-free
```
> 📦 **Note:** The package name on PyPI is `trust-free`, but the module you import in Python is `trust`: `from trust import TRUST`.

### Platform Compatibility

| Platform / Environment   | OS & Arch         | Python    | Status      |
|--------------------------|-------------------|-----------|-------------|
| **macOS ARM64** (M1–M4)  | macOS 11+ ARM64   | 3.11–3.12 | ✅ Working  |
| **macOS Intel** (x86_64) | macOS 11+ Intel   | 3.11–3.12 | ✅ Working  |
| **Linux Intel/AMD**      | manylinux x86_64  | 3.11–3.12 | ✅ Working  |
| **Google Colab**         | Linux x86_64      | 3.12      | ✅ Working  |
| **Kaggle Notebooks**     | Linux x86_64      | 3.11      | ✅ Working* |
| **Linux ARM64**          | manylinux ARM64   | 3.11–3.12 | ✅ Working  |
| **Windows Intel/AMD**    | Windows 11 x86_64 | 3.11–3.12 | ✅ Working  |

*If Kaggle shows a dependency-compatibility issue message upon installation via %pip install trust-free you may safely ignore it and hit "Restart and run up to selected cell" (assuming your selected cell is the one installing trust-free).

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
# Unconditional variable importance by permutation (with added debiasing and uncertainty quantification steps)
model.varImpPerm(X_test, y_test, R=20, B=20, U=10, filename="Synthetic")
```
<div align="center">
<img src="https://raw.githubusercontent.com/adc-trust-ai/trust-free/main/assets/Direct_Importance_plot_Synthetic.png" alt="varImp" width="50%" style="display: block; margin: auto;" />
</div>

```python
# Obtain prediction explanation for first observation
model.explain(X_test[0,:], mode="detailed", actual=y_test[0], filename="Synthetic") 
```
<div align="center">
<img src="https://raw.githubusercontent.com/adc-trust-ai/trust-free/main/assets/trust-free_explain1.png" alt="Explain1" width="97%" style="display: block; margin: auto;" />

<img src="https://raw.githubusercontent.com/adc-trust-ai/trust-free/main/assets/Pie_chart_Synthetic.png" alt="PieChart" width="50%" style="display: block; margin: auto;" />
</div>

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
<div align="center">
<img src="https://raw.githubusercontent.com/adc-trust-ai/trust-free/main/assets/tree_plot_Diabetes.png" alt="tree" width="50%" style="display: block; margin: auto;" />
</div>

```python
# Obtain direct and systemic variable importance along with impact propagation heatmap
RLT_Diabetes.varImp(Diabetes_X, Diabetes_y, corAnalysis=True, filename="Diabetes") #Ghost method
RLT_Diabetes.varImpPerm(Diabetes_X, Diabetes_y, filename="Diabetes") #Permutation method
```
<div align="center">
    <img src="https://raw.githubusercontent.com/adc-trust-ai/trust-free/main/assets/Direct_Importance_plot_Diabetes.png" alt="varImp2" width="33.5%" />
    <img src="https://raw.githubusercontent.com/adc-trust-ai/trust-free/main/assets/Systemic_Importance_plot_Diabetes.png" alt="varImp3" width="33.5%" />
     <img src="https://raw.githubusercontent.com/adc-trust-ai/trust-free/main/assets/Impact_Propagation_Heatmap_Diabetes.png" alt="varImp3b" width="31%" />
</div>


```python
# Obtain prediction explanation for second observation
RLT_Diabetes.explain(Diabetes_X.iloc[1,:], aim="decrease", actual=Diabetes_y[1], filename="Diabetes")
```
<div align="center">
<img src="https://raw.githubusercontent.com/adc-trust-ai/trust-free/main/assets/trust-free_explain2.png" alt="Explain2" width="97%" style="display: block; margin: auto;" />

<img src="https://raw.githubusercontent.com/adc-trust-ai/trust-free/main/assets/trust-free_explain3.png" alt="Explain3" width="97%" style="display: block; margin: auto;" />

<img src="https://raw.githubusercontent.com/adc-trust-ai/trust-free/main/assets/trust-free_explain4.png" alt="Explain4" width="97%" style="display: block; margin: auto;" />
</div>

```python
# Compare the second and fourth observations head-to-head
RLT_Diabetes.compare(Diabetes_X.iloc[1,:], Diabetes_X.iloc[3,:], filename="Diabetes")
```
<div align="center">
<img src="https://raw.githubusercontent.com/adc-trust-ai/trust-free/main/assets/trust-free_compare1.png" alt="Compare1" width="97%" style="display: block; margin: auto;" />

<img src="https://raw.githubusercontent.com/adc-trust-ai/trust-free/main/assets/Radar_chart_Diabetes.png" alt="Radar" width="50%" style="display: block; margin: auto;" />

<img src="https://raw.githubusercontent.com/adc-trust-ai/trust-free/main/assets/trust-free_compare2.png" alt="Compare2" width="97%" style="display: block; margin: auto;" />

<img src="https://raw.githubusercontent.com/adc-trust-ai/trust-free/main/assets/Pie_charts_Diabetes.png" alt="Pies" width="97%" style="display: block; margin: auto;" />
</div>

### More Examples on Kaggle Datasets
- [Medical Insurance Charges (1.82M views, 360K downloads)](https://www.kaggle.com/datasets/mirichoi0218/insurance)
- [Life Satisfaction in the EU (own contribution)](https://www.kaggle.com/datasets/albertdorador/eu-life-satisfaction-eurostat-un-oecd)


## License

This software is provided under a Proprietary - Permissive Binary Only license. See LICENSE.txt for details.

## More Information

For more details, documentation, and information about the full upcoming 'pro' version of the TRUST™ algorithm, please visit our official website:

https://adc-trust-ai.github.io/trust/

Further details about the TRUST™ algorithm can be found in our preprint on arXiv:

https://www.arxiv.org/abs/2506.15791

Copyright © 2025 Albert Dorador Chalar. All rights reserved. TRUST™ is a trademark of Albert Dorador Chalar.
