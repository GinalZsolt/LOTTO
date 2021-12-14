import csv

def elso():
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
        

file =open(r"D:/Git GZs/Új mappa/LOTTO/otos.csv")
elso=True
data_array=[]
for row in file.readlines():
    if elso:
        elso=not elso
        continue
    data=[]
    data.append(int(row.split(';')[11]))
    data.append(int(row.split(';')[12]))
    data.append(int(row.split(';')[13]))
    data.append(int(row.split(';')[14]))
    data.append(int(row.split(';')[15]))

    data_array.append(data)



