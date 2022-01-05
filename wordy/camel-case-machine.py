import sys
result = ""
first = True
count = 0
for line in sys.stdin:
    # print(line, " at ", count)
    # count += 1
    if line == "\n":
        result += " "
        first = True
    else:
        stripped = line.rstrip("\n")
        if first:
            result += stripped.lower()
            first = False
        else:
            result += stripped.capitalize()
print(result, end="")


"""
Lines are parsed such that newline is appended to end of line if there is one
Spaces between lines are then parsed as \n\n strings
"""
