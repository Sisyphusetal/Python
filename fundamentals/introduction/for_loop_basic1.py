#Basic
for num in range(151):
    print(num)

#Multiples of Five
for num in range(5,1001):
    if num%5 == 0:
        print(num)

#Counting, the Dojo Way
for num in range(1,101):
    if num%10 == 0:
        print("Coding Dojo")
    elif num%5 == 0:
        print("Coding")
    else:
        print(num)

#Whoa, that Sucker's Huge
sum = 0
for num in range(500001):
    if num%2 != 0:
        sum += num
print(sum)

#Countdown by fours
for num in range(2018,0,-4):
    print(num)

#Flexible Counter
lowNum = 1
highNum = 16
mult = 2
for num in range(lowNum, highNum+1):
    if num%mult == 0:
        print(num)