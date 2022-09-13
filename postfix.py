#referencia de la idea https://blog.cernera.me/converting-regular-expressions-to-postfix-notation-with-the-shunting-yard-algorithm/

from thompson_v2 import *

stack =[]
output = []

def transform_postfix(c):
    print(c)
    for l in c:
        if l == "|" or l == "(" or l == ")" or l == "*" or l == "?":
            stack.append(l)
            if ")" in stack:
                output.append(stack[stack.index(")")-1])
                stack.pop(stack.index(")")-1)
                stack.remove("(")
                stack.remove(")")
            if l == "?":
                if "*" in stack:
                    output.append(stack[stack.index("*")])
                    stack.pop(stack.index("*"))
                elif "?" in stack:
                    output.append(stack[len(stack)-1])
                    stack.pop(len(stack)-1)             
        else:
            output.append(l)
            
    while(len(stack) > 0):
        output.append(stack[len(stack)-1])
        stack.pop(len(stack)-1)       
    
    # print("output: " + str(output))
    # print("stack: " + str(stack))
    
    #convertir el postfix a afd
    construccion_thompson(output)
