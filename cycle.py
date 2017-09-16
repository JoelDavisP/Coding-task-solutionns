def cycle(s = "ABC"):
    i =0
    while True:
        yield s[i % len(s)]
        i += 1
