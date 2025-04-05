import csv
import math

def read_csv(filepath):
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = []
        for row in reader:
            print(row)
            rows.append(row)
    return rows

def join_csvs(file1, file2):
    rows1 = read_csv(file1)
    rows2 = read_csv(file2)
    lookup_dict = {}
    for row in rows2:
        lookup_dict[row['name']] = row
        
    combined = []
    for row in rows1:
        if row['name'] in lookup_dict:
            row['stride_length'] = lookup_dict[row['name']]['stride_length']
            row['stance'] = lookup_dict[row['name']]['stance']
            combined.append(row)

    return combined

def filter_print(combined):
    filtered = []
    for row in combined:
        if row['stance'] == 'bipedal':
            leg = float(row['leg_length'])
            stride = float(row['stride_length'])
            speed = ((stride / leg) - 1) * math.sqrt(leg * 9.8)
            row['speed'] = speed
            filtered.append(row)
            
    filtered = sorted(filtered, key=lambda x: x['speed'], reverse=True)
    
    for row in filtered:
        print('Name:', row['name'])
        print('Speed:', row['speed'])
    
def main():
    file1 = './meta-pe/dataset1.csv'
    file2 = './meta-pe/dataset2.csv'
    combined = join_csvs(file1, file2)
    filter_print(combined)

if __name__ == "__main__":
    main()


