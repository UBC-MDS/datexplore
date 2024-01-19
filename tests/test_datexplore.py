from datexplore import datexplore

# Test Case 1: Basic Functionality
def test_basic_functionality():
    df = pd.DataFrame({
        'A': np.random.rand(100),
        'B': np.random.rand(100),
        'C': np.random.choice(['X', 'Y', 'Z'], 100)
    })
    try:
        visualise(df)
        print("test passed!")
    except Exception as e:
        pytest.fail(f" Unexpected Error: {e}")

# Test Case 2: Missing Values
def test_missing_values():
    df = pd.DataFrame({
        'A': np.random.rand(10),
        'B': [np.nan, *np.random.rand(9)]
    })
    try:
        visualise(df)
        print("test passed!")
    except Exception as e:
        pytest.fail(f"Missing Values: {e}")

# Test Case 3: Non-Numeric Data
def test_nonnumeric_data():
    df = pd.DataFrame({
        'A': np.random.choice(['X', 'Y', 'Z'], 10),
        'B': np.random.choice(['Cat', 'Dog', 'Bird'], 10)
    })
    try:
        visualise(df)
        print("test passed!")
    except Exception as e:
        pytest.fail(f"Non-numeric Data: {e}")

# Test Case 4: Empty DataVFrame
def test_empty_df():
    df = pd.DataFrame()
    try:
        visualise(df)
        print("test passed!")
    except Exception as e:
        pytest.fail(f"Empty DataFrame: {e}")

# Test Case 5: Single Column DataFrame
def test_single_column_df():
    df = pd.DataFrame({'A': np.random.rand(10)})
    try:
        visualise(df)
        print("test passed!")
    except Exception as e:
        pytest.fail(f"Only one data column used: {e}")

# Test Case 6: DataFrame with Special Values
def test_df_special_values():
    df = pd.DataFrame({
        'A': [np.nan, np.inf, - np.inf]
    })
    try:
        visualise(df)
    except Exception as e:
        pytest.fail(f"Special Values used: {e}")