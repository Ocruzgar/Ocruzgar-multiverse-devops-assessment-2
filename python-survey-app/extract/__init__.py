def get_input(filename):
    rows = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            list = line.strip().split(',') #clean the /n at the end of the line and separate the line in an array by ,

            #checking if the user_id for this line already exist in rows, that is not empty and that has answers
            if not is_duplicate(rows,list[0]) and list[0]!="" and not is_empty(list[1:]): 
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
