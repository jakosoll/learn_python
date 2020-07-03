import re

def is_stressful(subj):
    """
        recognize stressful subject
    """
    patterns = [
        'h+.e+.l+.p+|help',
        'a+.s+.a+.p|help',
        'u+.r+.g+.e+.n+.t|help'
    ]
    return any([re.findall(p, subj.lower()) for p in patterns])

if __name__ == '__main__':
    #These "asserts" are only for self-checking and not necessarily for auto-testing
    # assert is_stressful("Hi") == False, "First"
    # assert is_stressful("I neeed HELP") == True, "Second"
    # print('Done! Go Check it!')
    print(is_stressful("I neeed H!E!L!P"))
