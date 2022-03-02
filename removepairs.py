# Function to remove all occurrences of 'XX' and 'YY' from the string
def remove(s):
    chars = list(s)
    i = 0
    k = 0
    while i < len(chars):
        if chars[i] == 'X' and (k > 0 and chars[k - 1] == 'X'):
            k = k - 1
            i = i + 1

        elif chars[i] == 'Y' and (k > 0 and chars[k - 1] == 'Y'):
            i = i + 1
            k = k - 1
        else:
            chars[k] = chars[i]
            k = k + 1
            i = i + 1

    return ''.join(chars[:k])


print(remove('CDXXYY'))
print(remove('CDXYXY'))
