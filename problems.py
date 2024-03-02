def isPalindrome(s):
    for i in "!@#$%&(),.;?:'":
        s = s.replace(i, "")
    print(s)
    s = "".join(s).lower()
    if s == s[::-1]:
        return True
    print(s)
    return False


isPalindrome("tHai")
