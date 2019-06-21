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

# Replace "pass" with your code
import time
from time import gmtime, strftime, mktime, localtime
class BankAccount(object):

    def __init__(self, label, balance):
        self.label = label
        self.balance = balance
        self.transactions = []

    def __str__(self):
        result = self.label + str(self.balance)
        return result

    def lbl(self):
        return self.label

    def withdraw(self, amount):
        if amount < 0 :
            print("error")
        elif self.balance > amount:
            self.balance = self.balance - amount
            self.transactions.append(Transaction('withdraw', amount))
        elif self.balance < amount:
            print("not enough money in balance")

    def deposit(self, amount):
        if amount < 0:
            print("error")
        else:
            self.balance = self.balance + amount
            self.transactions.append(Transaction('deposit', amount))

    def rename(self, newLabel):
        if newLabel == '':
            print("label cannot be blank")
        else:
            self.label = newLabel

    def transfer(self, dest_account, amount):
        if amount < 0 :
            print("error")
        elif self.balance > amount:
            self.balance = self.balance - amount
            dest_account.balance = dest_account.balance + amount
            dest_account.transactions.append(Transaction("transfer_in", amount, self.lbl()))
            self.transactions.append(Transaction('transfer_out', amount, dest_account.lbl()))
        elif self.balance < amount:
            print("not enough money in balance")

    def showTransaction(self):
        for trans in self.transactions:
            print(trans)

class Transaction(object):

    def __init__(self, type, amount, dest_account=""):
        self.time = strftime("%a, %d %b %Y %H:%M:%S", localtime())
        self.type = type
        self.amount = amount
        self.dest_account = dest_account

    def __str__(self):
        if self.dest_account == "":
            return(str(self.time) + ": " + str(self.type) + " $" + str(self.amount))
        elif self.type == 'transfer_in':
            return(str(self.time) + ": " + str(self.type) + " $" + str(self.amount) + " from account " + str(self.dest_account))
        else:
            return(str(self.time) + ": " + str(self.type) + " $" + str(self.amount) + " to account " + str(self.dest_account))


account = BankAccount("my Account", 500)
account2 = BankAccount("Friend Account", 500)
account.transfer(account2, 200)
account.deposit(400)
account.withdraw(200)
account.showTransaction()
account2.showTransaction()
