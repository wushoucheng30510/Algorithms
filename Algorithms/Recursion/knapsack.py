#knapsack
from __future__ import print_function
import random
import time


def knapsack_REC(W,n,wt,val):

    if W==0:
        return 0
    if n==0:
        return 0
    if (wt[n-1]>W):
        return knapsack_REC(W, n-1, wt, val)
    else:
        return max(val[n-1]+ knapsack_REC(W-wt[n-1], n-1, wt, val), knapsack_REC(W, n-1, wt, val))



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

    return v_table[len(val)][total_weights]

W = 100
for size in range(10,45,5):
    val =[]
    wt = []
    for k in range(size):
        val.append(random.randint(1,100))
        wt.append(random.randint(1,20))

    time1 = time.time()
    a = knapsack_REC(W,len(val),wt,val)
    time2 = time.time()
 
    time3 = time.time()
    b = knapsack_DP(wt, val , W)
    time4 = time.time()
    print("N=",size , "W=", 100, "Rec time=%.6f" %(time2-time1), "DP time=%.6f" %(time4-time3), "Max Rec=", a , "Max DP=",b)


