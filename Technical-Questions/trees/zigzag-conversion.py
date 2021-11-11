# INPUT: A string of ASCII characters, Number of rows for zig zag conversion
# OUTPUT: String after zig zag conversion
# INFO: Zig zag conversion organises string into columns (with specific number of rows) and diagonals connecting columns

# Length of diagonal section between columns = number of rows - 2

def convert(s: str, numRows: int) -> str:
    matrix = [[] for _ in range(numRows)]
    index = 0
    diagonal_traversal = False

    for char in s:
        print("Appended ", char, "into index ", index)
        matrix[index].append(char)
        if ((index + 1) % numRows == 0):
            diagonal_traversal = True
        elif (index == 0):
            diagonal_traversal = False
        if diagonal_traversal:
            index -= 1
        else:
            index += 1

    final_string = "".join(sum(matrix, []))
    return final_string


def main():
    print(convert("MICHAEL", 3))


if __name__ == '__main__':
    main()
