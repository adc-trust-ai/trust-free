# Setting Up a Virtual Environment for `trust-free`

Follow these steps to create a reproducible Python environment that can download, install and run the `trust-free` package.

## 0. If needed, download and install either Python 3.11 (e.g. 3.11.13) or Python 3.12 (e.g. 3.12.10)

## 1. Create and activate a new environment
You can replace `environ` with any name you like. In your bash/terminal, run:

```bash
conda create -n environ python=3.11
conda activate environ
```
You may replace 3.11 by 3.12 above.

## 2. Install core dependencies via Conda -- but it may take a while... otherwise switch to pip (for specific pkg versions, use "==")

```bash
conda install -c conda-forge --strict-channel-priority numpy=1.26.4 "joblib>=1.5.1" "matplotlib>=3.10.5" "pandas>=2.3.2" "scikit-learn>=1.7.1" "scipy>=1.16.1" "shap>=0.48.0" "statsmodels>=0.14.5" jupyter ipykernel "ipython>=9.4.0"
```

## 3. Install additional packages via pip

Some packages (or some of their latest versions) may not be available on Conda-forge, so you need to pip-install them separately:

```bash
pip install "PyALE>=1.2.0" "pydot>=4.0.1"
```

## 4. Install trust-free itself

```bash
pip install trust-free
```

## 5. Install Graphviz (for tree visualization)

```bash
conda install -c conda-forge graphviz
```

## 6. Optional: install additional packages used in tutorial

The life satisfaction tutorial requires a few extra packages:

```bash
pip install eurostat
conda install openpyxl lxml
```

## 7. Optional: verify your installation

You can check that the correct versions are installed with:

```bash
conda list
```

which - as at August 24, 2025 - would show (among other installed dependencies):

| Package            | Version |
|------------------- |---------|
| numpy              | 1.26.4  |
| joblib             | 1.5.1   |
| matplotlib         | 3.10.5  |
| pandas             | 2.3.2   |
| scikit-learn       | 1.7.1   |
| scipy              | 1.16.1  |
| shap               | 0.48.0  |
| statsmodels        | 0.14.5  |
| jupyter            | 1.1.1   |
| ipykernel          | 6.30.1  |
| category-encoders  | 2.8.1   |
| pyale              | 1.2.0   |
| pydot              | 4.0.1   |
| trust-free         | 1.1.1   |
| graphviz           | 13.1.2  |
| eurostat           | 1.1.1   |
| openpyxl           | 3.1.5   |
| lxml               | 6.0.1   |


### Rule of thumb:

Use `conda` for packages that include compiled binaries or system dependencies (e.g., numpy, pandas, scipy, graphviz).

Use `pip` for pure Python packages or when a package is not available on conda (e.g., category-encoders, pyale, pydot, trust-free).

So, generally, the rule of thumb is: try `conda` first, then `pip` only if the package isn’t available on conda (especially on conda-forge) or you know there's a newer version not present on conda.

A few reasons:

- Binary compatibility: Conda packages often include precompiled binaries and handle system libraries, which avoids the common “DLL/symbol not found” or compilation errors that pip can trigger.

- Environment stability: Installing via pip over a conda package (or mixing versions too aggressively) can break your environment, especially for packages like numpy, pandas, scipy, or anything C/C++-based.

- Dependency resolution: Conda will automatically resolve dependencies between installed packages, which pip may not do as safely in a mixed environment.

⚠️ Warning: Avoid using `pip` to reinstall a package already installed by `conda` (e.g., numpy or pandas). This can break the environment and may require deleting and recreating it.

### Check how a package was installed:

Run `conda list` inside the environment. Packages installed via `conda` will show the conda channel in the last column (e.g., conda-forge), while `pip`-installed packages will usually show pypi or nothing in that column.


