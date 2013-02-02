# look into argparse
from sys import argv

if len(argv) > 1:
  plain_text = argv[1]
else:
  plain_text = raw_input("> ")
plain_text = ''.join(plain_text.split())
x = 0
p1 = ''
p2 = ''

for i in plain_text:
  if x == 0:
    p1 += i
    x += 1
  else:
    p2 += i
    x -= 1

cipher_text = p1 + p2
print cipher_text

position = 0
interval = len(plain_text) / 2
if len(plain_text) % 2 != 0:
  interval += 1
text = ''

for i in range(0, interval):
  text += cipher_text[i]
  text += cipher_text[interval + i:interval + i + 1]

print text
