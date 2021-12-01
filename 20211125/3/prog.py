import sys
text = sys.stdin.buffer.read()
try:
    size = int.from_bytes(text[4:8], 'little')
    typ = int.from_bytes(text[20:22], 'little')
    chns = int.from_bytes(text[22:24], 'little')
    rate = int.from_bytes(text[24:28], 'little')
    bits = int.from_bytes(text[34:36], 'little')
    dsize = int.from_bytes(text[40:44], 'little')
except Exception:
    print('NO')
else:
    if text[0:4].decode() == 'RIFF' and text[8:12].decode() == 'WAVE' and text[12:16].decode() == 'fmt ' and text[36:40].decode() == 'data':
        print(f'Size={size}, Type={typ}, Channels={chns}, Rate={rate}, Bits={bits}, Data size={dsize}')
    else:
        print('NO')
