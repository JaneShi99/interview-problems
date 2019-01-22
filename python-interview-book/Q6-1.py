def is_palindromic(s):
    # s[~i] for i in [0,len(s)-1] is s[-(i + 1)]
    return all (s[i] == s[~i] for i in range(len(s) //2))

def int_to_string(x):
    is_negative = False
    if x < x:
        x, is_negative = -x, True

    s = []
    while True:
        s.append(chr(ord('0') + x % 10)) #converting the x by adding its number to 0's char representation
        x //= 10
        if x == 0:
            break
    return ('-' if is_negative else '') + ''.join(reversed(s))

def string_to_int(s):
    return functools.reduce(
            lambda running_sum, c: running_sum * 10 + string.digits.index(c), 
            s[s[0] == '-':], 0 * (-1 if s[0] == '-' else 1)
