import sys
import requests
import timeit
from matplotlib import pyplot as plt




sys.setrecursionlimit(1000000)


def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
     


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


avg_data = []




for arr in data:
    # print(arr)
    high = len(arr) - 1
       
    rez = []
    tm = timeit.timeit(lambda: func1(arr, 0, high), number=10)
   
    rez.append(tm/10)
   
    avg = sum(rez) / len(rez)
    avg_data.append(avg)
    print(avg_data)
   




plt.plot(avg_data, color ="r")
plt.xlabel("arrays")
plt.ylabel("Average time over 10 iterations in seconds")
plt.show()
