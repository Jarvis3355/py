def Punctuate (str):
    result = ""
    for char in str:

        if char !=",":
            result += char

    print(result)

s = "hel,,,,,,l,,,o"
Punctuate(s)