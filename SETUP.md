# Setting Up a Virtual Environment for `trust-free`

Follow these steps to create a reproducible Python environment that can run the `trust-free` package.

### 1. Create and activate a new environment
You can replace `environ` with any name you like. In your bash/terminal, run:

```bash
conda create -n environ python=3.11
conda activate environ
```
The above should install python 3.11.13 (the latest python 3.11 version available).

2. Install core dependencies via Conda

```bash
conda install numpy=1.26.4 "joblib>=1.4.2" "matplotlib>=3.9.2" "pandas>=2.3.1" "scikit-learn>=1.7.0" "scipy>=1.16.0" "shap>=0.47.2" "statsmodels>=0.14.4" jupyter ipykernel
```

3. Install additional packages via pip

Some packages (or some of their latest versions) are not available on Conda-forge, so you need to pip-install them separately:

```bash
pip install "category-encoders>=2.8.1" "pyale>=1.2.0" "pydot>=4.0.1"
```

4. Install Graphviz (for tree visualization)

```bash
conda install -c conda-forge graphviz
```

5. Optional: verify your installation

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
| graphviz           | 13.1.2  |
