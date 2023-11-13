with open("stud.txt") as f:
	slist=f.readlines()
print(slist)
slist=[x.strip() forx x in slist]
print("the content of file r:")
print(slist)

