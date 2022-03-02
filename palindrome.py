def testpalindrome(s):
    if s == s[::-1]:
        return print( s + " is palindrome")
    else:
        return print( s + " is not palindrome")

testpalindrome("1001")