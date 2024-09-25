
letters = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext, key):
    encrypted = ''
    for letter in plaintext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                encrypted += letter
            else: 
                indextwo = index + key
                if indextwo >= 26:
                    indextwo -= 26
                encrypted += letters[indextwo]
    return encrypted

def decrypt(encrypted, key):
    plaintext = ''
    for letter in encrypted:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else: 
                indextwo = index - key
                if indextwo < 0:
                    indextwo += 26
                plaintext += letters[indextwo]
    return plaintext


type = input('Do you want to encrypt or decrypt?: ').lower()

if type == 'encrypt':
    key = int(input('Enter the key you want to use (1 through 26): '))
    plaintext = input('Enter the text to encrypt: ')
    encrypted = encrypt(plaintext, key)
    print()
    print('Before:', plaintext)
    print()
    print('encrypted:', encrypted)
    print()

elif type == 'decrypt':
    key = int(input('Enter the key (1 through 26): '))
    encrypted = input('Enter the text to decrypt: ')
    decrypted = decrypt(encrypted, key)
    print()
    print('Before:', encrypted)
    print()
    print('decrypted:', decrypted)
    print()



