## 1.1.1 (2025-08-18)
- Added:
  1. Automatic handling of de facto numeric columns, i.e. of object type but that can be coerced to float.
  2. Automatic handling in ALE plots of cases with many categorical levels.
  3. Automatic display of tree plot in embedded Plots pane or inline in a Jupyter notebook.
- Changed:
  1. Fixed bug in a print statement.
  2. Minor formatting improvements.
  3. Clarified some aspects in README.md, e.g. python 3.11 support.

## 1.0.0 - 1.0.1 (2025-08-11)
- Changed:
  1. Swapped alibi package by PyALE, which is fully open source. PyALE provides confidence intervals and a separate treatment for discrete features.
  2. Improved handling of bounded target variables.
  3. Multiple formatting improvements.
  4. Version 1.0.1 simply fixed an issue displaying the OS badge.

## 0.9.3 (2025-07-30)
- Added:
  1. Explicit limitations of free version.
  2. Plot-saving functionality for permutation importance scores and waterfall plot.
- Changed: Improved default naming of saved plots.

## 0.9.0 - 0.9.2 (2025-07-21)
- Changed: Made several minor improvements on PyPI page and documentation, including the one below.
- Removed: Statement of support for python 3.12 and 3.13, as some dependencies do not currently support them.
