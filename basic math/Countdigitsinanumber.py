import math
def countDigits(n):
    cnt = int(math.log10(n) + 1)
    return cnt

# Main function
if __name__ == "__main__":
    N = 329823
    print("N:", N)
    digits = countDigits(N)
    print("Number of Digits in N:", digits)

                         
