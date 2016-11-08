def bits_to_bytes(bitStr):
    s = i = 0
    for b in bitStr:
        s = (s >> 1)|(0,0x80)[b]
        i +=1
        if i ==8:
            yield s
            s = i =0
    while i < 8:
        s>>1
        i +=1
        yield s

def bytes_to_bits(byteStr):
    for b in byteStr:
        i = 0
        for i in range(8):
            yield b&1
            b >>1
            i +=1


print(bits_to_bytes(bytes_to_bits(10010101010011010101010100101)))
