
#Greeting
print ('Hello! I will be your personal online calculator for today!')


def get_y(choice):
    y = int(input('Please enter another number: '))

    """
    So basically whats happening here is we are making sure that if the user chooses division that the second number (The number being divided by) is not 0.
    """
    if choice == "division" and y <= 0: #This line says if the choice is divison AND if y is less than or equal to 0 then ask for the y input again
        
        # I made a while loop here cause the stupid user might enter 0 again ang again so until the fool enters the right value keep them in the loop
        while y <= 0:
            y = int(input('This is not a valid entry, please enter another number: '))
    return y


def get_x():
    x = int(input('Please enter a number: '))
    return x
    


#User enters two numbers to get the sum 
def Addition(x, y):
    total = (x + y)
    return total

#User enters two numbers to get the difference              
def Subtraction(x, y):
    total = (x - y)
    return total

#User enters two numbers to get the product 
def Multiplication(x, y):
    total = (x * y)
    return total

#User enters two numbers to get the quotient
def Divison (x, y):
    total = (x / y)
    return total
        

choice = "addition"
while choice != "quit":

    #User picks which operation they would like to complete 
    print('Please Choose An Option')
    choice=input('addition, subtraction, multiplication, division or quit: ')
    
    # If the choice is quit then break the loop right away and end the program
    if choice == "quit":
        break

    """
    You should ask the user for the two inputs before hand because then you don't have to repeat this code in every single function
    You can instead just pass the parameters; num1 and num1 to every function
    """
    print("You chose %s" % (choice))


    """
    The reason I made this variable is so that if the user enters the wrong choice it tells our program not to
    Show the total
    """
    show_total = True

    # Now you can choose the operation you want and get back the right value 
    if choice == 'addition':
        x = get_x()
        y = get_y(choice)
        total = Addition(x, y)
    elif choice == 'subtraction':
        x = get_x()
        y = get_y(choice)
        total = Subtraction(x, y)
    elif choice == 'multiplication':
        x = get_x()
        y = get_y(choice)
        total = Multiplication(x, y)
    elif choice == 'division':
        x = get_x()
        y = get_y(choice)
        total = Divison(x, y)
    else:
        print("Hmmm, that't not an option. Please enter from the given choices.")
        show_total = False # we don't want to show the total anymore cause there is NONE !!


    if show_total: # only show if we want to
        # Print the right value
        print("The %s of %s and %s is %s" % (choice, x, y, total))
    
