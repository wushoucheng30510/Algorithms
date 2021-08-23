# CS 325 - mergesort program
# read a file
import random
import time
import matplotlib.pyplot as plt


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




def random_list(min,max,length):

        outlist=[]
        for i in range(0,length):
                c = random.randint(min,max)
                outlist.append(c)
        return outlist

num_list = []

for i in range (5000,55000,5000):
        a = random_list(0,10000,i)
        num_list.append(a)

time_list = []

for i in range (0,len(num_list)):

        start = time.time()
        mergesort(num_list[i])
        end = time.time() - start
        print (end)
        time_list.append(end)

x_r = [i for i in range (5000,55000,5000)]
plt.plot(x_r,time_list,'o-', label ="speed of insert sort")
plt.xlabel("array_size")
plt.ylabel("second")
plt.show()