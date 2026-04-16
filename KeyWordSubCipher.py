def encrypt(text, keyword):
    keyword = ''.join(dict.fromkeys(keyword.upper()))
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    # Build cipher key: keyword letters + remaining letters + numbers
    remaining = ''.join(c for c in alphabet if c not in keyword)
    key = keyword + remaining

    result = ""
    for char in text.upper():
        if char in alphabet:
            result += key[alphabet.index(char)]
        else:
            result += char
    return result
    # perfundimi


def decrypt(text, keyword):
    keyword = ''.join(dict.fromkeys(keyword.upper()))
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    remaining = ''.join(c for c in alphabet if c not in keyword)
    key = keyword + remaining

    result = ""
    for char in text.upper():
        if char in key:
            result += alphabet[key.index(char)]
        else:
            result += char
    return result


