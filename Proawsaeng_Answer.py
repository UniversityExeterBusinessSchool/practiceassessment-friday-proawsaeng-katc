#######################################################################################################################################################
# 
# Name:Proawsaeng Katcharoen
# SID:740094448
# Exam Date: 28 March 2025
# Module:BEMM458 Programming for Business Analytics
# Github link for this assignment:  https://github.com/UniversityExeterBusinessSchool/practiceassessment-friday-proawsaeng-katc.git
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Data Processing and Loops
# You are given a string representing customer reviews. Use a for loop to process the text and count occurrences of specific keywords.
# Your allocated keywords are determined by the first and last digit of your SID.
# Count and store occurrences of each keyword in a dictionary called keyword_counts.
 
customer_reviews = """The product is well-designed and user-friendly. However, I experienced some issues with durability. The customer service was helpful, 
but I expected a faster response. The quality of the materials used is excellent. Overall, the purchase was satisfactory."""

# Keywords dictionary
keywords = {
    0: 'user-friendly',
    1: 'helpful',
    2: 'durability',
    3: 'response',
    4: 'satisfactory',
    5: 'quality',
    6: 'service',
    7: 'issues', #mytarget1
    8: 'purchase',#mytarget2
    9: 'materials'
}

# Write your code to process the text and count keyword occurrences

keywords_counts = {}    #create new dictionary to store data

#locate each target using .find()
target1 = (customer_reviews.find('issues'), customer_reviews.find('issues') + len('issues'))
target2 = (customer_reviews.find('purchase'), customer_reviews.find('purchase') + len('purchase'))

#add key-value in the new dictionary
keywords_counts['issues_position'] = target1
keywords_counts['purchase_position'] = target2

print(keywords_counts)

##########################################################################################################################################################

# Question 2 - Business Metrics
# Scenario - You work in an online retail company as a business analyst. Your manager wants weekly reports on financial performance, including:
# Gross Profit Margin, Inventory Turnover, Customer Retention Rate (CRR), and Break-even Analysis. Implement Python functions 
# that take relevant values as inputs and return the computed metric. Use the first two and last two digits of your ID number as input values.

# Insert first two digits of ID number here:    74
# Insert last two digits of ID number here:     48

# Write your function for Gross Profit Margin

def GrossProfitMargin(revenue, price):
    return ((revenue - price) / revenue) * 100

# Write your function for Inventory Turnover

def InventoryTurnover(sales, avg_inventory):
    return sales / avg_inventory

# Write your function for Customer Retention Rate (CRR)

def CustomerRetentionRate(last_cust, new_cust, first_cust):
    return ((last_cust - new_cust) / first_cust) * 100

# Write your function for Break-even Analysis

def BreakEven (fixed_cost, sales_per_unit, variable_cost):
    return fixed_cost / (sales_per_unit - variable_cost)

#I'm declaring that I have used Ai to understand equations above.

# Call your functions here

print(f"Gross Profit Margin: {GrossProfitMargin(74,48):.2f}")
print(f"Inventory Turnover: {InventoryTurnover(74,48):.2f}")
print(f"Customer Retention Rate (CRR): {CustomerRetentionRate(74,48,48):.2f}")
print(f"Break-even Analysis: {BreakEven(74,48,74):.2f}")
#using .2f to make it to 2 decimals

##########################################################################################################################################################

# Question 3 - Forecasting and Regression
# A logistics company has gathered data on delivery costs and shipment volumes.
# The table below provides different costs and their corresponding shipment volumes.
# Develop a linear regression model and determine:
# 1. The optimal delivery cost that maximizes profit
# 2. The expected shipment volume when the cost is set at £68

"""
Delivery Cost (£)    Shipment Volume (Units)
-------------------------------------------
25                  500
30                  480
35                  450
40                  420
45                  400
50                  370
55                  340
60                  310
65                  290
70                  250
"""

# Write your regression model code here

import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
from sklearn.linear_model import LinearRegression

#create array for using in scikit
cost = np.array([25, 30, 35, 40, 45, 50, 55, 60, 65, 70]).reshape(-1, 1)
shipment = np.array([500, 480, 450, 420, 400, 370, 340, 310, 290, 250]).reshape(-1, 1)


mymodel = LinearRegression()
mymodel.fit(cost, shipment)

predict_shipment = mymodel.predict(np.array([[68]]))
print(f"The expected shipment volume when the cost is set at £68: {predict_shipment[0]}")

# Regression line
plt.scatter(cost, shipment, color='blue')
plt.plot(cost, mymodel.predict(cost), color='red')
plt.xlabel("Delivery Cost (£)")
plt.ylabel("Shipment Volume (Units)")
plt.title("Delivery Cost and Shipment Volume")
plt.show()

#The optimal delivery cost that maximizes profit
optimal_cost = max(mymodel)
print(optimal_cost)

##########################################################################################################################################################

# Question 4 - Debugging and Data Visualization

import rand as random               #this is wrong, rand and random should switch position
import matplotlib.pyplt as plt      #this is wrong, typing wrong, it should be 'pyplot'

# Generate 100 random numbers between 1 and student ID number
your_ID=input("Enter your Student ID: ")
max_value = int(your_ID)
random_numbers = [random.randint(your_ID, max_valu) in range(100)]      #this is wrong, there are some misspelling of the value and wrong command from error before

# Plotting the numbers in a histogram
plt.histogram(random_number, bin=10, edgecolour='blue', alpha=0.7, colour='red')    #wrong value because of 
plt.title="Histogram of 100 Random Numbers"
plt.xlabel="Value Range"    #need to be parenthesis ()
plt.ylabel="Frequency"      #need to be parenthesis ()
plt.grid("True")            #No quotation
plt.show("plot")            #Should be just empty parenthesis ()

# Question 4 - Debugging and Data Visualization

#Below is the correct command
import random as rand
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student ID number

your_ID=input("Enter your Student ID: ")
max_value = int(your_ID)
random_numbers = [rand.randint(1, max_value) for i in range(100)]

#Correcting
plt.hist(random_numbers, bins=10, edgecolor='blue', alpha=0.7, color='red')
plt.title("Histogram of 100 Random Numbers")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()