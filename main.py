from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def launch():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  
  if direction == "encode" or direction == "decode":
    
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
  
    if shift > 26:
      shift = shift % 26
    caesar(text, shift, direction)
    
  else:
    launch()
  
def caesar(text, shift, direction):
  result = ""
  
  if direction == "decode":
    shift *= -1
    
  for char in text:
    
    if char in alphabet:
      result += alphabet[alphabet.index(char) + shift]
    else:
     result += char
      
  print(f"Here's the {direction}d result: {result}")

print(logo)

launch()

restart = input("Want to restart the cipher program? yes or no ")

if restart == "yes":
  launch()
else:
  print("Goodbye")