divisor = int(input())
boundary = int(input())
largest = 0
for number in range(boundary, divisor-1, -1):
    if number%divisor==0:
        largest = number
        print(largest)
        break