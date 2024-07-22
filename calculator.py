def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def mul(a,b):
	return a*b
def div(a,b):
	return a/b
def power(a,b):
	return a**b
print("Select the operation:")
print("1.Add\n 2.Subtract\n 3.Multiply\n 4.Divide\n 5.Power");
while True:
	choice=input("Enter your choice:")
	a=int(input("Enter a value:"))
	b=int(input("Enter b value:"))
	if(choice=="1"):
		print("the sum is:",add(a,b))
	elif(choice=="2"):
		print("the difference is:",sub(a,b))
	elif(choice=="3"):
		print("the product is:",mul(a,b))
	elif(choice=="4"):
		print("the division is:",div(a,b))
	elif(choice=="5"):
		print("the exponential value is:",power(a,b))
	else:
		print("Warning: Please Enter the value in between 1 to 5")


