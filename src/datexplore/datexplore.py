import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def clean_names(data, case = "snake_case"):
    """Clean all column names of a dataframe.

    Make all column names in a dataframe such that the names only use letters, numbers, and underscores. 
    Capitalization format is specifed using the case parameter. 
    
    Parameters
    ----------
    data : pandas.core.frame.DataFrame
        Dataframe containing data with column names. 
    case : str, optional
        Indicates the capitalization structure of the clean names (snake_case, CamelCase, lowerCamelCase)

    Returns
    -------
    pandas.core.frame.DataFrame
        Dataframe with clean column names.

    Examples
    --------
    >>> from datexplore.clean_names import clean_names
    >>> import pandas as pd
    >>> data = pd.DataFrame{'Even Numbers': [2, 4, 6, 8],'odd numbers': [1, 3, 5, 7]}
    >>> clean_data = clean_names(data)
    """
    if case not in ["snake_case", "CamelCase", "lowerCamelCase"]: 
        raise ValueError("Incorrect input for case parameter")
    
    if not isinstance(data, pd.core.frame.DataFrame):
        raise TypeError("Incorrect input. Data must be of type pandas.core.frame.DataFrame ")
    
    for label in data.columns: 
        if not isinstance(label, str):
            raise TypeError("All column labels must be strings")
    

    if case == "snake_case":
        for label in data.columns:
            new = label.replace(" ", "_")
            for char in new:
                if (char.isalnum() == False) and char != '_':
                    new = new.replace(char, "")
            new = new.lower()
            data.rename(columns={label: new}, inplace=True)
    
    if case == "CamelCase":
        for label in data.columns:
            new = label.title()
            for char in label:
                if (char.isalnum() == False):
                    new = new.replace(char, "")
                    data.rename(columns={label: new}, inplace=True)
    
    if case == "lowerCamelCase":
        for label in data.columns:
            new = label.title()
            for char in label:
                if (char.isalnum() == False):
                    new = new.replace(char, "")
            new = new[0].lower() + new[1:]
            data.rename(columns={label: new}, inplace=True)

    return data
    

def visualise(df):
    """This function generates visualizations for a pandas DataFrame to identify patterns in missing values, correlation between variables, and distribution of variables and variable pairs.

    This function creates three types of plots:
    1. A heatmap of missing values: Each cell in the heatmap represents a value in the DataFrame. Cells are colored differently to indicate whether the value is missing or not. 
This helps in identifying patterns or areas with missing data.
    2. A correlation heatmap: This heatmap shows the correlation coefficients between all pairs of columns in the DataFrame.
       High positive or negative values indicate strong relationships, while values close to zero suggest weak relationship. This is useful for understanding the relationships between variables.
    3. A pairplot: This creates a grid of scatter plots for each pair of variables in the DataFrame. It helps in visualizing the distribution of individual variables and the relationships between them.
    
    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame for which the visualizations are to be generated.

    Returns
    -------
    None
        This function does not return any value. Instead, it displays the generated plots on the screen.

    Notes
    -----
    - The function utilizes seaborn and matplotlib libraries for plotting. Ensure these libraries are imported as 'sns' for seaborn and 'plt' for matplotlib.pyplot.

    Example Usage
    -------------
    >> from dataexplore import visualise
    >> visualise(df)
"""
    if not df.empty:
        plt.figure(figsize=(10, 4))
        sns.heatmap(df.isnull(), cbar = False, cmap = 'coolwarm')
        plt.title('Heatmap of Missing Values in DataFrame')
        plt.xlabel('Columns')
        plt.ylabel('Rows')
        if display==True:
            plt.show()
    
    if not df.select_dtypes(include='number').empty: 
        corr = df.select_dtypes(include='number').corr()
        plt.figure(figsize=(10, 4))
        sns.heatmap(corr, annot = True, cmap = 'coolwarm')
        plt.title('Correlation Heatmap of Variables in DataFrame')
        if display==True:
            plt.show()
            
        sns.pairplot(df)
        plt.figure(figsize=(10, 4))
        if display==True:
            plt.show()


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
