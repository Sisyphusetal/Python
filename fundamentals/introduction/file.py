num1 = 42 #variable declaration, intialize int
num2 = 2.3 #variable declaration, intialize float
boolean = True #variable declaration, intialize boolean
string = 'Hello World' #variable declaration, intialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, list intialization
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, intialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, intialize tuple
print(type(fruit)) #log tuple type check
print(pizza_toppings[1]) #log list access value
pizza_toppings.append('Mushrooms') #list add value
print(person['name']) #log dictionary access value
person['name'] = 'George' #dictionary change value
person['eye_color'] = 'blue' #dictionary add value
print(fruit[2]) #log tuple access value

if num1 > 45: #conditional if
    print("It's greater") #log string
else: #conditional else
    print("It's lower") #log string


if len(string) < 5: #conditional if
    print("It's a short word!") #log string
elif len(string) > 15: #conditional else if
    print("It's a long word!") #log string
else: #conditional else
    print("Just right!") #log string


for x in range(5): #for loop start
    print(x) #log variable x
for x in range(2,5): #for loop start
    print(x) #log variable x
for x in range(2,10,3): #for loop start
    print(x) #log variable x
x = 0 #variable declaration, intialize number
while(x < 5): #while loop start
    print(x) #log variable x
    x += 1 #while loop increment

pizza_toppings.pop() #list, remove value
pizza_toppings.pop(1) #list, remove value at index 1

print(person) #log dictionary
person.pop('eye_color') #dictionary, remove value
print(person) #log dictionary

for topping in pizza_toppings: #for loop start
    if topping == 'Pepperoni': #conditional if
        continue #for loop continue
    print('After 1st if statement') #log string
    if topping == 'Olives': #conditional if
        break #for loop stop

def print_hello_ten_times(): #define function
    for num in range(10): # for loop start
        print('Hello') #log string

print_hello_ten_times() #call function

def print_hello_x_times(x): #define function with argument
    for num in range(x): #for loop start
        print('Hello') #log string

print_hello_x_times(4) #call function with specified argument

def print_hello_x_or_ten_times(x = 10):# define function with argument
    for num in range(x): #for loop start
        print('Hello') #log string

print_hello_x_or_ten_times() #call function
print_hello_x_or_ten_times(4) #call function with specified argument


"""
Bonus section
"""

# print(num3) Error, variable was not yet defined
# num3 = 72 variable declaration, intialize int
# fruit[0] = 'cranberry' Error, tuple is immutable cannot change value
# print(person['favorite_team']) Error, dictionary has no value 'favorite_team'
# print(pizza_toppings[7]) IndexError, list index is out of range
#   print(boolean) IndentationError
# fruit.append('raspberry') Error, tuple is immutable cannot add value
# fruit.pop(1) Error, tuple is immutable cannot remove value