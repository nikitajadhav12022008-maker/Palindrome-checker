#palindrome checker:
s = input("enter word/number:").lower()
if(s == s[::-1]):
    print("palindrome")
else:
  print("not palindrome")
