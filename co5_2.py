stud=open("stud.txt",'r')
oddline=open("odd.txt",'w')
evenline=open("even.txt",'w')
content=stud.readlines()
print("content of the file r:")
print(content)
for i in range(len(content)):
   if ((i%2)==0):
          evenline.write(content[i])
   else:
          oddline.write(content[i])


