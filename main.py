
def checkIfInt(userNumber):
    while True:
        try:
            userInput = int(input(userNumber))
            if userInput > 0:
                return userInput
            else:
                print("Not an positive integer!")
        except:
            print("Not an positive integer!")
            continue

# MAIN PROGRAM STARTS HERE:


userNumber = checkIfInt("Enter positive whole number: ")

for number in range(userNumber,0,-1):
    if (number % 5 == 0) and (number % 3 == 0):
        print ("Testing")
    elif number % 5 == 0:
        print ("Agile")
    elif number % 3 == 0:
        print ("Software")
    else:
        print (number)
