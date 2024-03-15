#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      feloe
#
# Created:     15/03/2024
# Copyright:   (c) feloe 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
password = input("Enter a password : ")

while password != 'Pass123':
    password = input("Enter a password : ")
    print("Incorrect Password!")
print('Correct!!!. Welcome Admin!')