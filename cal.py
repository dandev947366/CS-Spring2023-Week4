def cal(n1, n2, choice):
    if choice == '+':
        return n1 + n2
    elif choice == '-':
        return n1 - n2
    elif choice == '*':
        return n1 * n2
    elif choice == '/':
        return n1 / n2
    else:
        return "Choose between + - * /"

print(cal(2,5,"*"))
