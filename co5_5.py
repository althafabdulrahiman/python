import csv
field=['rollno','name','age']
sdict=[{'rollno':7, 'name':"ronaldo",'age':35},
      {'rollno':10, 'name':"embape",'age':22}]
with open("ppt.csv",'w') as dfile:
             writer=csv.DictWriter(dfile,fieldnames=field)
             writer.writeheader()
             writer.writerows(sdict)

