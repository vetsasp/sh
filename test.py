

def parse(cmd):
    res = []
    escapeCharacter = False
    escapeSingeQuote = False
    escapeDoubleQuote = False
    word = ''
    for c in cmd:
        if c == '\\' and not escapeDoubleQuote and not escapeSingeQuote:
            escapeCharacter = True
        elif escapeCharacter:
            word = word + c
            escapeCharacter = False
        elif c == "'" and not escapeDoubleQuote:
            escapeSingeQuote = not escapeSingeQuote
        elif c == '"' and not escapeSingeQuote:
            escapeDoubleQuote = not escapeDoubleQuote
        elif escapeSingeQuote or escapeDoubleQuote:
            word = word + c
            # print(f"'{word}'")
        elif isWhitespace(c):
            if word:
                res.append(word)
                word = ''
        else:
            word = word + c

    res.append(word)
    return res

def isWhitespace(c):
    return c in {" ", "\t", "\n"} 

def test():
    case1 = "echo hello world"
    case2 = "echo 'hello there' world"
    case3 = "echo 'before\     after'"
    case4 = 'echo world\ \ \ \ \ \ script'
    case5 = 'echo "world  shell"  "script"'

    cases = [case1, case2, case3, case4, case5]
    for i, case in enumerate(cases):
        print(f"case {i+1}: {parse(case)}")


if __name__ == "__main__":
    # test() 
    case5 = 'echo "world  shell"  "script"'
    res = parse(case5)
    print(res)
    print(res[1])