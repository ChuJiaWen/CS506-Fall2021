def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    
    file = open(csv_file_path,'r')
    lines = file.readlines()
    result=[]
    for line in lines:
        values = line.split(',')
        record = []
        for x in line.split(','):
            if x.isnumeric():
                record.append(int(x))
            else:
                record.append(x)
        
        result.append(record)
        
    file.close()
    return result
