"""Maybe it's a cipher? Maybe, but we don’t know for sure.
Maybe you can call it "homomorphism"? i wish I know this word before.
You need to check that the 2 given strings are isometric. This means that a character from one string can become a match
 for characters from another string.
One character from one string can correspond only to one character from another string. Two or more characters of one
 string can correspond to one character of another string, but not vice versa."""


def isometric_strings(str1: str, str2: str):
    dict_str = {}
    for i in range(len(str1)):
        if str1[i] in dict_str.keys():
            return str2[i] == dict_str[str1[i]]
        else:
            dict_str[str1[i]] = str2[i]
    return True


assert isometric_strings('add', 'egg') == True
assert isometric_strings('paper', 'title') == True
assert isometric_strings('foo', 'bar') == False
