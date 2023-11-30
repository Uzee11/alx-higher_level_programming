def islower(c):
    # Check if the ASCII value of the character is within the lowercase range
    return ord('a') <= ord(c) <= ord('z')

# Example usage:
character = 'a'
result = islower(character)
print(result)  # This should print True
