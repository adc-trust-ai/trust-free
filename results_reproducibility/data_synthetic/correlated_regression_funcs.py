import numpy as np
from scipy.linalg import toeplitz

def make_correlated_regression(n_samples, n_features, n_informative, noise=1.0, rho=0.5, random_state=123):
    rng = np.random.default_rng(random_state)

    # Step 1: Construct correlated covariance matrix
    # rho is the pairwise correlation between features
    Sigma = rho * np.ones((n_features, n_features)) + (1 - rho) * np.eye(n_features)

    # Step 2: Generate correlated features
    X = rng.multivariate_normal(mean=np.zeros(n_features), cov=Sigma, size=n_samples)

    # Step 3: Generate sparse coefficients
    coefs = np.zeros(n_features)
    coefs[:n_informative] = rng.normal(size=n_informative)

    # Step 4: Generate response
    y = X @ coefs + rng.normal(scale=noise, size=n_samples)

    return X, y, coefs


def make_block_correlated_regression(n_samples, n_features, n_informative, noise=1.0, rho=0.5, random_state=123):
    rng = np.random.default_rng(random_state)
    k = n_informative
    m = n_features - n_informative
    # --- covariance blocks ---
    # informative block
    Sigma_inf = (1 - rho) * np.eye(k) + rho * np.ones((k, k))
    Sigma_noise = (1 - rho/2) * np.eye(m) + (rho/2) * np.ones((m, m)) if m > 0 else np.empty((0,0))
    Sigma = np.block([
        [Sigma_inf, np.zeros((k, m))],
        [np.zeros((m, k)), Sigma_noise]
    ]) if m > 0 else Sigma_inf

    # generate X
    X = rng.multivariate_normal(mean=np.zeros(n_features), cov=Sigma, size=n_samples)

    # sparse coefficients
    coefs = np.zeros(n_features)
    coefs[:n_informative] = rng.normal(0, 1, size=n_informative)

    # generate y
    y = X @ coefs + rng.normal(scale=noise, size=n_samples)

    return X, y, coefs
  
  
def make_toeplitz_regression(n_samples, n_features, n_informative, noise=1.0, rho=0.5, random_state=123):
    """
    Generates regression data where features have a Toeplitz correlation structure.
    Corr(X_i, X_j) = rho^|i - j|
    """
    rng = np.random.default_rng(random_state)
    
    # Step 1: Construct Toeplitz covariance matrix
    # The first row/column is [1, rho, rho^2, ..., rho^p-1]
    first_row = rho ** np.arange(n_features)
    Sigma = toeplitz(first_row)

    # Step 2: Generate correlated features
    X = rng.multivariate_normal(mean=np.zeros(n_features), cov=Sigma, size=n_samples)

    # Step 3: Generate sparse coefficients
    # We assign signal to the first k features (which are highly correlated with each other)
    coefs = np.zeros(n_features)
    coefs[:n_informative] = rng.normal(size=n_informative)

    # Step 4: Generate response
    y = X @ coefs + rng.normal(scale=noise, size=n_samples)

    return X, y, coefs  

# Example usage
S1_X, S1_y, S1_coefs = make_correlated_regression(n_samples=100000, n_features=20, n_informative=10, rho=0.0, noise=1.0)
S4_X, S4_y, S4_coefs = make_toeplitz_regression(n_samples=1000, n_features=100, n_informative=10, rho=0.75, noise=2.0)
S10_X, S10_y, S10_coefs = make_block_correlated_regression(n_samples=300, n_features=3000, n_informative=30, rho=0.75, noise=2.0)
