import csv
def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    result=[]
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONE,quotechar="'")
        for row in reader:
            record = []
            for x in row:
                if x.isnumeric():
                    record.append(int(x))
                else:
                    record.append(x.replace('"',''))
            result.append(record)
    return result
