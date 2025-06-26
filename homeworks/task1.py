# Prints given string to the output console
print("Task: Print given string to the output console")
print("Mehdi Nuruzade")
print("")

# Data types
print("Task: Display types")
name = "Vasif Ismayilov"
age = 23
student = True
print(type(name), type(age), type(student))
print("")

# Data types
print("Task: Data types")
max_speed = 270
engine_size = 3.7
make = "Nissan"
model = "370Z"
is_running = True
print("Make:", make)
print("Model:", model)
print("Engine Size:", engine_size)
print("Max Speed:", max_speed)
print("Engine Is Running:", is_running)
print("")

# Type conversion from a string
int("42")
float("3.14")

# Takes user input and prints the input
print("Task: Displaying user input")
name = input("What is your name? ")
print("Hello", name)
print("")

# Finding index
print("Task: Finding index")
the_sentence = "Salam dünya"
print("The index for 'dünya' is :",the_sentence.find("dünya"))
print("The index for 'd' is :",the_sentence.index("d"))
print("")

# Capitalizing and Titling given sentence
print("Task: Capitalizing and Titling given sentence")
the_word = "salam"
print("The capitalized version :",the_word.capitalize())
print("The titled version: ",the_word.title())
print("")

#Finding length for a given sentence
print("Task: Finding length for a given sentence")
print("Length for 'Python öyrənmək maraqlıdır' is :",len("Python öyrənmək maraqlıdır"))
print("")

#Arithmetic operations for a and b
print("Task: Arithmetic operations for a and b" )
num_1 = 5
num_2 = 2
print("Addition operation for",num_1,"and",num_2,"is :",num_1+num_2)
print("Subtraction operation for",num_1,"and",num_2,"is :",num_1-num_2)
print("Multiplication operation for:",num_1,"and",num_2,"is :",num_1*num_2)
print("Division operation for",num_1,"and",num_2,"is :",num_1/num_2)
print("Floor division operation for",num_1,"and",num_2,"is :",num_1//num_2)
print("Modulus operation for",num_1,"and",num_2,"is :",num_1%num_2)
print("Exponentiation operation for",num_1,"and",num_2,"is :",num_1**num_2)
print("")

# Convertion a word to upper and lower case
print("Task: Convertion a word to upper and lower case")
print("Upper case operation for 'python' is","python".upper())
print("Lower case operation for 'python' is","python".lower())
print("")

#Arithmetic operations for a and b
print("Task: Arithmetic operations for a and b")
a = 12
b = 4
print("Addition operation for",a,"and",b,"is :",a+b)
print("Subtraction operation for",a,"and",b,"is :",a-b)
print("Multiplication operation for",a,"and",b,"is :",a*b)
print("Floor division operation for",a,"and",b,"is :",a/b)
print("Modulus operation for",a,"and",b,"is :",a%b)
print("Exponentiation operation for",a,"and",b,"is :",a/b)
print("")

# User input operations (Bonus Tasks)
print("Task: User input operations (Bonus Tasks)")
user_name = input("What is your full name? ")
print(user_name.capitalize())
print("Length for username is: ",len(user_name))
print("")

# Slicing with user input (Bonus Task)
print("Task: Slicing with user input (Bonus Task)")
user_input = input("Enter any sentence: ")
print(user_input[0:5]+user_input[-5:])
print("")

# Slicing with full name (Bonus Task)
print("Task: Slicing with full name (Bonus Task)")
full_name = input("Enter your full name: ")
print(full_name[0:3]+full_name[-2:])
print("")

# User input average float calculation (Bonus Task)
print("Task: User input average float calculation (Bonus Task)")
input_1 = float(input("Enter first number: "))
input_2 = float(input("Enter second number: "))
average = (input_1 + input_2) / 2
print("The average for given numbers is: ",average)
print("The type for result is: ",type(average))
print("")

# User input string modification (Bonus Task)
print("Task: User input string modification (Bonus Task)")
user_input2 = input("Enter any sentence: ")
print("Upper case version for the given input is: ",user_input2.upper())
print("Lower case version for the given input is: ",user_input2.lower())
print("Capitalized version for the given input is: ",user_input2.capitalize())
print("")

# User input operations (Bonus Task)
print("Task: User input operations (Bonus Task)")
user_input3 = input("Enter some input: ")
print("Length for input is: ",len(user_input3))
print("Type for input is: ",type(user_input3))
print("The first 3 letters for input is: ",user_input3[0:3])
print("")

# Age Calculation
print("Task: Age Calculation (Bonus Task)")
current_year = int(input("Enter current year: "))
birth_year = int(input("Enter birth year: "))
age = current_year - birth_year
print("Your age is:",age)
print("Output type is: ",type(age))
print("")

# Finding middle letter for a sentence
print("Task: Finding middle letter for a sentence (Bonus Task)")
user_input4 = input("Enter a sentence: ")
middle_index = len(user_input4)//2
print("Middle character for the given input is: ",user_input4[middle_index])
print("")

# Applying .title() method and finding first space
print("Task: Applying .title() method and finding first space (Bonus Task)")
user_input5 = input("Enter a sentence: ")
print("Titled version for the given input is: ",user_input5.title())
print("First occurrence for the space character is: ",user_input5.find(' '))
print("")

# Combining user inputs
print("Task: Combining user inputs (Bonus Task)")
user_input_name = input("Enter your name: ")
user_input_age = int(input("Enter your age: "))
user_input_occupation = input("Enter your occupation: ")
print("My name is",user_input_name,". I am",user_input_age,"years old.","My occupation is",user_input_occupation,".")
