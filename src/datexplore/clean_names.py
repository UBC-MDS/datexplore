import pandas as pd
def clean_names(data, case = "snake_case"):
    """Clean all column names of a dataframe.

    Make all column names in a dataframe such that the names only use letters, numbers, and underscores. 
    Capitalization format is specifed using the case parameter. 
    "Unclean" column labels should be delimited by spaces for best results with case format. 
    
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
    >>> print(clean_data.columns)
    Index(['even_numbers', 'odd_numbers'], dtype='object')
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