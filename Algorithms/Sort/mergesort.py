# CS 325 - mergesort program
# read a file
from __future__ import print_function
data_read = []
filein = open ("data.txt",'rt')
while True:
        line = filein.readline()
        if not line:
                break
        data_read.append (line)
filein.close()

data =[]
data_array = []
# process the data
for i in range (0,len(data_read)):
        if data_read[i] != []:
                data = data_read[i].split(" ")
                lastnumber = data[-1]
                data.pop()
                data.append(lastnumber)
                data = list (map (int,data))
        data_array.append(data)


def mergesort(inputlist):
    if len(inputlist)>=2:
        center = int(round(len(inputlist)/2))
        leftlist = inputlist[0:center]
        rightlist = inputlist[center:]

        mergesort(leftlist)
        mergesort(rightlist)

        ir = il = it = 0
        case1 = il < len(leftlist) and ir < len(rightlist)
        while case1:
            if leftlist[il] < rightlist[ir]:
                inputlist[it]=leftlist[il]
                il += 1
                it += 1
            else:
                inputlist[it]=rightlist[ir]
                ir += 1                    
                it += 1
            case1 = il < len(leftlist) and ir < len(rightlist)

        case2 = il < len(leftlist) 
        case3 = ir < len(rightlist) 
        if case2:
            while case2:
                inputlist[it]=leftlist[il]
                il += 1
                it += 1
                case2 = il < len(leftlist) 
        elif case3:
            while case3:
                inputlist[it]=rightlist[ir]
                ir += 1
                it += 1
                case3 = ir < len(rightlist) 
    return inputlist

sorted_data = []
for i in range (0,len(data_array)):
    elements = data_array[i].pop(0)
    result = [elements] + mergesort(data_array[i])
    sorted_data.append(result)


for i in range (0,len(data_read)):
        if sorted_data [i][0] != len(sorted_data[i])-1:
                print ("format error, the length of data is not correct")
        else:
                if sorted_data[i] != []:
                        for j in range(0,len(sorted_data[i])):
                                print (sorted_data[i][j],end=' ')
                else:
                        print ("")
        print("")