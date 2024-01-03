stud=open("stud.txt",'r')
oddline=open("odd.txt",'w')
evenline=open("even.txt",'w')
content=stud.readlines()
print("Contents of the file are")
print(content)
for i in range(len(content)):
 if(i%2==0):
  oddline.write(content[i])
 else:
  evenline.write(content[i])
stud.close()
evenline.close()
oddline=open("odd.txt",'r')
content1=oddline.readlines()
print("Odd lines")
print(content1)
evenline=open("even.txt",'r')
content2=evenline.readlines()
print("Even lines")
print(content2)
oddline.close()


