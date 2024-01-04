def isValid(s: str) -> bool:
    stack = []
    for i in s:
        if i == "(" or i == "{" or i == "[":
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            elif i == ")" and stack[-1] == "(":
                stack.pop()
            elif stack[-1] == "[" and i == "]":
                stack.pop()
            elif stack[-1] == '{' and i == "}":
                stack.pop()
            else:
                return False
    return not stack


print(isValid(s="()"))
print(isValid(s = "()[]{}"))
print(isValid(s = "(]"))