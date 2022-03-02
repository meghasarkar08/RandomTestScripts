# Function to remove all occurrences of 'AB' and 'C' from the string
def remove(s):
    chars = list(s)
    i = 0
    k = 0
    while i < len(chars):
        if chars[i] == 'B' and (k > 0 and chars[k - 1] == 'A'):
            k = k - 1
            i = i + 1

        elif chars[i] == 'A' and (k > 0 and chars[k - 1] == 'B'):
            i = i + 1
            k = k - 1

        elif chars[i] == 'D' and (k > 0 and chars[k - 1] == 'C'):
            i = i + 1
            k = k - 1

        elif chars[i] == 'C' and (k > 0 and chars[k - 1] == 'D'):
            i = i + 1
            k = k - 1

        else:
            chars[k] = chars[i]
            k = k + 1
            i = i + 1

    return ''.join(chars[:k])


print(remove('CBACD'))
print(remove('CABABD'))
print(remove('ACBDACBD'))