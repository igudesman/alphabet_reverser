def get_reverse_string_code(s):
    if not s.isalpha():
        return 'Invalid input!'

    result = []
    s = s.upper()
    for char in reversed(s):
        result.append(str(ord(char) - ord('A') + 1))
    return ' '.join(result)

s = input()
print(get_reverse_string_code(s))
