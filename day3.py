def isValid(s):
    checked_string = list()
    for e in s:
        if e == '(' or e == '[' or e == '{':
            checked_string.append(e)
        else:
            if len(checked_string) == 0:
                return False
            if e == ')':
                tested_char = checked_string.pop()
                if tested_char != '(':
                    return False
            elif e == ']':
                tested_char = checked_string.pop()
                if tested_char != '[':
                    return False
            elif e == '}':
                tested_char = checked_string.pop()
                if tested_char != '{':
                    return False
    return True



def main():
    s ="()[]{}"
    print(isValid(s))

if __name__ == "__main__":
    main()
