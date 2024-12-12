

def parse(cmd):
    res = []
    escapeCharacter = False
    escapeSingeQuote = False
    escapeDoubleQuote = False
    word = ''
    for c in cmd:
        print(f"{word}: '{c}'")
        if escapeCharacter:
            print('escape')
            if escapeDoubleQuote and c not in {'\\', '$', '"'}:
                word = word + '\\'
            word = word + c
            escapeCharacter = False
        elif c == '\\' and not escapeSingeQuote:
            escapeCharacter = True
        elif c == "'" and not escapeDoubleQuote:
            escapeSingeQuote = not escapeSingeQuote
        elif c == '"' and not escapeSingeQuote:
            escapeDoubleQuote = not escapeDoubleQuote
        elif escapeSingeQuote:
            word = word + c
        elif escapeDoubleQuote:
            word = word + c
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

case1 = "echo hello world"
case2 = "echo 'hello there' world"
case3 = "echo 'before\     after'"
case4 = 'echo world\ \ \ \ \ \ script'
case5 = 'echo "world  shell"  "script"'
case6 = 'echo "foo\\\'f \\60"'

cases = [case1, case2, case3, case4, case5, case6]

def test():
    for i, case in enumerate(cases):
        print(f"case {i+1}: {parse(case)}")


if __name__ == "__main__":
    # test() 
    res = parse(case6)
    print(res)
    print(res[1])