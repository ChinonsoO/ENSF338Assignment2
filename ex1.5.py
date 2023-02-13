import timeit
from matplotlib import pyplot as plt



def fib2(n, cache={}):
    if n == 0 or n == 1:
        return n
    else:
        if n in cache:
            return cache[n]
        else:
            cache[n] = fib2(n-1) + fib2(n-2)


            return cache[n]

def func(n): 
    if n == 0 or n == 1: 
        return n 
    else: 
        return func(n-1) + func(n-2)
    


avgtimes = []
avgtimes_optimized = []
# For fibonacci's from 0 - 35...
fibs = [x for x in range(36)]
for num in fibs:
    # Generate a list of that input length,
    # numbers = [x for x in range(num)]
    rez = []
    rez2 = []
    # then, consider 1000 different random permutations of that list. For each
    # permutation, time how long it takes to find the number 5 in the list.
    # For increased accuracy, use timeit and ask it to run the test 100 times
    # for i in range(1000):
    # random.shuffle(numbers)
    tm = timeit.timeit("func(num)", setup="from __main__ import func, num", number=100)
    tm1 = timeit.timeit("fib2(num)", setup="from __main__ import fib2, num", number=100)
    rez.append(tm/100)
    rez2.append(tm1/100)
    # Then, compute the average execution times across all permutations
    # and add it to our list of average times
    avg = sum(rez) / len(rez)
    avg_optimized = sum(rez2) / len(rez2)
    avgtimes.append(avg)
    avgtimes_optimized.append(avg_optimized)
    print(f'Average time for fib({num}) is {avg}\n')
    print(f'Average time for optimized fib({num}) is {avg_optimized} ')
    
    
plt.plot(avgtimes, color='r', label="fib w/out memoization")
plt.plot(avgtimes_optimized, color = 'b', label="fib w/ memoization")
plt.legend(loc="upper left")
plt.xlabel("Fibonacci number")
plt.ylabel("Average time over 100 iterations")
plt.show()



# input1 = data[0]

# input2 = data[1]

# input3 = data[2]

# input4 = data[3]

# input5 = data[4]

# input6 = data[5]

# input7 = data[6]

# input8 = data[7]

# input9 = data[8]

# input10 = data[9]

# print(input5)

