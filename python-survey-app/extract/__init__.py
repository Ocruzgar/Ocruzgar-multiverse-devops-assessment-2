def get_input(filename):
    rows = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            list = line.strip().split(',') #clean the /n at the end of the line and separate the line in an array by ,
            
            #checking if the user_id for this line already exist in rows, that is not empty and that has answers
            is_a_duplicate = is_duplicate(rows,list[0])
            has_user_id = list[0]!=""
            has_answers = not is_empty(list[1:])

            if not is_a_duplicate and has_user_id and has_answers: 
               
                if list[0]!='user_id':                    #Capitalizing name and last names but not the headers
                    list[1]=list[1].title()
                    list[2]=list[2].title()
                rows.append(list)

    print (rows)
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
