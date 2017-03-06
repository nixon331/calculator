'''
Created on 24 Feb 2017

@author: James.Nixon
'''


#returns the sum of num1 and num2
def add(num1, num2):
	return num1 + num2

#returns the multiplication of num 1 and num2
def mul(num1, num2):
	return num1 * num2
	
#returns the subtration of num1 and num2
def sub(num1, num2):
	return num1 - num2
	
#returns the division of num1 and num2
def div(num1, num2):
	return num1 / num2
	
def main():
	operation = input("What do you want to do(+,-,*,/,exit): ")
	if(operation != "+" and operation != "-" and operation != "*" and operation != "/" and operation != "exit"):
		#invalid operation
		print("you must enter a valid operation")
		main()
	elif(operation == "exit"):
		raise SystemExit
	else:
		var1 = int(input("enter num1: "))
		var2 = int(input("enter num2: "))
		if(operation == "+"):
			print(add(var1, var2))
			main()
		elif(operation == "*"):
			print(mul(var1, var2))
			main()
		elif(operation == "-"):
			print(sub(var1, var2))
			main()
		elif(operation == "/"):
			print(div(var1, var2))	
			main()
			
	
	
main()
