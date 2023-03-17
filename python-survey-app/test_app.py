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
    expected_n_rows = 20


    # Act
    output= get_input(filename)
    output_first_line = output[0]
    output_n_rows = len(output)
    # Assert
    assert output_first_line == expected_output
    assert output_n_rows == expected_n_rows


def test_duplicates_remove():
    #testing that all duplicates has been removed

    # Arrange
    filename ="results.csv"


    # Act
    output_without_duplicates = get_input(filename)

    # Assert
    i=0
    while i < len(output_without_duplicates)-1:   #I dont need to test the last element as it will be already unique
        j=i+1
        while j < len(output_without_duplicates):
            assert output_without_duplicates[i][0]!= output_without_duplicates[j][0]
            j=j+1
        i=i+1

def test_no_ID_blanks():
    #testing that there are lines with blank user_id

    # Arrange
    filename ="results.csv"

    # Act
    output_without_blanks = get_input(filename)

    # Assert
    for i in output_without_blanks:
        assert i[0]!=""


def test_no_blanks_lines():
    #testing that there are not lines with user_id but without any answer

    # Arrange
    filename ="results.csv"

    # Act
    output_without_blanks = get_input(filename)

    # Assert
    for i in output_without_blanks:
        j=1 #starting at 1 as user_id will have a number
        while j<len(i):
            assert i[j]!=""
            j=j+1
