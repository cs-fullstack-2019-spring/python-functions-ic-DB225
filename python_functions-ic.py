def main():
    #problem1()
    #problem2()
    #problem3()
    #problem4()
    #challenge()

#PROBLEM1
#Create a variable named favoriteTeacher and assign it "Kevin".
# Send the favoriteTeacher variable to a function that will display the item when something is sent to it.
def problem1():
    favoriteTeacher = "Kevin"
    favoriteTeacherFunction(favoriteTeacher)
def favoriteTeacherFunction(teacher):
    print(teacher)

################################################################################################################
#PROBLEM2
#Create a function that has a loop that quits with ‘q’.
# If the user doesn't enter 'q', ask them to input another string.
def problem2():
    userInput = ""
    while(userInput != "q"):
        userInput = input("Put a string: ")

################################################################################################################
#PROBLEM3
#Create a sumOf3Numbers function that will print out the sum of the three numbers using the starting code below:
#sumOf3Numbers(number1, number2, number3)
def problem3():
    print(sumOfNumbers(1,2,3))
def sumOfNumbers(number1,number2,number3):
    return number1+number2+number3
################################################################################################################
#PROBLEM4
#Create a function that’s passed a name and the number of times a user wants to print Hello [NAME].
# Print Hello [NAME] that many times in the function.
def problem4():
    greetingAndName("Didier",3)
def greetingAndName(name,number):
    for eachEl in range(number):
        print(f"Hello{eachEl}")



################################################################################################################
#CHALLENGE
#Create a function that’s passed an array and a string and returns the new updated array.
# Create another function that’s passed two integers and returns the difference.
# Create a third function that’s passed an integer array and prints it.
def challenge():






if __name__ == '__main__':
    main()