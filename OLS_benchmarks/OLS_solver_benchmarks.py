import numpy as np
import time
import scipy.linalg

def benchmark_individual(X, Y, n_reps = 1000):
    times = np.zeros((n_reps, 5)) # columns: scipy lstsq, qr_solve, gram_inv, gram_solve, gram_chol
    
    for i in range(n_reps):
        # 0: scipy.linalg.lstsq
        t0 = time.perf_counter_ns()
        scipy.linalg.lstsq(X, Y)
        times[i,0] = time.perf_counter_ns() - t0  
        
        # 1: QR + solve
        t0 = time.perf_counter_ns()
        Q, R = np.linalg.qr(X, mode='reduced')
        np.linalg.solve(R, Q.T @ Y)
        times[i,1] = time.perf_counter_ns() - t0
        
        # 2: Gram + inv
        t0 = time.perf_counter_ns()
        XT = X.T
        G = XT @ X
        G_inv = np.linalg.inv(G)
        G_inv @ XT @ Y
        times[i,2] = time.perf_counter_ns() - t0
        
        # 3: Gram + solve
        t0 = time.perf_counter_ns()
        XT = X.T
        G = XT @ X
        np.linalg.solve(G, XT @ Y)
        times[i,3] = time.perf_counter_ns() - t0
        
        # 4: Gram + chol
        t0 = time.perf_counter_ns()
        XT = X.T
        G = XT @ X
        L = scipy.linalg.cholesky(G, lower=True, check_finite=False)
        z = scipy.linalg.solve_triangular(L, XT @ Y, lower=True, check_finite=False)
        scipy.linalg.solve_triangular(L.T, z, check_finite=False)
        times[i,4] = time.perf_counter_ns() - t0        
    
    # Convert to seconds
    times = times * 1e-9
    return times
  
scenarios = [
    # === A goog mix of n >= p regimes ===
    (20,      2),    
    (20,     15),
    (50,     50),
    (500,     5),    
    (500,    20),
    (1000, 1000),
    (5000,    5),    
    (5000,  100),    
    (5000,  500),    
    (50000,   5),    
    (50000, 100),    
    (50000, 500)
]

all_results = []
condition_numbers = []

for n, p in scenarios:
    print(f"Running n={n:,} p={p}")
    np.random.seed(123)
    X = np.random.randn(n, p)
    Y = np.random.randn(n)
    condition_numbers.append(np.linalg.cond(X))
    reps = 1000
    
    times = benchmark_individual(X, Y, reps)
    
    means = times.mean(axis=0)
    print(f'Mean times: {means}')
    
    rel_means = means / means[0] # relative to scipy.linalg.lstsq
    # use 2 instead of 1.96 to guard against (mild) deviations from normality
    rel_ci    = 2 * (times / means[0]).std(ddof=1, axis=0) / np.sqrt(reps)

    XT = X.T
    G = XT @ X
    beta_lstsq, *_ = scipy.linalg.lstsq(X, Y)
    G_inv = np.linalg.inv(G)
    beta_NE_inv = G_inv @ XT @ Y     
    beta_NE_solve = np.linalg.solve(G, XT @ Y)
    L = scipy.linalg.cholesky(G, lower=True, check_finite=False)
    z = scipy.linalg.solve_triangular(L, XT @ Y, lower=True, check_finite=False)
    beta_NE_chol = scipy.linalg.solve_triangular(L.T, z, check_finite=False)
        
    if np.max(np.abs(beta_lstsq - beta_NE_inv)) < 1e-9:
        print("✅ lstsq and beta_NE_inv produce the same beta estimates")   
    else:
        print(f"🚨 lstsq and beta_NE_inv do NOT produce the same beta estimates for n={n}, p={p}")
        print(f'np.max(np.abs(beta_lstsq - beta_NE_inv)) = {np.max(np.abs(beta_lstsq - beta_NE_inv))}') 
   
    if np.max(np.abs(beta_lstsq - beta_NE_solve)) < 1e-9:
        print("✅ lstsq and beta_NE_solve produce the same beta estimates")   
    else:
        print(f"🚨 lstsq and beta_NE_solve do NOT produce the same beta estimates for n={n}, p={p}")
        print(f'np.max(np.abs(beta_lstsq - beta_NE_solve)) = {np.max(np.abs(beta_lstsq - beta_NE_solve))}')

    if np.max(np.abs(beta_lstsq - beta_NE_chol)) < 1e-9:
        print("✅ lstsq and beta_NE_chol produce the same beta estimates")   
    else:
        print(f"🚨 lstsq and beta_NE_chol do NOT produce the same beta estimates for n={n}, p={p}")
        print(f'np.max(np.abs(beta_lstsq - beta_NE_chol)) = {np.max(np.abs(beta_lstsq - beta_NE_chol))}')       
    
    all_results.append({
        'n': n, 'p': p,
        'means': means,
        'rel_means': rel_means,
        'rel_lower': rel_means - rel_ci,
        'rel_upper': rel_means + rel_ci
    })  
