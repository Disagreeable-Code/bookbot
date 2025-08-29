# python
from stats import get_num_words

from stats import num_lett

# from stats import sort

from stats import mak_list

import sys

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents



def main(book_path):
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    
    print(f"============ BOOKBOT ============ \nAnalyzing book found at {book_path} \n----------- Word Count ---------- \nFound {num_words} total words")
    
    #print(get_num_words(text))
    c_dic = num_lett(text)
    s_dic = mak_list(c_dic)
    for item in s_dic:
        print(f"{item['char']}: {item['num']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]
    main(book_path)

    

    