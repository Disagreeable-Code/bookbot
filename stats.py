
def get_num_words(textssss):
    textypoopy = textssss.split()
    num_words = len(textypoopy)
    return num_words

text_cunt = {}

def num_lett(textssss):
    text_lowr = textssss.lower()
    for i in text_lowr:
        if i in text_cunt:
            text_cunt[i] += 1
        else:
            text_cunt[i] = 1
    return text_cunt

def sort(items):
    return items["num"]

def mak_list(items):
    diclist = [{"char": key, "num": value} for key, value in items.items()]
    diclist.sort(reverse=True, key=sort)
    return diclist
