import pandas as pd
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