#Name: Robert Christain Horne
#Date: October 6 2025
#Filename: loanschedule.py

#This program will create a loan schedule for the user based on the data they have entered.
#The program will calculate and create a table to show the payment ammount.

#Imports module to for files.
import os
import math

#Initializing Variables
#Using a constant for months in a year.
MONTHS_IN_A_YEAR = 12
#Variables used in calculations.
loanAmount = 0.0
loanYears = 0
annualRate = 0.0
numMonths = 0
monthlyRate = 0.0
monthlyPayment = 0.0
beginBalance = 0.0
interestAmount = 0.0
principalAmount = 0.0
endBalance = 0.0
paymentAmount = 0
#Variables used for user inputs.
userAnswer = ""
fileName = ""
replaceFile = ""
#Boolean flag for the text file.
fileFinished = False

#Program asks the user to input their loan ammount they want,
#   how long they want the loan for, and the interest rate the loan is set at.
loanAmount = float(input("Enter the ammount you wish to borrow: "))
loanYears = int(input("Enter the number of years for the loan: "))
annualRate = float(input("Enter the yearly interest rate: "))

#Asks the user if they would like to create a text file of the loan schedule.
userAnswer = input("\nWould you like to create a text file of the loan schedule (Y/N)? ")
#Changes the answer to uppercase.
userAnswer = userAnswer.upper()

#If the user answers "Yes", then this loop will occur.
if userAnswer == "Y":
    #A boolean flag set for the loop.
    fileFinished = False
    while fileFinished == False:
        #Asking the user to input a file name without the extention. 
        #The program will add ".txt" to the textfile by default.
        fileName = input("Enter the text file's name without extention: ")
        fileName = fileName + ".txt"

        #if the filename already exists the program will let the user know and ask if they want to replace it.
        if os.path.exists(fileName):
            replaceFile = input("File name already exists. Want to replace it (Y/N)? ")
            #Changes the answer to uppercase.
            replaceFile = replaceFile.upper()

            if replaceFile == "Y":
                #Sets the flag to true to break the loop.
                fileFinished = True
                print("")
            #If the user says no to replacing the filename, then the program will ask them to choose another name.    
            else:
                print("Please enter a new filename.\n")
        else:
            #Sets the flag to true to break the loop.
            fileFinished = True
            print("")


#Calculations for total months of the loan and the monthly rate.
numMonths = loanYears * MONTHS_IN_A_YEAR
monthlyRate = annualRate / 100 / MONTHS_IN_A_YEAR

#Calculations for the monthly payment of the loan.
#Will factor in if the monthly rate is set to 0% or not.
if monthlyRate == 0:
    monthlyPayment = loanAmount / numMonths
else:
    monthlyPayment = (loanAmount * monthlyRate) / (1 - math.pow((1 + monthlyRate), -numMonths))

#Displays the monthly payment to the user.
print(f"The monthly payment is: ${monthlyPayment:.2f}.\n")

#Prints the headers for the table.
print("  Pmt#    Beg Balance    Payment    Interest    Principle    End Balance")

#If the user wrote a text file, then this condition will occur.
if userAnswer == "Y":
    #The program will open the text file to write the following.
    outfile = open(fileName, "w")
    outfile.write(f"For a loan of ${loanAmount:.2f}, for {loanYears} years")
    outfile.write(f" with an annual interest rate of {annualRate:.1f}%,\n")
    outfile.write(f"the monthly payment is ${monthlyPayment:.2f}.\n")
    #Headers for the table.
    outfile.write(f"  Pmt#    Beg Balance    Payment    Interest    Principle    End Balance\n")

#Sets the balance to the loan amount.
beginBalance = loanAmount

#A "for" loop to calculate and create the table based on the total months for the loan.
for paymentNumber in range(1, numMonths + 1):
    #Calculations for the interest and principal for the current month in the table.
    interestAmount = beginBalance * monthlyRate
    principalAmount = monthlyPayment - interestAmount

    #Adjusts the loan payments so they end with 0.
    if paymentNumber == numMonths:
        principalAmount = beginBalance
        monthlyPayment = interestAmount + principalAmount

    #Calculations for the remaining balance.
    endBalance = beginBalance - principalAmount   

    #Displays the text for the table.
    #The program will write the table based on the programed spacing and decimal limits.
    print(f"{paymentNumber:6d}{beginBalance:15.2f}{monthlyPayment:12.2f}{interestAmount:12.2f}{principalAmount:12.2f}{endBalance:15.2f}\n") 

    #If the user has a textfile, then the program will write the tableline into the textfile.
    if userAnswer == "Y":
        outfile.write(f"{paymentNumber:6d}{beginBalance:15.2f}{monthlyPayment:12.2f}{interestAmount:12.2f}{principalAmount:12.2f}{endBalance:15.2f}\n")

    #Resets the balance for the loop.
    beginBalance = endBalance

#Displays to the user that the file was created if yes is answered
if userAnswer == "Y":
    #Closes the file.
    outfile.close()
    print("\nThe file " + fileName + " has been written.")

#Keeps the program from immediately shutting down upon finishing.
input("Press Enter to exit.")