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
