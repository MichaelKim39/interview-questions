# INPUT - String containing only valid "brackets" [], {}, ()
# OUTPUT - True if every pair of brackets is matched False otherwise
# EXAMPLE
# {[()]} => YES

def isBalanced(word):
    stack = list()
    for char in word:
        if char in '({[':
            stack.append(char)
        else:
            lastBracket = stack.pop()
            switch(char) {
                case ')':
                    if lastBracket != '(': return False
                    break;
                case ']':
                    if lastBracket != '[': return False
                    break;
                case '}':
                    if lastBracket != '{': return False
                    break;}
    return True
