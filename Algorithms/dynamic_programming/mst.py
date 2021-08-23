from __future__ import print_function
data_read = []
filein = open ("graph.txt",'rt')
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
case = data_read[0]
case = int(case)
for i in range(1,len(data_read)):
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


def distance(a,b):
    d = ((a[0]-b[0])*(a[0]-b[0]) + (a[1]-b[1])*(a[1]-b[1])) ** 0.5      # calcuate the distance
    d = round(d)
    return d 

list = []

def pick_node(graph,parent):                                #graph 
    index = 0
    a = []
    b = []
    list = []
    min = float ('Inf')                                     #set min as an infinity number  
    for j in range(len(parent)):
        for i in range(len(graph)):
            d = distance(parent[j],graph[i])
            if d< min:
                min = d
                index = i
                a = graph[i]
                b = parent[j]
    list.append(b)
    list.append(a)
    list.append(min)
    return a , index , list, min

for i in range(0,case):
    print("Test Case",i)
    print("Edges in MST")
    a = []
    j = set[i]
    for k in range(j):
        a.append(data[0])
        data.pop(0)

    empty = []
    b = a.pop(0)
    empty.append(b)
    list = []
    sum = 0
    for k in range(len(a)):
        v,i,l,m = pick_node(a,empty)
        sum += m
        list.append(l)
        b = a.pop(i)
        empty.append(v)

    print("Point (x,y)        Distance")
    for q in range(0,len(list)):
        print((list[q][0][0],list[q][0][1]), "-",(list[q][1][0],list[q][1][1]),"  ",list[q][2])
    
    print("      Total Distance",sum)


