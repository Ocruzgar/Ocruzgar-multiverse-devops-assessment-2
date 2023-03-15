def get_input(filename):
    rows = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            rows.append(line.strip().split(',')) #clean the /n at the end of the line and separate the line in an array by ,
    return rows