#outline font maker

#Character Sets
lower = "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫"
upper = "𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ"

#turns a character to an ASCII code
def ascify(char):
    char = ord(char)
    return char

#Turns an ASCII code into a character
def charify(code):
    code = chr(code)
    return code

#Figures out character type and returns adjusted input
def giveChar(letter):
    global lower
    global upper
    
    code = ascify(letter)
    
    if code >= 65 and code <= 90: #upper
        code = code - 65
        return upper[code]
    elif code >= 97 and code <= 122: #lower
        code = code - 97
        return lower[code]
    else: #all other characters don't have outline versions
        return letter
        

#main bit
def convertInput():
    string = ""
    initialText = str(input(">"))
    for i in range (len(initialText)):
        string = string + giveChar(initialText[i])
    print(string)

while 1 == 1:
    convertInput()
