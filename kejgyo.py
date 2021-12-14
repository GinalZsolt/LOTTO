from os import system
system('cls')

file =open(r"D:/Git GZs/LOTTO/otos.csv")
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
