import collections
    
def balancedString(s):
    stack = collections.deque()
    bracketDict = collections.defaultdict()
    bracketDict['}'] = '{'
    bracketDict[']'] = '['
    bracketDict[')'] = '('
    prevTop = ''

    for char in s:
        if stack:
            prevTop = stack[-1]

        if char == '(' or char == '{' or char == '[':
            stack.append(char)
        elif bracketDict[char] == prevTop:
            stack.pop()
        else:
            return False

    if not stack:
        return True
    else:
        return False
        
print(balancedString("{{{}}}")) # True
print(balancedString("")) # True
print(balancedString("{[}]")) # False
print(balancedString("}}}")) # False
print(balancedString("{[()(")) # False
print(balancedString("{}[")) # False
