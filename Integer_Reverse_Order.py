# Write a program to extract each digit from an integer in the reverse order.

# pseudocode

# Convert the integer to a string, reverse it, and then iterate through each character
def reverse_digits(integer):
    reverse_digits=[char for char in str(integer)[::-1]]
    
# Print the reversed digits with a space separating them
