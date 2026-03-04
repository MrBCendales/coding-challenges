#Task
#The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

#1.The first line contains the sum of the two numbers.
#2.The second line contains the difference of the two numbers (first - second).
#3.The third line contains the product of the two numbers.

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b, a - b, a * b, sep='\n')


#Task
#The provided code stub reads two integers,  and , from STDIN.

#Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

#No rounding or formatting is necessary.

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b, a/b, sep="\n")