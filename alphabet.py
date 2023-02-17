import re
import timeit


def alphabet_position1(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())


def alphabet_position2(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())



#def alphabet_position2(text):
#    text = text.lower()
#    letters = 'abcdefghijklmnopqrstuvwxyz'
#    letters_count = 0
#
#    for i, l in enumerate(letters):
#        letters_count += l in text
#        text = text.replace(l, f'{i+1} ')
#        
#    if not letters_count:
#        return ''
#        
#    return ' '.join(re.findall(r'\d+', text))
#

def main():
    file = open('text').read()
    t1 = timeit.timeit(
        lambda: alphabet_position1(file), number=100)
    t2 = timeit.timeit(
        lambda: alphabet_position2(file), number=100)

    # print(t1)
    # print(t2)
    # print(t1 > t2)
    
    
if __name__ == '__main__':
    main()