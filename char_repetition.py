def first_non_repeated(s):
    char_counts = {}  # Dictionary to store character counts
    # Count occurrences of each character in the string
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    # Find the first non-repeating character
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i
    
    return -1  # No non-repeating character found
