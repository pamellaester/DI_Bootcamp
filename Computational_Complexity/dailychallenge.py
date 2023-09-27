expr = "(1 + 2) * {[(3 / 4) - 5]}"
def checks_balanced_parentheses(expr):
    
    parentheses = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    stack = []
    for p in expr:
        if p in parentheses.values():
            stack.append(p)    
        elif p in parentheses.keys():
            parentheses[p] == stack[-1]
            stack.pop()

    if stack.isempty():
        return

    # if len(stack) == 0:
    #     return True 
    # else:
    #     return False 

expr = "(1 + 2) * {[(3 / 4) - 5]}"

print(checks_balanced_parentheses(expr))




             