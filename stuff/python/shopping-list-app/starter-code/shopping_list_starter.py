#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

choice = ""

print("Welcome to the shopping list app!")

shopping_list = []

def printMenu():
    print("Please choose your action from the following list:")
    print("a. Add an item to the list")
    print("b. Remove an item from the list")
    print("c. Check to see if an item is on the list")
    print("d. Show all items on the list")
    print("e. exit")

def addItem(stuff):
    shopping_list.append(stuff)

def removeItem(stuff):
    shopping_list.remove(stuff)

printMenu()
while choice.lower() != "e":
    choice = raw_input("Enter your choice [a|b|c|d|e], help for menu:")
    if choice.lower() == "a":
        item = raw_input("Enter the item to add: ")
        item = item.strip()
        item = item.split(',')
        for i in range(len(item)):
            strippedItem = item[i].strip()
            if strippedItem in shopping_list:
                print(str(strippedItem)+ " is already in the shopping list")
            else :
                shopping_list.append(strippedItem)
    elif choice.lower() == "d":
        print("List: "+ str(shopping_list))
    elif choice.lower() == "help":
        printMenu()
    elif choice.lower() == "b":
        item = raw_input("Enter the item to remove: ")
        if item in shopping_list:
            confirm = raw_input("Are you sure?")
            if confirm.lower() == "yes":
                removeItem(item)
        else:
            print("ITEM ISN'T IN THE LIST DUMMY, check spelling")
    elif choice.lower() == "c":
        item = raw_input("Enter the item to check: ")
        if item in shopping_list:
            action = raw_input("Item is in the list, would you like to remove it?")
            if action.lower() == "yes":
                removeItem(item)
        else:
            action = raw_input("Item is not in the list, would you like to add it?")
            if action.lower() =="yes":
                addItem(item)




    # Your code below! Handle the cases when the user chooses a, b, c, d, or e
