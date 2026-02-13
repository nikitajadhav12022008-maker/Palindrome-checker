#palindrome checker:
s = input("enter word/number:").lower()
if(s == s[::-1]):
    print("a palindrome")
else:
    print("not a palindrome")