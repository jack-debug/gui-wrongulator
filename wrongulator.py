inputNum = []
outputNum = []

while True:
	equation = input("Type your equation\n")

	for i in range(0, len(equation)):
		if equation[i].isdigit():
			print(True)
			inputNum.append(equation[i])
		elif equation[i] == "+":
			print(False)
		elif equation[i] == "-":
			print(False)
		elif equation[i].lower() == "x":
			print(False)
		elif equation[i] == "/":
			print(False)
		else:
			print(False)

print(equation)
