import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualise(df, display = False):
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
