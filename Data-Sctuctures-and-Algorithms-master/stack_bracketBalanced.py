from stack import  Stack

def isMatch(open, close):
    if open == "(" and close == ")":
        return True
    elif open == "{" and close == "}":
        return True
    elif open == "[" and close == "]":
        return True
    else:
        return False

def isBalanced(paraStr):
    s = Stack()
    balalnced = True
    index = 0

    while index < len(paraStr) and balalnced:
        paren = paraStr[index]
        if paren in '{[(':
            s.push(paren)
        else:
            if s.is_empty():
                balalnced = False
                break
            else:
                top = s.pop()
                if not isMatch(top, paren):
                    balalnced = False
                    break
        index+=1

    if s.is_empty() and balalnced:
        return True
    else:
        return False


print(isBalanced("(((({})))"))
