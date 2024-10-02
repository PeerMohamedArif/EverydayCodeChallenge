
# you can always use modulo to find the index value when it goes out of range



logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
Continue=True
def caesar(text, shift, direction):
    encrypted_text = ""
    decrypted_text=""
    if direction=='encode':
        for char in text:
            if char in alphabet:
                temp= alphabet.index(char)
                if temp+shift<=25:
                    encrypted_text += alphabet[temp+shift]
                else:
                    encrypted_text += alphabet[temp+shift-26]
            else:
                encrypted_text+=char
        print(f'Your encrypted text is {encrypted_text}')
        return encrypted_text
    elif direction=='decode':
        for char in text:
            if char in alphabet:
                temp= alphabet.index(char)
                if temp-shift>=0:
                    decrypted_text += alphabet[temp-shift]
                else:
                    decrypted_text += alphabet[temp-shift+26]
            else:
                decrypted_text+=char
        print(f'Your decrypted text is {decrypted_text}')
        return decrypted_text
while(Continue!= False):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction != 'encode' and direction != 'decode':
        print("invalid entry , try again")
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        value=caesar(text, shift, direction)

    value=input("Do you want to continue, if Yes give \'y\' else give \'n\'")
    if value=='y':
        Continue= True
    else:
        break

print("Goodbye")






