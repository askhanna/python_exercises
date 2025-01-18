def areBracketsBalanced(expr):
    stack = []

    for char in expr:
        if char in ("(","{","["):
            stack.append(char)

        else:
            if not stack:
                print(char)
                return False
            
            current_char = stack.pop()

            if current_char == "(":
                if char != ")" :
                    return False
                
            if current_char == "{":
                if char != "}" :
                    return False
                
            if current_char == "[":
                if char != "]" :
                    return False
                
    # check empty stack
    if stack:
        print("1")
        return False
    return True

# driver code

if __name__ == "__main__":
    expr = "{()}[]]"

    # Function call
    if areBracketsBalanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")



                
                
