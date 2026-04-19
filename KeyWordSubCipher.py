def encrypt(text, keyword):
    # I largojna shkronjat qe perseriten te keyword-i dhe e bejme me shkronja te medha
    keyword = ''.join(dict.fromkeys(keyword.upper()))
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    # Ndertojna alfabetin e shifrimit: keyword-i + shkronjat e mbetura te alfabetit
    remaining = ''.join(c for c in alphabet if c not in keyword)
    key = keyword + remaining

    result = ""
    # Tekstin qe e ka dhene user-i, shkojna shkronje per shkronje
    for char in text.upper():
        if char in alphabet:
            # E gjejme ku eshte shkronja te alfabeti normal edhe e marrim te ai i shifrimit (dmth key)
            result += key[alphabet.index(char)]
        else:
            # Nese eshte simbol ose hapesire, e lojm qashtu
            result += char
    return result
    # perfundimi


def decrypt(text, keyword):
    # E krijojna te njejtin alfabet dhe çeles si te enkriptimi
    keyword = ''.join(dict.fromkeys(keyword.upper()))
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    remaining = ''.join(c for c in alphabet if c not in keyword)
    key = keyword + remaining

    result = ""
    # Tash procesi anasjelltas, shkojme te teksti i shifruar
    for char in text.upper():
        if char in key:
            # Dallimi eshte- gjejme shkronjen te 'key' (dmth i shifruari) dhe e kthejna te 'alphabet' (origjinali)
            result += alphabet[key.index(char)]
        else:
            # Edhe ktu simbolet dhe hapesirat nuk preken
            result += char
    return result

# MAIN (pjesa kryesore)
print("=== Keyword Substitution Cipher (Letters + Numbers) ===\n")

message = input("Enter the sentence you want to encrypt: ")
keyword = input("Enter the keyword: ")

if not keyword:
    print("Keyword cannot be empty!")
    exit()

# Thirrja e funksioneve edhe shfaqja e rezultateve
encrypted = encrypt(message, keyword)
decrypted = decrypt(encrypted, keyword)

print("\n--- Results ---")
print("Original  :", message)
print("Encrypted :", encrypted)
print("Decrypted :", decrypted)

