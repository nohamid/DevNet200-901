message = input("Enter your name:")
print (f"Yor Name is {message}")

age = input("Enter your age:")
age = int(age)
if age >= 18:
    print("You can vote")
else: 
    print("You are too young to vote!")

number = 1
while number <=10:
    print(f"number is {number}")
    number +=1

prompt = "\n Tell me something:"
prompt += "\n Enter 'quit to end the program"

message = ""

while message != 'quit':
    message = input(prompt)
    print (message)

