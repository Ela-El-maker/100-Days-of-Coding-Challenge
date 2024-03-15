#-------------------------------------------------------------------------------
# Name:        Making a TODO List
# Purpose:
#
# Author:      feloe
#
# Created:     15/03/2024
# Copyright:   (c) feloe 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

user_prompt = "Enter a todo: "
todos = []
while True:
    todo = input(user_prompt)
    todo.capitalize()
    todos.append(todo)
    print(todos)
    print("Next ...")
