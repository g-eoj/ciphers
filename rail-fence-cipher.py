# look into argparse
from sys import argv


def railPosition(start_position, rails, up):
    if start_position == 0:
        up = False
    elif start_position == rails - 1:
        up = True
    if up:
        return start_position - 1, up
    else:
        return start_position + 1, up


def encipher(plain_text, rails):
    plain_text = ''.join(plain_text.split())
    cipher_text = []
    for r in range(rails):
        cipher_text.append('')
    rail = 0
    up = False
    for t in plain_text:
        cipher_text[rail] += t
        rail, up = railPosition(rail, rails, up)
    cipher_text = ''.join(cipher_text)
    cipher_text = ' '.join([cipher_text[p:p + 5] for p in xrange(0, len(cipher_text), 5)])
    return cipher_text


def decipher(cipher_text, rails):
    cipher_text = ''.join(cipher_text.split())
    plain_text = ''
    chunks = []
    chunkSizes = []
    for r in range(rails):
        chunkSizes.append(0)
    rail = 0
    up = False
    for i in range(len(cipher_text)):
        chunkSizes[rail] += 1
        rail, up = railPosition(rail, rails, up)
    position = 0
    for r in range(rails):
        chunks.append(cipher_text[position:position + chunkSizes[r]])
        position += chunkSizes[r]
    rail = 0
    up = False
    for i in range(len(cipher_text)):
        plain_text += chunks[rail][0]
        chunks[rail] = chunks[rail].replace(chunks[rail][0], '', 1)
        rail, up = railPosition(rail, rails, up)
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
