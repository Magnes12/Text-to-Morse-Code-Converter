alphabet_morse = {
'1': '.----',
'2': '..---',
'3': '...--',
'4': '....-',
'5': '.....',
'6': '-....',
'7': '--...',
'8': '---..',
'9': '----.', 
'0': '-----',
' ': ' ',
 "A": ".-",
 "B": "-...",
 "C": "-.-.",
 "D": "-..",
 "E": ".",
 "F": "..-.",
 "G": "--.",
 "H": "....",
 "I": "..",
 "J": ".---",
 "K": "-.-",
 "L": ".-..",
 "M": "--",
 "N": "-.",
 "O": "---",
 "P": ".--.",
 "Q": "--.-",
 "R": ".-.",
 "S": "...",
 "T": "-",
 "U": "..-",
 "V": "...-",
 "W": ".--",
 "X": "-..-",
 "Y": "-.--",
 "Z": "--..",
 "Ą": ".-.-",
 "Ć": "-.-..",
 "Ę": "..-..",
 "Ł": ".-..-",
 "Ń": "--.--",
 "Ó": "---.",
 "Ś": "...-...",
 "Ż": "--..-.",
 "Ź": "--..-",
}

text = input("Type text: ").upper()

morse_text = ""

for t in text:
    if t in alphabet_morse:
        morse_text += alphabet_morse[f'{t}']
    else:
        morse_text += " "

print(f"Morse: {morse_text}")
