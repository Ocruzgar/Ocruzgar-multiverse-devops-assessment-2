def get_input(filename):
    rows = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            list = line.strip().split(',') #clean the /n at the end of the line and separate the line in an array by ,
            
            if list[0]=='user_id':
                rows.append(list)
            else:
                #checking if the user_id for this line already exist in rows
                is_a_duplicate = is_duplicate(rows,list[0])
                #User_is is not empty
                has_user_id = list[0]!=""
                #line has answers
                has_answers = not is_empty(list[1:])
            
                if not is_a_duplicate and has_user_id and has_answers: 
                    
                    #answer3 is between correct values
                    answer3_right_values = check_between_values(1,10,int(list[5]))
                    if answer3_right_values:
                        list[1]=list[1].title()
                        list[2]=list[2].title()
                        rows.append(list)
    return rows

def is_duplicate (list, to_find):
#Checking that the list does not contain already the element to_find

    is_duplicate = False   
    for item in list:
        if item[0] == to_find:
            is_duplicate = True
    return is_duplicate


def is_empty(list):
    
    is_empty = True
    for item in list:
        if item != "":
            is_empty = False

    return is_empty

def check_between_values(lower_value, upper_value,to_chec):
    if to_chec >=lower_value and to_chec<=upper_value:
        return True
    else:
        return False
        