from collections import defaultdict

# Print all positive solutions to a^3 + b^3 = c^3 + d^3 | a,b,c,d in [1,1000]
# Runtime: O(N^2)


def cube_solutions():
    n = 5
    cd_pairs = defaultdict(list)
    for c in range(1, n+1):
        for d in range(1, n+1):
            sum = (c ** 3) + (d ** 3)
            # Sum is key, holds any pair that has sum
            cd_pairs[sum].append((c, d))

    for sum in cd_pairs.items():
        for pair1 in sum[1]:
            for pair2 in sum[1]:
                a = pair1[0]
                b = pair1[1]
                c = pair2[0]
                d = pair2[1]
                print(pair1, pair2)


# Main entry point
def main():
    cube_solutions()


# Handle running main from terminal, restrict execution of code for imports
if __name__ == "__main__":
    main()
