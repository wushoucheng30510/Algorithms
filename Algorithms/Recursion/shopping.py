from __future__ import print_function
# Read file
data_read = []
filein = open ("shopping-1.txt",'rt')
while True:
        line = filein.readline()
        line = line.replace("\n",'')
        if not line:
                break
        data_read.append (line)
filein.close()

# process the data   --------  item information
data = []
item = []
for i in range(0,len(data_read)):
    if data_read[i].find(" ") == -1:
        data.append(data_read[i])
    else:
        item.append(data_read[i])

# process the data   --------  wt and val
wt = []
val = []
for i in range(0, len(item)):
    a = item[i].split(" ")
    val.append(a[0])
    wt.append(a[1])

# data, wt, val => integer array 
data = list (map (int,data))
val = list(map (int, val))
wt = list(map(int,wt))


# generate group data array (item, people, ability)
num = data.pop(0)           # how many cases
group = [0 for i in range(num)]
j = j2 = 0 
for i in range(0,num):
    if i == 0:
        j = 0
        j2= 2+data[j+1]
    else:
        j = j2
        j2 = 2 + j + data[j+1]
    empty = []
    for k in range(j,j2):
        empty.append(data[k])
    group[i] = empty

#group of data (val, wt)
group_val = [0 for i in range(num)]
group_wt = [0 for i in range(num)]
start = end = 0
for i in range(0,num):
    items = group[i][0]
    people = group[i][1]
    empty = []
    empty2 = []
    if i == 0:
        start = 0
        end = start + items
    else:
        start = end
        end = start + items
    for k in range(start, end):
       empty.append(val[k])
       empty2.append(wt[k])
    group_val[i] = empty
    group_wt[i] =empty2


#Knapsack function
def knapsack_DP(wt,val,total_weights):
    item_row = len(val)
    weights_column = total_weights

    v_table = [[0 for _ in range(weights_column+1)] for _ in range(item_row+1)]

    for i in range (1,item_row+1):
        for w in range (1,weights_column+1):
            if wt[i-1] <= w:
                v_table[i][w] = max(val[i-1]+v_table[i-1][w-wt[i-1]], v_table[i-1][w])
            else:
                v_table[i][w] = v_table[i-1][w]

    i = len(val)
    k = weights_column
    table = []
    while i != 0:
        if v_table[i][k] != v_table[i-1][k]:
            a = i
            table.append(a)
            i = i-1
            k = k- wt[i]
        else:
            i = i-1

    #return v_table[len(val)][total_weights]
    return table, v_table[len(val)][total_weights]

# Caculate total price of each group
total_price = []
member = []

for i in range(0,num):
    sum = 0
    empty = []
    for k in range (2,len(group[i])):
        a,b = knapsack_DP(group_wt[i],group_val[i],group[i][k])
        empty.append(a)
        sum += b
    member.append(empty)
    total_price.append(sum)

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

for i in range(len(member)):
    for k in range((len(member[i]))):
        mergesort(member[i][k])


f = open("result.txt","w+")
for i in range(0,num):
    f.write("Test Case"+str(i+1)+"\n")
    f.write("Total Price"+ str(total_price[i])+"\n")
    f.write("Member Items:"+"\n")
    for k in range(len(member[i])):
        ints = member[i][k]
        string_ints = [str(int) for int in ints]
        str_of_ints = " ".join(string_ints)
        f.write("%s:" %str(k+1) + str_of_ints+"\n")
    f.write("\n")
f.close()