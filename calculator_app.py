# Task 1: Create functions for each arithmetic operation, with parameters for two numbers to be used in the operation. 


def add(a,b):
    return (int(a) + int(b))

# print(f"Testing addition function: {add(2,3)}\n Should return 5")

#------------------------
def sub(a,b):
    return (int(a) - int(b))

# print(f"Testing subtraction function: {sub(7,3)}\n Should return 4")

#------------------------
def multi(a,b):
    return (int(a) * int(b))

# print(f"Testing multiplication function: {multi(2,3)}\n Should return 6")

#------------------------

def divi(a,b):

    try:
        answer = (int(a)/int(b))
        message = print(f"{a} / {b} = {answer}")
        return message
        
    except ZeroDivisionError:
        print("="*50)
        print("CANNOT DIVIDE NUMBERS BY 0 !")
        print("="*50)
        calculate()
   

# print(f"Testing division function: {divi(8,4)}\n Should return 2.0")

# print("="*50)



# Task 2: Implement user input to receive numbers and an operation choice, their response for operation should call the associated function

def calculate():

    while True:
        try: #Testing block of code for errors

            num1 = int(input("Enter 2 numbers:\nnum1: "))
            num2 = int(input("num2: "))

        except ValueError: #let's you handle error
            print("="*50)
            print("ENTER NUMBERS ONLY\n")
            pass

        else:

            while True: 
            
                choice = input("Would you like to add(+), subtract(-), divide(/) or multiply(*) these two numbers?\nEnter the correct symbol for your arithmetic operation: ")

                if (choice == "+"):
                    print(f"{num1} + {num2} = {add(num1,num2)}")
                    break
                elif (choice == "-"):
                    print(f"{num1} - {num2} = {sub(num1,num2)}")   
                    break
                elif (choice == "*"):
                    print(f"{num1} * {num2} = {multi(num1,num2)}")
                    break
                elif(choice == "/"):
                    divi(num1,num2)
                    break
                else:
                    print("="*50)
                    print("\nPlease follow the prompt!\n")
                    pass
            break
calculate() 



