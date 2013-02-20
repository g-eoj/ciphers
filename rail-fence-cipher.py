# look into argparse
from sys import argv


def encipher(plain_text, rails):
    plain_text = ''.join(plain_text.split())
    cipher_text = []
    for r in range(rails):
        cipher_text.append('')
    rail = -1
    up = False
    # track rail position
    for t in plain_text:
        if rail == 0:
            up = False
        elif rail == rails - 1:
            up = True
        if up:
            rail -= 1
        else:
            rail += 1
        cipher_text[rail] += t
    cipher_text = ''.join(cipher_text)
    return cipher_text


def decipher(cipher_text, rails):
    plain_text = ''
    chunks = []
    chunkSizes = []

    for r in range(rails):
        chunkSizes.append(0)
    up = False
    rail = -1
    for i in range(len(cipher_text)):
        if rail == 0:
            up = False
        elif rail == rails - 1:
            up = True
        if up:
            rail -= 1
        else:
            rail += 1
        chunkSizes[rail] += 1

    position = 0
    for r in range(rails):
        chunks.append(cipher_text[position:position + chunkSizes[r]])
        position += chunkSizes[r]

    up = False
    rail = -1
    for i in range(len(cipher_text)):
        if rail == 0:
            up = False
        elif rail == rails - 1:
            up = True
        if up:
            rail -= 1
        else:
            rail += 1
        plain_text += chunks[rail][0]
        chunks[rail] = chunks[rail].replace(chunks[rail][0], '', 1)

    return plain_text

# cipher_text = encipher("What's going on", 4)
# print decipher(cipher_text, 4)

if len(argv) > 1:
    plain_text = argv[1]
else:
    plain_text = raw_input("Plain text> ")
    rail_count = int(raw_input("How many rails> "))
cipher_text = encipher(plain_text, rail_count)
print cipher_text
print decipher(cipher_text, rail_count)

ctext_file_name = raw_input("Save as (leave blank if you don't want to save): ")
if len(ctext_file_name) > 0:
    ctext_file = open(ctext_file_name, 'w')
    ctext_file.write(cipher_text)
    ctext_file.close()
