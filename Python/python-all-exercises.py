import numpy
# Task
# You are given a 2-D array with dimensions NXM.S
# Your task is to perform the sum tool over axis 0 and then find the product of that result.
# Input Format
# The first line of input contains space separated values of N and M.
# The next N lines contains M space separated integers.
# Output Format
# Compute the sum along axis 0. Then, print the product of that sum.


import numpy

first_line= input()

N, M = [int(x) for x in first_line.split()]
data_array=[]

for i in range(N):
    data_array.append([int(x) for x in input().split()])

print (numpy.prod(numpy.sum(numpy.array(data_array), axis = 0)))