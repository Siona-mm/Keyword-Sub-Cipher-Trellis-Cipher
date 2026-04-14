
def trellis_encrypt(plaintext: str) -> str:
    # e bojna inputin e userit uppercaee dhe nese ka hapesira i zevendesojna me X
    text = ''.join(c.upper() for c in plaintext if c.isalnum() or c.isspace())
    text = text.replace(" ", "X")

    #duhet me llogarit nbaze te inputit, sa blloqe na vyjn
    block_size = 16
    num_blocks = (len(text) + block_size - 1) // block_size

    ciphertext = ""

    #pe bojm ni loop
    for block in range(num_blocks):
        start = block * block_size
        end = start + block_size
        block_text = text[start:end]

        #per seciln bllok e bojna ni grid(matrice)
        grid = [[' ' for _ in range(4)] for _ in range(4)]
        idx = 0

        # nfillim mushen pozitat cifte
        for i in range(4):
            for j in range(4):
                if (i + j) % 2 == 0 and idx < len(block_text):
                    grid[i][j] = block_text[idx]
                    idx += 1

        # pozitat teke
        for i in range(4):
            for j in range(4):
                if (i + j) % 2 == 1 and idx < len(block_text):
                    grid[i][j] = block_text[idx]
                    idx += 1

        # Padding: Fill remaining empty cells with 'X'
        while idx < 16:
            for i in range(4):
                for j in range(4):
                    if grid[i][j] == ' ' and idx < 16:
                        grid[i][j] = 'X'
                        idx += 1


        for row in grid:
            ciphertext += ''.join(row)

    return ciphertext