from stack import Stack

def decimal2Binary(decimal):
    s = Stack()
    count = 0
    binary = ""

    while decimal > 0:
        s.push(decimal%2)
        decimal //= 2
        count+=1

    while not s.is_empty():
        binary += str(s.pop())

    return binary

print(decimal2Binary(int(input())))
