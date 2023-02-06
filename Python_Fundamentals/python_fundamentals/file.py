num1 = 42 # variable declaration Data Types - Primitive - Numbers

num2 = 2.3 # variable declaration Data Types - Primitive - Numbers

boolean = True #variable declaration Data Types - Primitive - Boolean initialize

string = 'Hello World'#variable declaration - Data Types - Primitive - Strings initialize

pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration - Data Types - Composite - List initialize

person = {'name': 'John', 'location': 'Salt Lake','age': 37, 'is_balding': False} #variable declaration - Data Types - Composite - Dictionary initialize

fruit = ('blueberry', 'strawberry', 'banana')#variable declaration - Data Types - Composite - Tuples initialize

print(type(fruit)) #- log statement


print(pizza_toppings[1]) #- log statement

pizza_toppings.append('Mushrooms') #Data Types - Composite - List add value

print(person['name']) #- log statement

person['name'] = 'George' #Data Types - Composite - Dictionary change value

person['eye_color'] = 'blue' #Data Types - Composite - Dictionary add value

print(fruit[2])#- log statement

if num1 > 45: #Data Types-Conditional - if 
    print("It's greater") #- log statement 
else:#Data Types-Conditional - else
    print("It's lower")#- log statement 

if len(string) < 5:#Data Types-Conditional - if length check
    print("It's a short word!")#- log statement 
elif len(string) > 15:#Data Types-Conditional - else if length check
    print("It's a long word!")#- log statement 
else:#Data Types-Conditional - else length check
    print("Just right!")#- log statement 

for x in range(5):#for loop - 
    print(x)#- log statement 
for x in range(2, 5):# for loop - 2 start 5
    print(x)#- log statement 
for x in range(2, 10, 3):# for loop - 2 start 10 stop increments of 3
    print(x) #- log statement 
x = 0 #variable declaration
while (x < 5): #while loop- 
    print(x)#- log statement
    x += 1 #increment

pizza_toppings.pop() #Data Types - Composite - List delete value
pizza_toppings.pop(1)#Data Types - Composite - List delete value index of 1

print(person)#log statement
person.pop('eye_color')#Data Types - Composite - Dictionary change value
print(person)#log statement

for topping in pizza_toppings:#Conditional - for loop
    if topping == 'Pepperoni':#Condtional - if loop
        continue#continue
    print('After 1st if statement')#log statement
    if topping == 'Olives': #Condtional - if loop
        break#break


def print_hello_ten_times(): #function - 
    for num in range(10): #for loop - argument
        print('Hello')#log statement -return 


print_hello_ten_times()#log statement function 


def print_hello_x_times(x):#function - parameter
    for num in range(x):#  for loop - argument
        print('Hello')#log statement - return 


print_hello_x_times(4)#log statemnet fuction -parameter


def print_hello_x_or_ten_times(x=10):
    for num in range(x):#  for loop - argument
        print('Hello')#log statement - return


print_hello_x_or_ten_times() #log statemnet- function
print_hello_x_or_ten_times(4)#log statemnet - function - paremeter


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
