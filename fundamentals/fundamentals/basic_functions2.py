#Countdown from n
def countdown(number):
    for num in range(number,0,-1):
        print(num)

countdown(5)

#Print and Return
def listTwo(list):
    print(list[0])
    return list[1]

numbers = [1,7]
print(listTwo(numbers))

#First Plus Length
def sumList(list):
    return list[0]+len(list)

numbers = [4,3,2]
print(sumList(numbers))

#Values Greater Than Second
def betterList(list):
    newList = []
    sum = 0
    for num in list:
        if len(list)<2:
            return False
        elif num>list[1]:
            sum+=1
            newList.append(num)
    print(sum)
    return newList

numbers = [6,3,7,2,8]
print(betterList(numbers))

#This Length, That Value
def listMaker(size,value):
    sizeValue = []
    for num in range(size):
        sizeValue.append(value)
    return sizeValue

print(listMaker(4,3))
