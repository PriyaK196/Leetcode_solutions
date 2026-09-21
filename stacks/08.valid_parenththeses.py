# Test Case 1
s1 = "()[]{}"
stack1 = []
valid1 = True

for c in s1:
    if c == '(' or c == '[' or c == '{':
        stack1.append(c)
    else:
        if len(stack1) == 0:
            valid1 = False
            break

        open_bracket = stack1.pop()

        if ((c == ')' and open_bracket != '(') or
            (c == ']' and open_bracket != '[') or
            (c == '}' and open_bracket != '{')):
            valid1 = False
            break

if len(stack1) != 0:
    valid1 = False

print("Test Case 1:", str(valid1).lower())


# Test Case 2
s2 = "(]"
stack2 = []
valid2 = True

for c in s2:
    if c == '(' or c == '[' or c == '{':
        stack2.append(c)
    else:
        if len(stack2) == 0:
            valid2 = False
            break

        open_bracket = stack2.pop()

        if ((c == ')' and open_bracket != '(') or
            (c == ']' and open_bracket != '[') or
            (c == '}' and open_bracket != '{')):
            valid2 = False
            break

if len(stack2) != 0:
    valid2 = False

print("Test Case 2:", str(valid2).lower())