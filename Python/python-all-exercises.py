import numpy as np
# Task / prod - sum
# You are given a 2-D array with dimensions NXM.S
# Your task is to perform the sum tool over axis 0 and then find the product of that result.
# Input Format
# The first line of input contains space separated values of N and M.
# The next N lines contains M space separated integers.
# Output Format
# Compute the sum along axis 0. Then, print the product of that sum.


first_line= input()

N, M = [int(x) for x in first_line.split()]
data_array=[]

for i in range(N):
    data_array.append([int(x) for x in input().split()])

print (np.prod(np.sum(np.array(data_array), axis = 0)))

# Task / min max
# You are given a 2-D array with dimensions NXM.
# Your task is to perform the min function over axis 1 and then find the max of that.
# Input Format
# The first line of input contains the space separated values of N and M.
# The next IN lines contains M space separated integers.
# Output Format
# Compute the min along axis 1 and then print the max of that result.

N, M = [int(x) for x in input().split()]

data_array=[]
for i in range(N):
    data_array.append([int(x) for x in input().split()])

np_array=np.array(data_array)
print(np.max(np.min(np_array, axis = 1)))

# Task
# You are given a 2-D array of size NXM.
# Your task is to find:
# 1. The mean along axis 1
# 2. The var along axis 0
# 3. The std along axis

# Enter your code here. Read input from STDIN. Print output to STDOUT

N, M = [int(x) for x in input().split()]

data_array = []

for i in range(N):
    data_array.append([int(x) for x in input().split()])

np_array = np.array(data_array)

print(np.mean(np_array, axis = 1))
print(np.var(np_array, axis = 0))
print(round(np.std(np_array), 11))



# Task
# You are given two arrays A and B. Both have dimensions of NX.N.
# Your task is to compute their matrix product.
# Input Format
# The first line contains the integer N.
# The next IN lines contains IN space separated integers of array A.
# The following N lines contains N space separated integers of array B.
# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())
A = []
B = []

for i in range(N):
    A.append([int(x) for x in input().split()])
for i in range(N):
    B.append([int(x) for x in input().split()])
    
array_A = np.array(A)
array_B = np.array(B)

print(np.dot(array_A, array_B))
            

# Task
# You are given two arrays: A and B.
# Your task is to compute their inner and outer product.
# Input Format
# The first line contains the space separated elements of array A
# The second line contains the space separated elements of array B.
# Output Format
# First, print the inner product.
# Second, print the outer product.

A = np.array([int(x) for x in input().split()])
B = np.array([int(x) for x in input().split()])

print(np.inner(A, B))
print(np.outer(A, B))

