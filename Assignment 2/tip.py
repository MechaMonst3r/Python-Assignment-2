# Name: Luke Bowden
# Student Number: t00040951
# Lab Number: 2
# Date: 2020-09-24
# Description: Calculates tip based on customer satisfaction.

#Declaring constants and variables
TIP_ONE = 0.20;
TIP_TWO = 0.15;
TIP_THREE = 0.10;
ONE = 1;
TWO = 2;
THREE = 3;
totalTip = 0.00;

#Printing initial messages to the user.
print("Please use the following scale:");
print(" 1:Totally Satisfied");
print(" 2:Satisfied");
print(" 3:Dissatisfied");

#Prompting user to enter their satisfaction level.
userSatisfaction = int(input("What was your level of satisfaction?"));

#Continues to prompt user for a valid satisfaction level (1, 2, or 3) if they dont answer a proper level.
while userSatisfaction != ONE and userSatisfaction != TWO and userSatisfaction != THREE:
    print("Invalid entry. Try again.");
    userSatisfaction = int(input("Enter Satisfaction level:"));
                    
#Prompts user for input on their bill cost. Can be any number inluding decimal points.                    
userBill = float(input("How much was your bill?"));

#Calculates tip based on user satisfaction level, then prints appropriate message along with the tip amount.
if userSatisfaction == 1:
            totalTip = TIP_ONE * userBill;
            print("Because you were totally satisfied, your tip should be: $" + "{:.2f}".format(totalTip));  

if userSatisfaction == 2:
            totalTip = TIP_TWO * userBill;
            print("Because you were satisfied, your tip should be: $" + "{:.2f}".format(totalTip));
            
if userSatisfaction == 3:
            totalTip = TIP_THREE * userBill;
            print("Because you were dissatisfied, your tip should be: $" + "{:.2f}".format(totalTip));