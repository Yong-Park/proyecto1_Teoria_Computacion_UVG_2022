#referencia de la idea https://blog.cernera.me/converting-regular-expressions-to-postfix-notation-with-the-shunting-yard-algorithm/

from operator import index
from thompson_v2 import *

stack =[]
output = []

def transform_postfix(c):
    print(c)
    for l in c:
        # print("====================")
        # print(l)
        # print("s: " + str(stack))
        # print("o: " + str(output))
        if l == "|" or l == "(" or l == ")" or l == "*" or l == "?":
            stack.append(l)

            if l == ")":
                a = len(stack)-2
                while(stack[a] != "("):
                    output.append(stack[a])
                    stack[a]=""
                    a = a-1
                stack[a] = ""
                stack[stack.index(")")] = ""
                while "" in stack:
                    stack.remove("")
            elif l == "?":
                try:
                    if len(stack) > 1:
                        # print("====================")
                        # print("verdadero")
                        # print("s: " + str(stack))
                        # print("====================")
                        if stack[len(stack)-2] == "*":
                            output.append(stack[len(stack)-2])
                            stack.pop(len(stack)-2)
                        elif stack[len(stack)-2] == "?":
                            output.append(stack[len(stack)-1])
                            stack.pop(len(stack)-1)
                except:
                    pass
            elif l == "|":
                try:
                    if len(stack) > 1:
                        if stack[len(stack)-2] == "*":
                            output.append(stack[len(stack)-2])
                            stack.pop(len(stack)-2)
                        elif stack[len(stack)-2] == "?":
                            output.append(stack[len(stack)-2])
                            stack.pop(len(stack)-2)
                        elif stack[len(stack)-2] == "|":
                            output.append(stack[len(stack)-1])
                            stack.pop(stack[len(stack)-1])
                except:
                    pass
            elif l =="*":
                try:
                    if len(stack) > 1:
                        if stack[len(stack)-2] == "*":
                            output.append(stack[len(stack)-1])
                            stack.pop(stack[len(stack)-1])
                except:
                    pass
                         
        else:
            output.append(l)
    while(len(stack) > 0):
        output.append(stack[len(stack)-1])
        stack.pop(len(stack)-1)

    # print("output: " + str(output))
    # print("stack: " + str(stack))
    
    #convertir el postfix a afd
    return output
