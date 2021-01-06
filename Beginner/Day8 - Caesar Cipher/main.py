import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]

def ceasar(text, shift, direction) :
  result = ""
  if direction == "decode":
    shift*=-1

  for char in text :
    if char not in alphabet:
      result += char
      continue

    letter_index = alphabet.index(char)
    letter_index += shift

    #only possible if direction is positive
    if letter_index > len(alphabet) :
      letter_index = - (len(alphabet) - letter_index )

    letter = alphabet[letter_index]
    result+=letter

  print(result)



print(art.logo)

should_continue = True

while should_continue :
    
  direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  #In case user enters a shift that is greater than the number of letters in the alphabet
  if shift > len(alphabet) :
    shift = shift % len(alphabet)

  ceasar(text, shift, direction)

  result = input("\nType 'exit' if you want to end the program:\n")

  if(result == "exit"):
    should_continue = False