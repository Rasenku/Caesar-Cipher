import string


# The Encryption Function
def cipher_encrypt(plain_text, key):

    encrypted = ""

    for c in plain_text:

        if c.isupper(): #check if it's an uppercase character

            c_index = ord(c) - ord('A')

            # shift the current character by key positions
            c_shifted = (c_index + key) % 26 + ord('A')

            c_new = chr(c_shifted)

            encrypted += c_new

        elif c.islower(): #check if its a lowecase character

            # subtract the unicode of 'a' to get index in [0-25) range
            c_index = ord(c) - ord('a')

            c_shifted = (c_index + key) % 26 + ord('a')

            c_new = chr(c_shifted)

            encrypted += c_new

        elif c.isdigit():

            # if it's a number,shift its actual value
            c_new = (int(c) + key) % 10

            encrypted += str(c_new)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            encrypted += c

    return encrypted

# The Decryption Function
def cipher_decrypt(ciphertext, key):

    decrypted = ""

    for c in ciphertext:

        if c.isupper():

            c_index = ord(c) - ord('A')

            # shift the current character to left by key positions to get its original position
            c_og_pos = (c_index - key) % 26 + ord('A')

            c_og = chr(c_og_pos)

            decrypted += c_og

        elif c.islower():

            c_index = ord(c) - ord('a')

            c_og_pos = (c_index - key) % 26 + ord('a')

            c_og = chr(c_og_pos)

            decrypted += c_og

        elif c.isdigit():

            # if it's a number,shift its actual value
            c_og = (int(c) - key) % 10

            decrypted += str(c_og)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            decrypted += c

    return decrypted

plain_text = "Mate, the adventure ride in Canberra was so much fun, We were so drunk we ended up calling 911!"

ciphertext = cipher_encrypt(plain_text, 4)

print("Plain text message:\n", plain_text)

print("Encrypted ciphertext:\n", ciphertext)

ciphertext = "Sr xli gsyrx sj 7, 6, 5 - Ezirkivw Ewwiqfpi!"

decrypted_msg = cipher_decrypt(ciphertext, 4)

print("The cipher text:\n", ciphertext)

print("The decrypted message is:\n",decrypted_msg)


# table = str.maketrans("abcde", "01234")
#
# text = "Albert Einstein, born in Germany, was a prominent theoretical physicist."
#
# translated = text.translate(table)
#
# print("Original text:/n", text)
#
# print("Translated text:/n", translated)

import string

def cipher_cipher_using_lookup(text,  key, characters = string.ascii_lowercase, decrypt=False):

    if key < 0:

        print("key cannot be negative")

        return None

    n = len(characters)

    if decrypt==True:

        key = n - key

    table = str.maketrans(characters, characters[key:]+characters[:key])

    translated_text = text.translate(table)

    return translated_text

text = "HELLO WORLD! Welcome to the world of Cryptography!"

encrypted = cipher_cipher_using_lookup(text, 3, string.ascii_uppercase, decrypt=False)

print(encrypted)
