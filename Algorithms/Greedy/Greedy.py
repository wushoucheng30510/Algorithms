# Read file
from __future__ import print_function
data_read = []
filein = open ("act.txt",'rt')
while True:
        line = filein.readline()
        line = line.replace("\n",'')
        if not line:
                break
        data_read.append (line)
filein.close()

# process the data   --------  item information 
set = []                                #set stores the number of each case
item = []                               #item stores the information of each work
for i in range(0,len(data_read)):
    if data_read[i].find(" ") == -1:
        set.append(data_read[i])
    else:
        item.append(data_read[i])

data= []
for i in range(0, len(item)):
    a = item[i].split(" ")
    a = list(map(int,a))
    data.append(a)

set = list(map(int,set))                        #let the elements become integer

def insert_sort(input_array):
        for i in range (0, len(input_array)):                       # regular insert sort by decreasing the start time
                index = 1
                a = i
                
                while a != 0:
                    if input_array[a][index] > input_array[a-1][index]:         # if the current value is bigger than the previous values, I change its position
                        temp = input_array [a]
                        input_array[a] = input_array[a-1]
                        input_array[a-1] = temp
                    a = a - 1
                    
        return input_array


def activity_schedule(activity,size):
    j = 0
    for i in range(0,len(size)):                                    # i determines the set
        print("Set",i+1)
        empty = []
        if i==0:
            j = 0
        else: 
            j = j + size[i-1]
        for k in range(j,j+size[i]):
            empty.append(activity[k])                               #put the current set's activities into a empty list for future use
        a = insert_sort(empty)

        list_ac = []
        index_list = -1 
        for i in range (0,len(a)):                                  # start to do scheduling
            if i == 0:                                               
                list_ac.append(a[i])                                # schedule the first item in the list
                index_list += 1
            
            if list_ac[index_list][1] >= a[i][2]:                   # if the current activity's start time is bigger than the next activity's finish time, it means the next activity can be put in the list
                b = a[i][0]
                list_ac.append(a[i])
                index_list += 1

        activity_list = []
        for i in range(len(list_ac)-1,-1,-1):
            activity_list.append(list_ac[i][0])
        
        print("Number of activities selected",len(activity_list))

        string_ints = [str(int) for int in activity_list]
        output = " ".join(string_ints)

        print("Activities",output)

activity_schedule(data,set)

