def detect_outliers(df):
    """
    Detect and analyze outliers in the numeric columns of a pandas DataFrame.

    This function utilizes the Interquartile Range (IQR) to identify outliers in the data. It calculates the lower and upper bounds to determine which values 
    fall outside this range, thus classifying them as outliers. The function returns a DataFrame that contains detailed information about each outlier, 
    including its original index, the value, and the extent of its deviation from the nearest bound.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame containing the data.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing detailed information about each outlier, including indices, outlier values, and their deviation extents.

    Notes
    -----
    - The function considers values lying outside 1.5 times the IQR (below Q1 and above Q3) as outliers.
    - This approach is suitable for a preliminary analysis in the EDA stage, providing insights into potential data anomalies.

    Example Usage
    -------------
    >> df = pd.DataFrame({'data': [1, 2, 3, 4, 5, 6, 100]})
    >> outlier_info = detect_outliers(df)
    >> print(outlier_info)

    """
    #Implemented at the next release

