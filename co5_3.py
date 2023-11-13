import csv
with open("players.csv",'r') as efile:
    data=csv.reader(efile)
    for i in data:
        print(i)
   
