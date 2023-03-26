from extract import get_input
from extract import get_output
from filecmp import cmp

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
    expected_n_rows = 17


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


def test_capitalization():
    #testing that first and last name are capitalised

    # Arrange
    filename ="results.csv"

    # Act
    output = get_input(filename)

    # Assert
    i=1 #I don't want to check the headers
    while i< len(output):
        assert output[i][1].istitle()    #Using istitle to account for compound names and last names
        assert output[i][2].istitle()
        i=i+1
    

def test_answer3():
    #testing that answer 3 has values between 1 and 10

    # Arrange
    filename ="results.csv"

    # Act
    output = get_input(filename)

    # Assert

    i=1 #I don't want to check the headers

    while i< len(output):
        assert int(output[i][5])<=10
        assert int(output[i][5])>=1
        i=i+1


def test_output_file():
    #testing that a csv file has been create with the clean input

    # Arrange
    input_file ="results.csv"
    output_file ="clean_results.csv"
    compare_file =["user_id,first_name,last_name,answer_1,answer_2,answer_3",
                   "1,Charissa,Clark,yes,c,7",
                   "2,Richard,Mckinney,yes,b,7",
                   "3,Patience,Reeves,yes,b,9",
                   "5,India,Gentry,yes,c,7",
                   "6,Abra,Sheppard,yes,b,6",
                   "8,Diana,Cameron,yes,b,9",
                    "9,Alexander,Herring,no,b,4",
                    "11,Uma,Glass,yes,a,2",
                    "12,Brittany,Weeks,yes,b,8",
                    "13,Roth,Stout,yes,c,10",
                    "14,Amos,Daniel,yes,a,5",
                    "16,Eugenia,Nichols,yes,b,6",
                    "17,Dieter,Alvarado,yes,b,6",
                    "18,Roary,Frank,yes,c,7",
                    "19,Ulric,Hensley,no,b,9",
                    "20,Felicia,Wilkins,yes,b,8"]

    # Act
    get_input(input_file)
    
    # Assert
    i = 0
    with open(output_file, 'r') as f:
        for line in f.readlines():
            assert line.strip() == compare_file[i]
            i= i+1
    
def test_output_print(capsys):
    #testing that the file is print on screen

    #Arrange
    
    file = 'clean_results.csv'
    expected_file = 'clean_results_test.csv'
    expected_output = []
    with open(expected_file, 'r') as f:
        for line in f.readlines():
            expected_output.append(line.strip())
    

    #Act
    get_output(file)
    captured = capsys.readouterr()
    output_print = captured.out.strip().split('\n')


    #Assert
    
    i = 0
    
    while i < len(output_print):
        assert output_print[i] == expected_output[i]
        i= i+1

    