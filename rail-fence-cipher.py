def railPosition(rails):
    while True:
        for i in xrange(rails):
            yield i
        for i in xrange(rails - 2, 0, -1):
            yield i


def removeSpaces(s):
    return ''.join(s.split())


def alphaNumFilter(s):
    return ''.join(c for c in s if c.isalnum())


def fiveCharUpper(s):
    return ' '.join([s.upper()[p:p + 5] for p in xrange(0, len(s), 5)])


def encipher(plain_text, rails):
    # plain_text = removeSpaces(plain_text)
    plain_text = alphaNumFilter(plain_text)
    cipher_text = [''] * rails
    rail = railPosition(rails)
    for t in plain_text:
        cipher_text[rail.next()] += t
    cipher_text = ''.join(cipher_text)
    cipher_text = fiveCharUpper(cipher_text)
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
    return plain_text.lower()


# TESTS
import time

def timedcall(fn, *args):
    "Call function with args; return the time in second and result."
    t0 = time.clock()
    g = fn(*args)
    result = [next(g) for i in xrange(10 ** 3)]
    t1 = time.clock()
    return t1 - t0, result[:10]


def average_time(n, fn, *args):
    if isinstance(n, int):
        times = [timedcall(fn, *args)[0] for i in xrange(n)]
    else:
        times = []
        while sum(times) < n:
            times.append(timedcall(fn, *args)[0])
    return sum(times) / len(times)


def run_tests():
    test_cases = [("What's going on?", 3), ("What's going on?", 4), ("Ordinal: measures by rank order only.", 6),
              ("The ink drawings, of course, will be jeered at as obvious impostures;\n notwithstanding a strangeness of technique which art experts ought to remark and puzzle over.", 11)]
    for t in test_cases:
        e = encipher(t[0], t[1])
        d = decipher(e, t[1])
        if alphaNumFilter(t[0]).lower() == d:
            print "Pass:", t
            print "Encipher:", e
            print "Decipher:", d
            print
        else:
            print "Fail:", t
            print "Encipher:", e
            print "Decipher:", d
            print

    # print timedcall(railPosition, 7)
    # print average_time(10.0, railPosition, 7)
