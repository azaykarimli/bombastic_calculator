import os
import sys
from multiprocessing import Process, Pipe
 

def calculate(init_result, num1,num2,operator):
    if operator == "P":
        result = num1 + num2
    elif operator == "M":
        result = num1-num2
    elif operator == "T":
        result = num1*num2
    elif operator == "D":
        result = num1/num2
    return result + init_result

def first(pipe):
    sys.stdin = open(0)
    num1 = float(input("Enter First Integer:"))
    num2 = float(input("Enter Second Integer:"))
    print("select operation: \nP - add \nM - substract\nT - multiply\nD - divide")
    operator = input("Enter operation (P, M, T, D) ").upper()
    result = calculate(init_result=0, num1=num1,num2=num2, operator=operator)
    pipe.send(result)
    pipe.close()
 
def second(pipe):
    sys.stdin = open(0)
    num1 = float(input("Enter First Integer:"))
    num2 = float(input("Enter Second Integer:"))
    print("select operation: \nP - add \nM - substract\nT - multiply\nD - divide")
    operator = input("Enter operation (P, M, T, D) ").upper()
    result = calculate(init_result=0, num1=num1,num2=num2, operator=operator)
    # print(result)
    pipe.send(result)
    pipe.close()
    

def third(pipe):
    sys.stdin = open(0)
    num1 = float(input("Enter First Integer:"))
    num2 = float(input("Enter Second Integer:"))
    print("select operation: \nP - add \nM - substract\nT - multiply\nD - divide")
    operator = input("Enter operation (P, M, T, D) ").upper()
    result = calculate(init_result=0, num1=num1,num2=num2, operator=operator)
    # print(result)
    pipe.send(result)
    pipe.close()

def fourth(pipe):
    sys.stdin = open(0)
    num1 = float(input("Enter First Integer:"))
    num2 = float(input("Enter Second Integer:"))
    print("select operation: \nP - add \nM - substract\nT - multiply\nD - divide")
    operator = input("Enter operation (P, M, T, D) ").upper()
    result = calculate(init_result=0, num1=num1,num2=num2, operator=operator)
    # print(result)
    pipe.send(result)
    pipe.close()
 
if __name__ == '__main__':
    (con1, con2) = Pipe() 
    first = Process(target = first, name = 'first', args = (con1, ))
    first.start()
    result_first = con2.recv()
    print("first got: %s" % result_first)#Receive message from send
    con2.close()

 
    (parentEnd, childEnd) = Pipe()
    second = Process(target = second, name = 'second', args = (childEnd,))
    second.start()
    result_second = int(parentEnd.recv())+ result_first
    print('second got:'+str(result_second))
    childEnd.close()

    (parentEndThird, childEndThird) = Pipe()
    third = Process(target = third, name = 'third', args = (childEndThird,))
    third.start()
    result_third = int(parentEndThird.recv()) + result_second
    childEndThird.close()

    (parentEnd4, childEnd4) = Pipe()
    fourth = Process(target = fourth, name = 'fourth', args = (childEnd4,))
    fourth.start()
    result_fourth = int(parentEnd4.recv()) + result_third
    childEnd4.close()

    print("TOTAL: "+str(result_fourth))

