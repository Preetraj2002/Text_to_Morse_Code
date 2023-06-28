# Text to morse code

text_to_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.',  '(': '-.--.',  ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-',  '+': '.-.-.',  '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

morse_to_text = dict((value,key) for (key,value) in text_to_morse.items())

def encrypt(mssg):
    # to the conversion word by word, letter by letter

    encrypt_mssg=''

    for letter in mssg:
        # if letter == " ":       #whitespace
        #     encrypt_mssg[-1] ='/'
        # else:
        encrypt_letter = text_to_morse[letter.upper()]
        encrypt_mssg += encrypt_letter+' '

    return encrypt_mssg


def decrypt(mssg):


    decrypt_mssg=''

    tokens=mssg.split(' ')

    for token in tokens:

        decrypt_letter = morse_to_text[token]
        decrypt_mssg += decrypt_letter

    return decrypt_mssg


print("-------------------MORSE-TEXT CONVERTOR-------------------")

ch='#'

while ch.lower() !='x':
    print("\n1. Convert Text to Morse (Press M)"
          "\n2. Convert Morse to Text (Press T)"
          "\n3. To Exit (Press X)")

    ch=input("Enter Choice: ")
    if ch.lower() == 'm':
        print("Enter you Message that you want to encrypt")
        mssg = input("==> ")
        print("Text ==> Morse:")
        print(encrypt(mssg))

    elif ch.lower() == 't':
        print("Enter you Message that you want to decrypt")
        mssg = input("==> ")
        print("Morse ==> Text:")
        print(decrypt(mssg))

    elif ch.lower() =='x':
        print("....")

    else:
        print("Invalid Input!! Try Again")





