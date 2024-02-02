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
    >> Output:
         column  index  outlier_value  deviation category
    0    data      6            100        87.0  Extreme
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")

    outliers_list = []

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
            
            #recalculate the quartiles to not consider the outlier          
            filtered_values = df[column].drop(index)
            new_q1 = filtered_values.quantile(0.25)
            new_q3 = filtered_values.quantile(0.75)
            new_iqr = new_q3 - new_q1
            new_lower_bound = q1 - 1.5 * new_iqr
            new_upper_bound = q3 + 1.5 * new_iqr
            deviation = abs(outlier[column] - (new_lower_bound if outlier[column] 
                                               < new_lower_bound else new_upper_bound))
            mean_filtered = filtered_values.mean()
            std_filtered = filtered_values.std()

            sd_deviation = abs(outlier[column] - mean_filtered) / std_filtered

            if deviation <= 3 * new_iqr:
                category = 'Mild' if deviation <= 1.5 * new_iqr else 'Moderate'
            else:
                category = 'Severe' if sd_deviation < 3 else 'Extreme'

            outlier_info = {'column': column, 'index': index, 
                            'outlier_value': outlier[column], 
                            'deviation': deviation, 'category': category}

            outliers_list.append(outlier_info)

    outliers_info_df = pd.DataFrame(outliers_list)
    return outliers_info_df