# The following code is for decoding and encoding strings using a Caesar cypher

# A Caesar cypher takes a letter and shifts it a predetermined amount of times.
# Example: 'in' whith a shift of 3 would shift into 'lq'
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Direction will determine if shifting to the right with encode or to the left with decode.
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(tex, shi, dir):
    caesarText = ""
    # For each letter in the tex. Will be shifted by shi number. Right for encode. Left for decode.
    for letter in tex:
        x = alphabet.index(letter)
        if dir == "encode":
            x += shi
            while x >= 25:
                x -= 26
        elif dir == "decode":
            x -= shi
        newLetter= alphabet[x]
        caesarText += newLetter
    print(f"The {dir}ed text is {caesarText}")

caesar(tex = text, shi = shift, dir = direction)