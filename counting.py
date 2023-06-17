# Create a 'string' variable and store "google.com" as its value.
string = "google.com"

# Create an empty dictionary {} called 'frequency'.
frequency = {}

# For 'char' in 'string'.
for char in string:

    # If 'char' is already occurring character in string, increment 'frequency[char]' by 1.
    if char in frequency:
        frequency[char] += 1

    # Else, 'frequency[char]' value is 1.
    else:
        frequency[char] = 1

# Print the character frequency of the string using f-string.
print(f"Character frequency of \"{string}\":\n{frequency}")
