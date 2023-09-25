key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',

'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',

'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',

'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',

'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',

'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',

'W':'J', 'X':'K', 'Y':'L', 'Z':'M', ' ':' '}

if(input("Encode (1) Decode (2): ") == '1'):
    raw = input("Enter text to Encrypt: ")
    Encrypted = ""
    #* Loops over the raw string looking through the key to find its value
    for i in range(raw.__len__()):
        Encrypted += key[raw[i]]
    #* Prints the encrypted string
    print(Encrypted)

else:
    encoded = input("Enter encoded string: ")
    Decrypted = ""
    #* Loops over the raw string looking through the key to find its value
    for i in range(encoded.__len__()):
        Decrypted += key[encoded[i]]
    #* Prints the encrypted string
    print(Decrypted)
