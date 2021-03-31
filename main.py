
def checkIfInt(userNumber):
    while True:
        try:
            return int(input(userNumber))
        except:
            print("Not an integer!")
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
        print number
