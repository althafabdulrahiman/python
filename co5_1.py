with open("stud.txt") as f:
	slist=f.readlines()
print(slist)
slist=[x.strip() for x in slist]
print("the content of file r:")
print(slist)

