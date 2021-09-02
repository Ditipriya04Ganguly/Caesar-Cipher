
def encrypted(string,s):
  cipher=''
  for char in string:
    if char==' ':
      cipher=cipher+char
    elif char.isupper():
      cipher=cipher+char((ord(char)+shift-65)%26+65)
    else:
      cipher=cipher+char((ord(char)+shift-97)%26+97)
  return cipher



text=input("Enter the text")
s=int(input("Enter the shift key"))
print("The original string is :",text)
print("The encrypted message is :".encrypted(text,s))