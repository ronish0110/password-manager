codes = {
    'a': 'x', 'b': '4', 'c': 's', 'd': '>', 'e': '&', 'f': 'X', 'g': 'l', 'h': 'v', 'i': '.', 'j': 'A',
    'k': '{', 'l': '5', 'm': "'", 'n': 'L', 'o': 'O', 'p': '_', 'q': '%', 'r': '2', 's': '|', 't': '*',
    'u': 'G', 'v': 'c', 'w': 'e', 'x': '[', 'y': 'M', 'z': 'T',

    'A': 'a', 'B': '7', 'C': '@', 'D': '+', 'E': 'W', 'F': 'd', 'G': 'S', 'H': '=', 'I': '?', 'J': ')',
    'K': '^', 'L': '"', 'M': 'j', 'N': 'N', 'O': 'y', 'P': '<', 'Q': '~', 'R': 'C', 'S': 'Z', 'T': '}',
    'U': '9', 'V': '$', 'W': ' ', 'X': 'm', 'Y': 'i', 'Z': '`',

    '0': '\\', '1': '-', '2': 'h', '3': 'k', '4': '3', '5': 'Q', '6': '0', '7': 'P', '8': '6', '9': 'r',

    '!': 'Y', '"': '!', '#': 'V', '$': 'D', '%': 'f', '&': 'B', "'": 'b', '(': '(', ')': 'g', '*': '1',
    '+': 'n', ',': 'U', '-': 'K', '.': 'I', '/': 'J', ':': 'z', ';': ';', '<': 'o', '=': '8', '>': '/',
    '?': '#', '@': 'p', '[': 'w', '\\': 'R', ']': 'F', '^': 't', '_': 'H', '`': ']', '{': ':', '|': ',',
    '}': 'q', '~': 'E', ' ': 'u'
}


decode_codes = {}
for key in codes.keys():
    decode_codes[codes[key]] = key


def encode(password):
    new_password = ""
    
    for char in password:
        if char in codes.keys():
            new_password += codes[char]
        else:
            new_password += char

    return new_password


def decode(en_password):
    password = ""
    for char in en_password:
        if char in decode_codes.keys():
            password += decode_codes[char]
        else:
            password += char

    return password



