#python based mini project the palindrome checker:
#input the word or a number
s = input("enter word/number:").lower()
#conditions
if(s == s[::-1]):
    print("palindrome")
else:
  print("not palindrome")

