def greater(a, b):
    return a > b

def less(a, b):
    return a < b

# aList: unsorted list
# op: a function that takes two arguments and returns a boolean
def bubbleSort(aList, op):
    for passnum in range(len(aList)-1, 0, -1):
        for i in range(0, passnum, 1):
            j = i + 1
            if op(aList[i],  aList[j]):
                temp = aList[i]
                aList[i] = aList[j]
                aList[j] = temp
    return aList



def doYourHomework():
    print('Do your homework!!!')

def discordYourBuddy():
    print('Discord your buddy!!!')

import time

def reminderAfterNSeconds(n, callback):
    time.sleep(n)
    callback()

reminderAfterNSeconds(2, doYourHomework)
reminderAfterNSeconds(3, discordYourBuddy)