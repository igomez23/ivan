# Python program for simple calculator 

# Function to add two numbers 
def add(num1, num2): 
	return num1 + num2 

# Function to subtract two numbers 
def subtract(num1, num2): 
	return num1 - num2 

# Function to multiply two numbers 
def multiply(num1, num2): 
	return num1 * num2 

# Function to divide two numbers 
def divide(num1, num2): 
	return num1 / num2 


# Take input from the user 
select = input("Select operations form add, sub, div, mul :") 

number_1 = int(input("Enter first number: ")) 
number_2 = int(input("Enter second number: ")) 

if select == 'add': 
	print(number_1, "+", number_2, "=", 
					add(number_1, number_2)) 

elif select == 'sub': 
	print(number_1, "-", number_2, "=", 
					subtract(number_1, number_2)) 

elif select == 'div': 
	print(number_1, "*", number_2, "=", 
					multiply(number_1, number_2)) 

elif select == 'mul': 
	print(number_1, "/", number_2, "=", 
					divide(number_1, number_2)) 
else: 
	print("Invalid input") 

