'''
The function should recognise if a subject line is stressful. A stressful subject line means that all letters are in uppercase, and/or ends by at least 3 exclamation marks, and/or contains at least one of the following “red” words: "help", "asap", "urgent". Any of those "red" words can be spelled in different ways - "HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P", even in a very loooong way "HHHEEEEEEEEELLP," they just can't have any other letters interspersed between them.

Input: Subject line as a string.

Output: Boolean
'''

import re

def is_stressful(subj):
    """
        recognize stressful subject
    """
    patterns = [
        '(H+E+L+P|h+.e+.l+.p+|help|H+.E+.L+.P|!{3}$)',
        '(A+S+A+P|a+.s+.a+.p|asap|A+.S+.A+.P|!{3}$)',
        '(U+R+G+E+N+T|u+.r+.g+.e+.n+.t|urgent|U+.R+.G+.E+.N+.T|!{3}$)'
    ]
    return any([any(re.findall(p, subj)) + subj.isupper() for p in patterns])

if __name__ == '__main__':
    #These "asserts" are only for self-checking and not necessarily for auto-testing
    # assert is_stressful("Hi") == False, "First"
    # assert is_stressful("I neeed HELP") == True, "Second"
    # print('Done! Go Check it!')
    print(is_stressful("HI?"))
