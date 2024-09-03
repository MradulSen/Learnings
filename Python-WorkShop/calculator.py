num1 = int(input("Enter First number: ")) 
num2 = int(input("Enter Second number: ")) 

print(type(num1))
print(type(num2))

sum_of_num = num1 + num2
print("Sum of two numbers",sum_of_num)

diff_of_num = num1 - num2
print("Diff of two numbers",diff_of_num)

prod_of_num = num1 * num2
print("Prod of two numbers",prod_of_num)

div_of_num = num1 /  num2
print("Div of two numbers",div_of_num)

rem_of_num = num1 %  num2
print("Div of two numbers",rem_of_num)

choice = input("Enter the operations: (Options + , - , * , / , %) ")

if choice == "+":
    print("addition: ",sum_of_num)
elif choice == "-":
    print("substraction: ",diff_of_num)
elif choice == "*":
    print("multiplication: ",prod_of_num)
elif choice == "/":
    print("division: ",div_of_num)
elif choice == "%":
    print("modulus: ",rem_of_num)
else:
    print("Invalid choice")
