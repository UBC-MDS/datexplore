import pandas as pd

def detect_outliers(df):
    """
    Detect and analyze outliers in the numeric columns of a pandas DataFrame.

    This function uses the Interquartile Range (IQR) and standard deviation to identify 
    outliers in the data.
    For each numeric column, it calculates the lower and upper bounds based on the IQR.
    Values falling outside these bounds are classified as outliers.
    The function categorizes each outlier as 'Mild', 'Moderate', 'Severe', or 'Extreme'
    based on its deviation from the IQR bounds and the standard deviation from the mean. 
    It returns a DataFrame containing detailed information about
    each outlier.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame containing the data to analyze.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing detailed information about each outlier. 
        Columns include:
        - 'column': The name of the column containing the outlier.
        - 'index': The original index of the outlier in the DataFrame.
        - 'outlier_value': The value of the outlier.
        - 'deviation': The absolute deviation of the outlier from the nearest IQR bound.
        - 'category': The category of the outlier ('Mild', 'Moderate', 'Severe', or 'Extreme').

    Example Usage
    -------------
    >> df = pd.DataFrame({'data': [1, 2, 3, 4, 5, 6, 100]})
    >> outlier_info = detect_outliers(df)
    >> print(outlier_info)
    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")

    # DataFrame to store outlier information
    outliers_info = pd.DataFrame(columns=['column', 'index', 'outlier_value', 
                                          'deviation', 'category'])

    for column in df.select_dtypes(include='number').columns:
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        # Identify outliers
        outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]

        # Calculate deviation and category
        for index, outlier in outliers.iterrows():
            deviation = abs(outlier[column] - (lower_bound if outlier[column] 
                                               < lower_bound else upper_bound))
            sd_deviation = abs(outlier[column] - df[column].mean()) / df[column].std()

            if deviation <= 3 * iqr:
                category = 'Mild' if deviation <= 1.5 * iqr else 'Moderate'
            else:
                category = 'Severe' if sd_deviation < 3 else 'Extreme'

            outliers_info = outliers_info.append({'column': column, 'index': index, 
                                                  'outlier_value': outlier[column], 
                                                  'deviation': deviation, 
                                                  'category': category}, ignore_index=True)

    return outliers_info