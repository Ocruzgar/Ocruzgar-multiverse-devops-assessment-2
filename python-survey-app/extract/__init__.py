def get_input(filename):
    rows = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            list = line.strip().split(',') #clean the /n at the end of the line and separate the line in an array by ,
            if not is_duplicate(rows,list[0]): #checking if the user_id for this line already exist in rows
                rows.append(list)
    return rows

def is_duplicate (list, to_find):

    is_duplicate = False   
    for item in list:
        if item[0] == to_find:
            is_duplicate = True
    return is_duplicate