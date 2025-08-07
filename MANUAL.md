# Usage manual describing the TRUST class and its attributes & methods

# TRUST class
## Parameters:
- `min_samples_split: int, default=6`
  
  Stopping condition 1.
  The minimum number of samples required to split an internal node. The minimum valid number of samples in each node is 6. A lower value implies a higher training time.
  Important: if min_samples_split < 2 \* p+3, then min_samples_split is set to 2 \* p+3, where p is the number of columns in your dataset.
  This is done to avoid an artificial perfect fit that would (likely) generalize poorly.

- `max_depth: int, default=None`
  
  Stopping condition 2.
  The default of None is used to indicate that the user does not have any predetermiend preference and so cross-validation (CV) will be used to determine it.
  Otherwise the user can specify a non-negative integer (usually in the 0 to 4 range) to train a tree of said maximum depth without CV tuning

- `stoppingR2: float, default=0.95`
  
  Stopping condition 3. This is a less arbitrary criterion than the usual 'minimum impurity decrease', as it has a more intuitive scale.
  If the current training R^2 in a given node attains or exceeds the stoppingR2 threshold the node will not split further. This should speed up training and reduce overfitting.
  Lower values imply (potentially) faster training, less overfitting but more underfitting. Higher values imply (potentially) slower training, more overfitting but less underfitting.
  A value of 1 (or higher) disables this stopping condition. A value of 0 (or lower) skips training altogether (hence must not be chosen).

- `scaling: {'RobS', 'StdS', 'MinMaxS', 'none'}, default='robs'`
  
  Scaling method desired (not case-sensitive). "RobS" stands for robust scaling, which is more robust to outliers than StdS (standard scaling), but also slightly slower.
  The string (!) "none" signifies that no scaling should be performed (generally discouraged).

- `random_state: int, default=123`
  
  Ensures results are reproducible.

The above default values are sensible and hence usually enough.

## Attributes:
- `df_X_train_original: pandas dataframe of shape (n, p), default=None`
  
  Original matrix of training features X.
- `df_Y_train_original: pandas dataframe of shape (n, 1), default=None`
  
  Original array of training responses Y.
- `YLB_root: ndarray of shape (n, ), default=None`
  
  Stores the calculated response lower bound at the root of the tree.
  It's computed as a small multiple below the minimum response in training, depending on respnse standard deviation.
- `YUB_root: ndarray of shape (n, ), default=None`
  
  Stores the calculated response upper bound at the root of the tree.
  It's computed as a small multiple above the maximum response in training, depending on respnse standard deviation.
- `df_train_original: pandas dataframe of shape (n, p+1), default=None`
  
  The horizontal concatenation of df_X_train_original and df_Y_train_original.
- `dataset: ndarray of shape (n, p+1), default=None`
  
  The numpy array version of df_train_original that stores target-encoded categorical variables (if any)
- `colnamesX: ndarray of shape (p, ), default=None`
  
  Column names of the original matrix of training features X.
- `nameY: str, default=None`
  
  The name of the response variable Y.
- `stat_vals: ndarray of shape (p, ), default=None`
  
  Statistical summary values of each column (one of median, mean, mode, sd, min, or max).
- `catvar: int or list, default=None`
  
  The index(es) of the colum(s) that hold features that should be treated as categorical (will be target-encoded).
- `summary: dict, default={}`
  
  Stores node information.
- `trunc: int or float, default=0`
  
  Constant used to truncate predictions.
  A value of 0 (starting default) indicates truncation at root (i.e. global) range, which is a sensible default during tree-building.
  However, the training process includes choosing a potentially different constant for each leaf, with the option of global truncation as well.
- `num_nodes: int`
  
  Number of nodes (>= 1) in the fitted TRUST tree.
- `num_leaves: int`
  
  Number of terminal nodes (>= 1) in the fitted tree.
- `tree_depth: int`
  
  Depth of the fitted tree.
- `num_coefs_total: int`
  
  Total number of estimated coefficients in the fitted tree. This is the sum of all linear model estimated coefficients (including intercept) across leaves.
- `df_X_train_original_withID: pandas dataframe of shape (n, p+1)`
  
  Same as df_X_train_original but with a leading column included that reports the ID number of the node in which each training sample landed.
- `leaf_Y_hat_all: ndarray of shape (n, )`
  
  Predicted response value for each training sample instance.



## Methods:
- `print_model(tree=None, indent="    ", coeffs="auto", enc_table=True, rnd=2)`
  
  Prints a basic depiction of the model: a text-based tree structure if the depth of the tree is at least 1, or a table of coefficient estimates otherwise.
  ### Parameters:
  - `tree: object, default=None`
    
    The trained instance of the TRUST class for which you wish to print its model. Only internal use requires deviation from the default value.
  - `indent: str, default="    "`
    
    Amount of indentation between levels of the printed tree.
  - `coeffs: bool, default="auto"`
    
    Signals whether coefficient estimates should be printed in the tree leaves. The default, to prevent clutter, is to do so only if there are at most 2 estimates.
  - `enc_table: bool, default=True`
    
    Whether or not an encoding table for categorical variables should be printed too.
    This is useful to interpret the estimated linear model coefficients corresponding to categorical variables.
  - `rnd: int, default=2`
    
    Number of decimal places to round numbers to in the printed output.

- `fit(X, Y, catvar=None, CV="Pro", n_folds="auto", depth_list="auto", 
          seCV=0.1, seEN=0.5, trunc_list = "auto", truncGlobal="auto", 
          gamma = "auto", TS=False, NA_method="median", verboseCV=1)`

  Fits a TRUST tree.
  ### Parameters:
  - `X: array-like of shape (n, p)`
    
    Training feature samples.
  - `Y: array-like of shape (n, ) or (n, 1)`
    
    Training response values.
  - `catvar: int or list, default=None`
    
    The index(es) of the colum(s) that hold features that should be treated as categorical (will be target-encoded).
  - `CV: {'Pro', 'standard', 'none'}, default="Pro"`
    
    Cross-validation (CV) method desired to tune tree depth.
    "Pro" stands for progressive cross-validation, which means that bad candidate depths are progressively dropped, which speeds up CV (quadratically).
  - `n_folds: int, default="auto"`
    
    Number of CV folds in standard CV. The default option sets either 5 or 10 if a smaller sample size relative to dimensionality.
    The number of folds in Pro CV is always equal to the length of depth_list (see next parameter).
  - `depth_list: list, default="auto"`
    
    Maximum depths to test in CV. The default is [0,maxD], where maxD <= 4 is calculated as a function of n and p to avoid an artificial perfect fit.
    Unless the training set is very small, this default yields [0,1,2,3,4], where 0 means just a relaxed Lasso model is fitted.
  - `seCV: int or float, default=0.1`
    
    Number of standard errors away from the CV best to consider when choosing the best depth by CV.
    Larger values favor the selection of smaller depths, while smaller values (in the limit, 0) may favor the selection of larger depths (if they appear better by CV).
  - `seEN: int or float, default=0.5`
    
    Same concept as `seCV` but in this case applied to the CV performed by sklearn's `ElasticNetCV`.
    Again, larger values favor parsimony, which in this case means larger L1 ratio (closer to pure Lasso) and larger 'alpha' penalty (heavier regularization).
  - `trunc_list: int, float or list, default="auto"`
    
    List of prediction truncation constants to consider. By default a sensible list of constants is chosen, which depends on whether the (experimental) time series mode is enabled or not.
    Keeping the default "auto" value is strongly recommended.
  - `truncGlobal: bool, default="auto"`
    
    Whether or not predictions should be truncated at the root, so that they can't extrapolate and exceed observed response values during training.
    The default is to decide (at no extra compute cost!) by CV whether to truncate globally or not. It is, hence, strongly recommended to keep the default "auto" value.
  - `gamma: int or float, default="auto"`
    
    Threshold in the interval [0,1] that dictates when predictions are averaged with their respective leaf mean response, depending on a calculated F-statistic p-value.
    The default is to let this be decided by CV at no extra compute cost. Keeping this default is thus advised.
  - `TS: bool, default=False`
    
    Whether or not the time series mode should be enabled. Time series forecasting with a TRUST regressor is currently an experimental feature.
  - `NA_method: {'median', 'mean', 'mode', 'sd', 'min', 'max'}, default="median"`
    
    The desired method to impute missing values in the leaves.
    TRUST handles missing values intelligently during tree-building to exploit information in their missigness itself,
    but a numeric value is still needed in the leaves to obtain a final prediction.
  - `verboseCV: {0,1,2,3}, default=1`
    
    Level of message verbosity during training.
    0 means no messages are printed.
    1 means select informative messages are also printed, including overall training time.
    2 means fold-level training time is included too.
    3 means includes further fold-level information, especially in the case of Pro CV.

- `predict(X, tree=None, OOD_info=False, B=50, verbose=False, truncation=True)`

  Uses the trained model to output predictions.
  ### Parameters:
  - `X: array-like of shape (n, p)`
    
    Training or, more commonly testing, feature samples.
  - `tree: object, default=None`
    
    The trained instance of the TRUST class for which you wish to print its model. Only internal use requires deviation from the default value.
  - `OOD_info: bool, default=False`

    Internal parameter in free version. In pro version: whether to conduct an on-the-fly Out-Of-Distribution detection for the samples whose prediction is requested. Can be slow.
  - `B: int, default=50`

    Number of boostrap replicates used for OOD detection (pro version).
    A larger number increases assessment precision but also computation time.
  - `verbose: bool, default=False`

    Whether or not a list with the indices of instances with at least 1 missing value should be printed.
  - `truncation: bool, default=True`

    Whether or not predictions should be truncated with the chosen truncation constant.

- `explain(x_original,pred=None,actual=None,enc_table=True,plot=True,filename=None,rnd=2)`

  Provides a comprehensive explanation of the prediction of a requested instance.
  ### Parameters:
  - `x_original: array-like of shape (1, p)`

    Instance (in original form, i.e. without any encoding or scaling) for which a prediction explanation is requested.
  - `pred: int or float, default=None`

    The prediction for which you request an explanation.
    If none is povided (default) it will be computed on the fly. You may save compute time by providing it yourself.
  - `actual: int or float, default=None`

    The actual target value that corresponds to the requested instance, if known.
  - `enc_table: bool, default=True`
    
    Whether or not an encoding table for categorical variables should be printed.
    This is useful to interpret the estimated linear model coefficients corresponding to categorical variables.
  - `plot: bool, default=True`

    Whether a root-to-leaf plot should be included in the report too.
  - `filename: str, default=None`

    The file name (without any extension) that you wish to use to save the root-to-leaf and waterfall plots.
    If none is provided (default), suitable names with today's date will be used.
    Plots are always saved in the user's current working directory.
  - `rnd: int, default=2`

    Number of decimal places to round the printed results to.

- `varImpPerm(X_test,y_test,LT,R=10,B=0,U=0,plot=True,filename=None,
                        alpha=0.05,rnd=2,random_state=123)`

  Calculates the variable importance of each variable in the model using Breiman's permutation scheme, with optional debiasing and uncertainty quantification.
  ### Parameters:
  - `X_test: array-like of shape (n, p)`
    
    Test feature samples.
  - `y_test: array-like of shape (n, ) or (n, 1)`
    
    Test response values.
  - `LT: object`

    The trained instance of the TRUST class for which you wish to get variable importance scores.
  - `R: int, default=10`

    Number of times permutations are repeated.
    A larger number increases assessment precision but also computation time.
  - `B: int, default=0`

    Number of boostrap repetitions used in the debiasing step.
    The default of 0 means no debiasing is performed.
    A larger number increases assessment precision but also computation time.
  - `U: int, default=0`

    Number of boostrap repetitions used in the uncertainty quantification step.
    The default of 0 means no uncertainty quantification is performed.
    A larger number increases assessment precision but also computation time.

  - `plot: bool, default=True`

    Whether a plot, besides a table, with the feature importance scores should be included.

  - `filename: str, default=None`

    The file name (without any extension) that you wish to use to save the variable importance plot.
    If none is provided (default), suitable names with today's date will be used.
    Plots are always saved in the user's current working directory.
  - `alpha: int or float, default=0.05`

    Significance level that should be used in the uncertainty quantification step.
  - `rnd: int, default=2`

    Number of decimal places to round the printed results to.
  - `random_state: int, default=123`
  
    Ensures results are reproducible.

- `varImp(X_test,y_test,LT,corAnalysis=False,plot=True,ALE_plot="auto",
             filename=None,rnd=2,random_state=123)`

  Calculates the variable importance of each variable in the model using the Ghost variable method (Delicado and Pena, 2023).
  This method, unlike Breiman's permutation scheme, accounts for feature correlation, and tends to be faster.
  It does not need a debiasing or uncertainty quantification step, because by construction it is unbiased and reported scores are statistically significant.
  ### Parameters:
  - `X_test: array-like of shape (n, p)`
    
    Test feature samples.
  - `y_test: array-like of shape (n, ) or (n, 1)`
    
    Test response values.
  - `LT: object`

    The trained instance of the TRUST class for which you wish to get variable importance scores.
  - `corAnalysis: bool, default=True`

    Whether a complementary correlation analysis should be included.

  - `plot: bool, default=True`

    Whether a plot, besides a table, with the feature importance scores should be included.

  - `ALE_plot: list, default="auto"`
    List containing the feature indices for which an Accumulated Local Effects (ALE) plot is requested.
    By default all features in the dataset are included, unless there are 25 or more, in which case only the most important 24 are included.
    Plots are arranged in a grid of at most 4 columns.  

  - `filename: str, default=None`

    The file name (without any extension) that you wish to use to save the variable importance and ALE plots.
    If none is provided (default), suitable names with today's date will be used.
    Plots are always saved in the user's current working directory.
  - `alpha: int or float, default=0.05`

    Significance level that should be used in the uncertainty quantification step.
  - `rnd: int, default=2`

    Number of decimal places to round the printed results to.
  - `random_state: int, default=123`
  
    Ensures results are reproducible.

- `varImpMarg(X_train,Y_train, plot=True, rnd=2)`

  Calculates the variable importance of each variable in the model based on correlation.
  If tree depth is 0, a measure of linear correlation is used (Pearson), while a non-linear one - though still monotonic -  is used otherwise (Kendall).
  ### Parameters:
  - `X_train: array-like of shape (n, p)`
    
    Training feature samples.
  - `Y_train: array-like of shape (n, ) or (n, 1)`

    Training response values.
  - `plot: bool, default=True`

    Whether a plot, besides a table, with the feature importance scores (correlations) should be included.

  - `rnd: int, default=2`

    Number of decimal places to round the printed results to.

- `plot_tree(filename=None, indiv=False)`

  Plots the fitted tree. If tree depth is 0, the user is prompted to use the print_model method instead.
    ### Parameters:
  - `filename: str, default=None`

    The file name (without any extension) that you wish to use to save the tree plot.
    If none is provided (default), suitable names with today's date will be used.
    Plots are always saved in the user's current working directory.
  - `indiv: bool, default=False`

    Whether a tree plot for an individual observation (root-to-leaf path) should be displayed.
    Only for internal use.
