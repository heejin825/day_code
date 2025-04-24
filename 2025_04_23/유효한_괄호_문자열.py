def is_valid_parentheses(s):
    stack = []
    for char in s:
        if char == '(' :
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

print(is_valid_parentheses("()"))
print(is_valid_parentheses("()(())"))
print(is_valid_parentheses("())())"))
