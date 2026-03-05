import numpy
# Task
# You are given a 2-D array with dimensions NXM.S
# Your task is to perform the sum tool over axis 0 and then find the product of that result.
# Input Format
# The first line of input contains space separated values of N and M.
# The next N lines contains M space separated integers.
# Output Format
# Compute the sum along axis 0. Then, print the product of that sum.


first_line= input()
second_line = input()
third_line = input()

N, M = [int(x) for x in first_line.split()]

for i in range(N-1):
    input()

data_array=[[int(x) for x in second_line.split()], [int(x) for x in third_line.split()]]



print (numpy.prod(numpy.sum(data_array, axis = 0), axis=None))