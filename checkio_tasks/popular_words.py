from collections import Counter

def popular_words(text: str, words: list) -> dict:
    c = Counter(text.lower().split())
    popular_dict = {}
    for w in words:
        if w in c:
            popular_dict[w] = c[w]
        else:
            popular_dict[w] = 0
    return popular_dict


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))