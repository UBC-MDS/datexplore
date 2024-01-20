from datexplore.datexplore import clean_names
from datexplore.datexplore import detect_outliers
from datexplore.datexplore import visualise

import pytest
import pandas as pd
import numpy as np

#---------------------Tests for detect_outliers()--------------------------------------------

#Test Case 1: Dataframe with no outliers

def test_basic_no_outliers():
    df = pd.DataFrame({'A': [10, 12, 11, 13, 14], 'B': [20, 21, 19, 22, 23]})
    result = detect_outliers(df)
    assert result.empty, "No outliers expected but found"


#Test Case 2: Handles dataframe with outliers

def test_detect_outliers():
    df = pd.DataFrame({'A': [1, 2, 3, 100], 'B': [10, 20, 30, 400]})
    result = detect_outliers(df)
    assert not result.empty, "Outliers expected but not found"
    assert len(result) == 2, "Incorrect number of outliers detected"

#Test Case 3: Mixed datatypes allowed but aren't analyzed

def test_mixed_data_types():
    df = pd.DataFrame({'A': [1, 2, 3, 100], 'B': ['X', 'Y', 'Z', 'W']})
    result = detect_outliers(df)
    assert 'B' not in result.columns, "Non-numeric column should not be processed"

#Test Case 4: Empty dataframe accepted

def test_empty_dataframe():
    df = pd.DataFrame()
    result = detect_outliers(df)
    assert result.empty, "No data to process but output is not empty"

#Test Case 5: Different sized dataframes handled

def test_single_column():
    df = pd.DataFrame({'A': [1, 2, 3, 100]})
    result = detect_outliers(df)
    assert not result.empty, "Outliers expected but not found"

#Test Case 6: Only accepts dataframes

def test_non_dataframe_input():
    with pytest.raises(TypeError):
        detect_outliers([1, 2, 3])

#Test Case 7: Correctly identifies the outliers, their deviation and their category for multiple columns
        
def test_correct_outliers_detection():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 100], 'B': [5, 6, 7, 8, 200]})
    expected_outliers = pd.DataFrame({
        'column': ['A', 'B'],
        'index': [4, 4],
        'outlier_value': [100, 200],
        'deviation': [93.75, 189.75], 
        'category': ['Extreme', 'Extreme'] 
    })
    result = detect_outliers(df)
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_outliers)


#Test Case 8: Correctly identifies the outliers, their deviation and their category for a single column
    
def test_outlier_details():
    df = pd.DataFrame({'A': [1, 2, 3, 100]})
    expected_outliers = pd.DataFrame({
        'column': ['A'],
        'index': [3],
        'outlier_value': [100],
        'deviation': [71.25],
        'category': ['Extreme']
    })
    result = detect_outliers(df)
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_outliers)

#Test Case 9: Correctly handles different outlier labels

def test_outlier_category_labeling():
    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100],
        'B': [20, 21, 19, 22, 23, 27, 16, 20, 19 , 50, 51],
        'C': [10, 12, 14, 16, 18, 19, 20, 14, 15, 16, 31]
    })
    expected_categories = {
        'A': ['Extreme'],
        'B': ['Severe', 'Severe'],
        'C': ['Moderate']
    }

    actual_outliers = detect_outliers(df)
    for column, categories in expected_categories.items():
        actual_categories = actual_outliers[actual_outliers['column'] == column]['category'].tolist()
        assert actual_categories == categories, f"Mismatch in categories for column {column}"


#---------------------Tests for Visualize()----------------------------------------------

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


#---------------------Tests for clean_names()--------------------------------------------
def test_clean_names_error():
    """Test that proper Errors are raised for clean_names function with incorrect input parameters."""
    with pytest.raises(ValueError):
        unclean_df =  pd.DataFrame({'course code': ['531', '511', '562'],
        'Block_number': [25, 30, 35],
        'course Instructor    name': ['Joel', 'Quan', 'Alexi']})
        clean_names(unclean_df, "not_a_param_option")
    
    with pytest.raises(TypeError):
        not_df = pd.Series([1,2,3,4])
        clean_names(not_df)
    
    with pytest.raises(TypeError):
        no_string_df = pd.DataFrame({000: ['531', '511', '562'],
        1.234: [25, 30, 35],
        0000: ['Joel', 'Quan', 'Alexi']})
        clean_names(no_string_df)

def test_clean_names():
    """Test clean_names return object"""
    
    unclean_df =  pd.DataFrame({'course code': ['531', '511', '562'],
        'Block_number': [25, 30, 35],
        'course Instructor name': ['Joel', 'Quan', 'Alexi']})
    
    expected_snake = pd.DataFrame({'course_code': ['531', '511', '562'],
        'block_number': [25, 30, 35],
        'course_instructor_name': ['Joel', 'Quan', 'Alexi']})
    actual_snake = clean_names(unclean_df)

    unclean_df =  pd.DataFrame({'course code': ['531', '511', '562'],
        'Block_number': [25, 30, 35],
        'course Instructor name': ['Joel', 'Quan', 'Alexi']})

    expected_camel = pd.DataFrame({'CourseCode': ['531', '511', '562'],
        'BlockNumber': [25, 30, 35],
        'CourseInstructorName': ['Joel', 'Quan', 'Alexi']})
    
    actual_camel = clean_names(unclean_df, "CamelCase")

    unclean_df =  pd.DataFrame({'course code': ['531', '511', '562'],
        'Block_number': [25, 30, 35],
        'course Instructor name': ['Joel', 'Quan', 'Alexi']})
    
    expected_lower_camel = pd.DataFrame({'courseCode': ['531', '511', '562'],
        'blockNumber': [25, 30, 35],
        'courseInstructorName': ['Joel', 'Quan', 'Alexi']})
    actual_lower_camel = clean_names(unclean_df, "lowerCamelCase")

    assert isinstance(clean_names(unclean_df), pd.core.frame.DataFrame), "Wrong return type"
    assert list(actual_camel.columns).sort() == list(expected_camel.columns).sort(), "Incorrect clean column names, not proper CamelCase"
    assert list(actual_snake.columns).sort() == list(expected_snake.columns).sort(), "Incorrect clean column names, not proper snake_case"
    assert list(actual_lower_camel.columns).sort() == list(expected_lower_camel.columns).sort(), "Incorrect clean column names, not proper lowerCamelCase"

    assert actual_lower_camel.shape == actual_camel.shape == actual_snake.shape == unclean_df.shape, "data frame shape should not change"
