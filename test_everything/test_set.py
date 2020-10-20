unique = []
filecountwithdots = 0
with open("Drive_C_dirlist.txt",'r') as f:
    for line in f:
        araara = f.readline()
        unique.append(araara)

unique = set(unique)
filecount = 0
with open("Unique_c_dirlist.txt",'w') as f:
    for elem in unique:
        f.write(elem)
        filecount+=1
        if '.' in elem:
           filecountwithdots+=1
           
    f.write("you have " + str(filecount)+ " extensions"+'\n')
    f.write("and "+ str(filecountwithdots)+ " real extension")