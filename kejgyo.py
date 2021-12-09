import csv

def elso:
    with open('otos.csv', 'r') as file:
        reader =csv.reader(file)
        array=[]
        first=True
        for row in reader:
            if first:
                first=not first
                continue
            array.append(row)
        numbre=str(array[0]).split(';')
        print(numbre[11:16])
        numbre=str(array[1]).split(';')
        print(numbre[11:16])
        
def gyakori:
    with open('otos.csv', 'r') as file:
        reader =csv.reader(file)
        array=[]
        first=True
        for row in reader:
            if first:
                first=not first
                continue
            array.append(row)
        