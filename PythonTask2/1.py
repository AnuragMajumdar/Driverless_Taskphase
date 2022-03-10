import csv
import operator

f = open("names.csv", "a", newline="")
tup1 =(1,"Anurag")
writer=csv.writer(f)
writer.writerow(tup1)
tup1 =(4,"Anuradha")
writer=csv.writer(f)
writer.writerow(tup1)
tup1 =(7,"Som")
writer=csv.writer(f)
writer.writerow(tup1)
tup1 =(2,"Arunabha")
writer=csv.writer(f)
writer.writerow(tup1)
tup1 =(9,"Harvey")
writer=csv.writer(f)
writer.writerow(tup1)
tup1 =(3,"Liam")
writer=csv.writer(f)
writer.writerow(tup1)
tup1 =(5,"Spectre")
writer=csv.writer(f)
writer.writerow(tup1)
tup1 =(6,"Theo")
writer=csv.writer(f)
writer.writerow(tup1)
tup1 =(8,"Kim")
writer=csv.writer(f)
writer.writerow(tup1)
f.close()

file = open('names.csv','r')

csv_reader = csv.reader(file,delimiter=',')

sort = sorted(csv_reader, key=operator.itemgetter(0))

for eachline in sort:
    print(eachline)

file1=open('names.csv','r')
reader =csv.reader(file)
L=[]
rows=[0,2,4,6,8]
for row in reader:
    if row[0] == str(rows):
        Found=true
    else:
        L.append(row)
file1.close()

