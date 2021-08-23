# CS 325 - insertsort program
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
'''
print ("Insert sort")
print ("")


'''
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

#insert sort
def insert_sort(input_array):
 #       for i in range (0, len(input_array)):
                for j in range (0,len(input_array)):
                        index = j
                        while index >0:
                                if input_array[index]< input_array[index-1]:
                                        temp = input_array [index]
                                        input_array[index] = input_array[index-1]
                                        input_array[index-1] = temp
                                index = index-1
                return input_array
'''
sorted_data = insert_sort (data_array)

#print out the result
for i in range (0,len(data_read)):
        if sorted_data [i][0] != len(sorted_data[i])-1:
                print ("format error, the length of data is not correct")
        else:
                if sorted_data[i] != []:
                        print (sorted_data[i])
                else:
                        print ("")
'''



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
        insert_sort(num_list[i])
        end = time.time() - start
        print (end)
        time_list.append(end)

x_r = [i for i in range (2000,26000,4000)]
plt.plot(x_r,time_list,'o-', label ="speed of insert sort")
plt.xlabel("array_size")
plt.ylabel("second")
plt.show()