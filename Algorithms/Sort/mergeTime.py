# CS 325 - mergesort program
# read a file
import random
import time
import matplotlib.pyplot as plt

'''
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

print ("merge sort")
print ("")

# process the data
for i in range (0,len(data_read)):
        if data_read[i] != []:
                data = data_read[i].split(" ")
                lastnumber = data[-1]
                data.pop()
                data.append(lastnumber)
                data = list (map (int,data))
        data_array.append(data)
'''

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




def random_list(min,max,length):

        outlist=[]
        for i in range(0,length):
                c = random.randint(min,max)
                outlist.append(c)
        return outlist

num_list = []

for i in range (2000,26000,4000):
        a = random_list(0,10000,i)
        num_list.append(a)

time_list = []

for i in range (0,len(num_list)):

        start = time.time()
        mergesort(num_list[i])
        end = time.time() - start
        print (end)
        time_list.append(end)

x_r = [i for i in range (2000,26000,4000)]
plt.plot(x_r,time_list,'o-', label ="speed of insert sort")
plt.xlabel("array_size")
plt.ylabel("second")
plt.show()