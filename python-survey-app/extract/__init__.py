import csv
import os
def get_input(filename):
    rows = []
    output_file = "./clean_results.csv"
    with open(filename, 'r') as f:
        for line in f.readlines():
            list = line.strip().split(',') #clean the /n at the end of the line and separate the line in an array by ,
            
            if list[0]=='user_id':
                rows.append(list)
                write_csv(output_file,list)
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
                        append_csv(output_file,list)
        del_last_empty_line_csv(output_file)
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
        


def write_csv(file,row):
    with open(file, 'w',newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(row)

def append_csv(file,row):
    with open(file, 'a',newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(row)

def del_last_empty_line_csv(file):
    #delete the new line character of the last line so the output file does not have an empty line at the end
    with open(file, 'r+', newline='') as f:   #Open the file on read and write mode

        f.seek(0, os.SEEK_END)                #position at the end of the file
        f.seek(f.tell()-2, os.SEEK_SET)       #move back 2 character
        f.truncate()                          #truncate from position  


def get_output(filename):
    #read and print the file on screen line by line
    with open(filename, 'r') as f:
        for line in f.readlines():
            list = line.strip().split(',')
            print('%-7s %-15s %-15s %8s %8s %8s' % (list[0],list[1],list[2],list[3],list[4],list[5]))
#            list = line.strip().split(',')
#            if i==0: 
#                    print('%10s' % list)
#            else:

            #print(line)
#            i= i+1

