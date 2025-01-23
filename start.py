def palindrome(s):
    if s==s[::-1]:
        return 'Palindrome'
    else:
        return 'Not'
print(palindrome('MALAYALAM'))