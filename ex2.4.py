import sys
import requests
import timeit
from matplotlib import pyplot as plt
import random
import json


sys.setrecursionlimit(20000)

def func1(arr, low, high):
    # Old Code:
    # if low < high:
    #     pi = func2(arr, low, high)
    #     func1(arr, low, pi-1)
    #     func1(arr, pi + 1, high)
    
    # New optimized code: 
    while low < high:
        pi = func2(arr, low, high)
        if (pi - low) < (high - pi):
            func1(arr, low, pi-1)
            low = pi + 1
        else:
            func1(arr, pi + 1, high)
            high = pi - 1
        

def func2(array, start, end):
    # pi = (start + end) // 2
    p = array[start]
    low = start + 1
    high = end
    
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]  
        else:
            break
    array[start], array[high] = array[high], array[start]  
    return high


url = "https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment2/ex2.json"

response = requests.get(url)

data = response.json()


for arr in data:
    random.shuffle(arr)

with open('ex2.5.json', 'w') as out:
    json.dump(data, out)


avg_data = []

file = open("ex2.5.json")

data = json.load(file)

for arr in data:
    high = len(arr) - 1
        
    rez = []
    tm = timeit.timeit(lambda: func1(arr, 0, high), number=10)
    
    rez.append(tm/10)
    
    avg = sum(rez) / len(rez)
    avg_data.append(avg)
    print(avg_data)
    




plt.plot(avg_data, color ="r")
plt.xlabel("input array")
plt.ylabel("Average time over 10 iterations")
plt.show()






