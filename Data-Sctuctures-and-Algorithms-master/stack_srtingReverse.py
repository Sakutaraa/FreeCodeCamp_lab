from stack import Stack

# Normal way to reverse the string
# print(input()[::-1])

# Using stack
def revStr(inpStr):
    s = Stack()
    for i in inpStr:
        s.push(i)

    revStr = ""
    for i in range(len(inpStr)):
        if not s.is_empty():
            revStr += s.pop()

    return revStr

print(revStr(input("Enter String: ")))
