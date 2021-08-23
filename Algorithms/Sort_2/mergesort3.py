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

    if len(inputlist)==2:
            inputlist = sorted(inputlist)
    if len(inputlist)>=3:
        a = int(round(len(inputlist)/3))
        leftlist = inputlist[0:a]
        midlist = inputlist[a:a*2]
        rightlist = inputlist[a*2:]

       
        if len(leftlist)>=3:
                mergesort(leftlist)
        else:
                leftlist=sorted(leftlist)
        if len(midlist)>=3:
                mergesort(midlist)
        else:
                midlist=sorted(midlist)
        if len(rightlist)>=3:
                mergesort(rightlist)
        else:
                rightlist = sorted(rightlist)

        
        ir = im = il = it = 0
        case1 = il < len(leftlist) and im < len(midlist) and ir < len(rightlist)
        while case1:
            
            if leftlist[il] <= rightlist[ir] and leftlist[il] <= midlist[im]:
                inputlist[it]=leftlist[il]
                it += 1
                il += 1
 
            elif midlist[im] <=  rightlist[ir] and midlist[im]<=leftlist[il]:
                inputlist[it]=midlist[im]
                it += 1
                im += 1                    

            elif rightlist[ir] <= leftlist[il] and rightlist[ir] <= midlist[im]:
                inputlist[it]=rightlist[ir]
                it += 1
                ir += 1        

            case1 = il < len(leftlist) and im < len(midlist) and ir < len(rightlist)

#------------------------------------------------------------------------------------------
        case2 = il < len(leftlist) and im < len(midlist)
        while case2:
                if leftlist[il]< midlist[im]:
                        inputlist[it] = leftlist[il]
                        it +=1
                        il +=1
                        
                else:
                        inputlist[it] = midlist[im]
                        it +=1
                        im +=1
                        
                case2 = il < len(leftlist) and im < len(midlist)

#-----------------------------------------------------------------------------------------
        case3 = im < len(midlist) and ir < len(rightlist)
        while case3:
                if midlist[im]< rightlist[ir]:
                        inputlist[it] = midlist[im]
                        it +=1
                        im +=1
                        
                else:
                        inputlist[it] = rightlist[ir]
                        it +=1
                        ir +=1
                        
                case3 = im < len(midlist) and ir < len(rightlist)
#------------------------------------------------------------------------------------------

        case4 = il < len(leftlist) and ir < len(rightlist)
        while case4:
                if leftlist[il]< rightlist[ir]:
                        inputlist[it] = leftlist[il]
                        it +=1
                        il +=1
                        
                else:
                        inputlist[it] = rightlist[ir]
                        it +=1
                        ir +=1
                        

                case4 = il < len(leftlist) and ir < len(rightlist)
        case5 = il < len(leftlist) 
        case6 = im < len(midlist) 
        case7 = ir < len(rightlist) 
        if case5:
            while case5:
                inputlist[it]=leftlist[il]
                it +=1
                il += 1
 
                case5 = il < len(leftlist) 
        elif case6:
            while case6:
                inputlist[it]=midlist[im]
                it +=1
                im += 1
     
                case6 = im < len(midlist)
        elif case7:
            while case7:
                inputlist[it]=rightlist[ir]
                it +=1
                ir += 1
  
                case7 = ir < len(rightlist)      
        
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

