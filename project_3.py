# Write a Python Program for Fibonacci numbers.
num = int(input("Enter the Fib Range: "))
First = 0
Second = 1
if num <= 0:
    print("Please enter a positive integer")
elif num == 1:
    print(num)
else:
    print("Fibonacci sequence:")
    for n in range(0, num):
        if(n <= 1):
            next = n
        else:
            next = First + Second
            First = Second
            Second = next
            print(next)
