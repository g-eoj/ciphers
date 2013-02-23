def railPosition(start_position, rails, up):
    if start_position == 0:
        up = False
    elif start_position == rails - 1:
        up = True
    if up:
        return start_position - 1, up
    else:
        return start_position + 1, up


def removeSpaces(s):
    return ''.join(s.split())


def encipher(plain_text, rails):
    plain_text = removeSpaces(plain_text)
    cipher_text = ['' for r in xrange(rails)]
    rail = 0
    up = False
    for t in plain_text:
        cipher_text[rail] += t
        rail, up = railPosition(rail, rails, up)
    cipher_text = ''.join(cipher_text)
    cipher_text = ' '.join([cipher_text[p:p + 5] for p in xrange(0, len(cipher_text), 5)])
    return cipher_text


def decipher(cipher_text, rails):
    cipher_text = removeSpaces(cipher_text)
    plain_text = ''
    chunks = []
    chunkSizes = [0 for r in xrange(rails)]
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

test_cases = [("What's going on?", 3), ("What's going on?", 4), ("Ordinal: measures by rank order only.", 6),
              ("The ink drawings, of course, will be jeered at as obvious impostures; notwithstanding a strangeness of technique which art experts ought to remark and puzzle over.", 11)]
for t in test_cases:
    e = encipher(t[0], t[1])
    d = decipher(e, t[1])
    if removeSpaces(t[0]) == d:
        print "Pass:", t
    else:
        print "Fail:", t
        print "Encipher:", e
        print "Decipher:", d
