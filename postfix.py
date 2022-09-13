
stack =[]
output = []

# Closure (Kleene star) a*
# Concatenation ab
# Union a+b

# "(b|b)*?a?b?b?(a|b)*"

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
    
    print("output: " + str(output))
    print("stack: " + str(stack))

    return 1