# datexplore

A package for exploratory data analysis and data cleaning.

## Contributors

Jordan Cairns, Sid Grover, Scout McKee

## Installation

``` bash
$ pip install datexplore
```

## Outline

Datexplore is a python package for the early stages of a data analysis project. It contains tools helpful for exploratory data analysis and data cleaning. The aim of this package is to help with some common tasks involved in these early stages of projects. The package includes tools for common EDA visualizations, data cleaning procedures, and detecting outlier numerical data.

Package functions:

-   `clean_names` : This function makes all column names in a dataframe such that the names only use letters, numbers, and underscores. The capitalization format is specified using an optional parameter.
-   `detect_outliers` : This function reports on the outliers in the numerical columns of a pandas DataFrame. It calculates the interquartile range to determine the lower and upper bounds for outlier detection. The function returns a new DataFrame with information about each outlier, including its original index, the outlier value, and the extent of its deviation.
-   `visualise` : This function generates visualizations for a pandas DataFrame to identify patterns in missing values, correlation between variables, and distribution of variables and variable pairs.

## Python Ecosystem Context

Datexplore complements well-known Python libraries like Pandas and Scikit-learn. These widely-used libraries offer a broad range of tools for handling all types of data and creating visualizations. Datexplore, on the other hand, provides specific functions tailored for aiding exploratory data analysis (EDA) and data cleaning. The focus on simplicity and ease of use differentiates it from these well-known python libraries. The functions in datexplore are intended to enhance user experience and efficiency in the EDA step of a data analysis pipeline.

The visualization function is inspired by autoviz 
(https://pypi.org/project/autoviz/0.0.6/), yet it's more customizable and fits smoothly into different data analysis workflows.

The clean_names function resembles pyjanitor’s approach 
(https://pyjanitor-devs.github.io/pyjanitor/), but we've tweaked it to be more aligned with the needs of EDA, making it straightforward to use while performing EDA.

The detect_outliers function takes an approach, similar to methods found in libraries like SciPy and Scikit-learn, but combines them in a single function. While these libraries provide comprehensive tools for statistical analysis, including outlier detection, Datexplore's outlier function allows all the data to be viewed within a single dataframe and a single function call, making the process simpler.


## Usage

Usage examples will be added next release, when the functions are fully implemented.

## Contributing

Interested in contributing? Check out the contributing guidelines in the root project directory. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`datexplore` was created by Jordan Cairns, Sid Grover, Scout McKee. It is licensed under the terms of the MIT license.

## Credits

`datexplore` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
