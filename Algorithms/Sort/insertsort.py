# CS 325 - insertsort program
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


#insert sort
def insert_sort(input_array):
        for i in range (0, len(input_array)):
                for j in range (2,len(input_array[i])):
                        index = j
                        while index >1:
                                if input_array[i][index]< input_array[i][index-1]:
                                        temp = input_array [i][index]
                                        input_array[i][index] = input_array[i][index-1]
                                        input_array[i][index-1] = temp
                                index = index-1
        return input_array

sorted_data = insert_sort (data_array)

#print out the result
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
