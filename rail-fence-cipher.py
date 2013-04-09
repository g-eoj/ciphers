def railPosition(rails):
    rail = 0
    while True:
        if rail == 0:
            down = True
        elif rail == rails - 1:
            down = False
        if down:
            yield rail
            rail += 1
        else:
            yield rail
            rail -= 1


def removeSpaces(s):
    return ''.join(s.split())


def encipher(plain_text, rails):
    plain_text = removeSpaces(plain_text)
    cipher_text = [''] * rails
    rail = railPosition(rails)
    for t in plain_text:
        cipher_text[rail.next()] += t
    cipher_text = ''.join(cipher_text)
    cipher_text = ' '.join([cipher_text[p:p + 5] for p in xrange(0, len(cipher_text), 5)])
    return cipher_text


def decipher(cipher_text, rails):
    cipher_text = removeSpaces(cipher_text)
    plain_text = ''
    chunks = []
    chunkSizes = [0] * rails
    rail = railPosition(rails)
    for i in xrange(len(cipher_text)):
        chunkSizes[rail.next()] += 1
    position = 0
    for r in xrange(rails):
        chunks.append(cipher_text[position:position + chunkSizes[r]])
        position += chunkSizes[r]
    rail = railPosition(rails)
    for i in xrange(len(cipher_text)):
        rail_p = rail.next()
        plain_text += chunks[rail_p][0]
        chunks[rail_p] = chunks[rail_p].replace(chunks[rail_p][0], '', 1)
    return plain_text

test_cases = [("What's going on?", 3), ("What's going on?", 4), ("Ordinal: measures by rank order only.", 6),
              ("The ink drawings, of course, will be jeered at as obvious impostures; notwithstanding a strangeness of technique which art experts ought to remark and puzzle over.", 11)]
for t in test_cases:
    e = encipher(t[0], t[1])
    d = decipher(e, t[1])
    if removeSpaces(t[0]) == d:
        print "Pass:", t
        print "Encipher:", e
        print "Decipher:", d
        print
    else:
        print "Fail:", t
        print "Encipher:", e
        print "Decipher:", d
        print
