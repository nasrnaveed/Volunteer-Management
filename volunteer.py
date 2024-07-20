#Volunteer Count from txt file
exists = False
id = []
name = []
csp = []
i=0
file = open('/content/sample_data/First13.txt','r')
for each in file :
  exists = False
  arr = each.split()
  for i in range(len(id)):
    if (arr[-1] == id[i]) :
      csp[i]+=2
      exists = True
  if (exists != True):
    id.append(arr[-1])
    name.append(' '.join([str(elem) for elem in arr[:-1]]))
    csp.append(2)

#Entering count into a txt file
file = open('/content/sample_data/NOTEPAD.txt','w')
for i in range(len(id)):
  file.write(id[i])
  file.write("\t")
  file.write(name[i])
  file.write("\t")
  file.write(str(csp[i]))
  file.write("\n")

file.close()

#displaying count
print("\nEnrollment \t | \t Name \t \t \t | CSP")
for i in range(len(id)):
  print(id[i]," \t | ",name[i]," \t \t | ",csp[i])
