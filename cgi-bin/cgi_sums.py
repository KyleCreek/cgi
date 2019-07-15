#!/usr/bin/env python
import cgi
import cgitb
import os

cgitb.enable()

print("Content-type: text/plain")
print()
print("Your job is to make this work")

# Create an instance of the field storage Class
form = cgi.FieldStorage()

# Obtain a list of the operands
operands = form.getlist('operand')
print(operands)

# Calculate the Totals
try:
    #total = sum(map(int, operands))
    # Define initial Total
    total = 0 
    for value in operands:
        # Change String Value to Integer when adding
        total = total + int(value)
    body = "Your total is: {}".format(total)
except (ValueError, TypeError):
    body = "Unable to calculate a sum: please provide integer operands."

# Display the content to the users.
print("Content-type: text/plain")
print()
print(body)