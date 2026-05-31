class Solution:
    # Function to print a square pattern of stars
    def pattern1(self, N):
        # Outer loop to handle rows
        for i in range(N):
            # Inner loop to handle columns for each row
            for j in range(N):
                # Print a star followed by a space
                print("*", end=" ")
            # After printing stars in a row, move to the next line
            print() 

# Driver code
sol = Solution()
N = 5  # Set the size of the square (5x5)
sol.pattern1(N)  # Call the function to print the pattern
