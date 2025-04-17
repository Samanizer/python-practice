import csv

def join_files(file1, file2):
    
    dinos = {}
    with open(file1) as f1:
        reader = csv.DictReader(f1)
        
        for line in reader:
            dinos['name'] = line['name']
            print(line)

join_files('./meta-pe/dinos/dataset1.csv', '')