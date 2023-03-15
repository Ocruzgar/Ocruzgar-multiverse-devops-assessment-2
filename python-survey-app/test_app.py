from extract import get_input
def test_input_is_list():
    #Testing that results.csv data file can be successfully processed into a list.
    # Arrange
    
    filename ="results.csv"
    expected_output = list
    
    # Act
    output= get_input(filename)
    # Assert
    assert type(output) == expected_output
def test_input_is_correct():
    #Testing that the first line of our file match with the first line of our list
    #Testing that is reading the right number of lines
    # Arrange

    filename ="results.csv"
    expected_output = ['user_id','first_name','last_name','answer_1','answer_2','answer_3']
    expected_n_rows = 26


    # Act
    output= get_input(filename)
    output_first_line = output[0]
    output_n_rows = len(output)
    # Assert
    assert output_first_line == expected_output
    assert output_n_rows == expected_n_rows