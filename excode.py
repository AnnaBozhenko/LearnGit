import re
import string

def greatword(string):
    ind = 0
    leng = len(string)
    list_string = list(string)
    while ind < leng:
        if list_string[ind - 1] == ' ' or ind == 0:
            list_string[ind] = list_string[ind].upper()
        ind += 1
    ls = "".join(list_string)
    return ls
# print(greatword("harry potter"))


def power(a, n):
    if n == 0:
        return 1
    return a*power(a, n - 1)


# print(power(2, 5))
def count(a):
    if a == 0:
        return 0
    else:
        accumul =  a - 1
        print(accumul)
        return a + count(a - 1)


# print(count(4))
def summ(lst):
    # Empty list is a base in counting the sum of elements in parent lists. 
    if lst == []:
        return 0
    else:
        single_el = lst[0]
        # Create a nested list in a parent list.
        rest_els = lst[1:]
        return single_el + summ(rest_els)
# ПЕРЕВІРКА


def get_available_letters(letters_guessed):
    '''
    function also uses sets, it returns 
    difference between all characters from
    alphabet and characters from letters_guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # Create a string of letters which are in letters_guessed list.
    letters_guessed = ''.join(letters_guessed)
    alphab = list(string.ascii_lowercase)
    for char in letters_guessed:
        for el in alphab:
            if char == el:
                alphab.remove(char)
    alphab = ''.join(alphab)

        
    # Create a set of letters which are not in letters_guessed list.
    # not_guessed_letters = set(string.ascii_lowercase) - set(letters_guessed)
    # Turn the type of not_guessed_letters variable into string
    # not_letters_guessed = ''.join(not_guessed_letters)
    return alphab
#print(get_available_letters(l))

def match_with_gaps(my_word, other_word):
    '''
    The function returns bool: True if all characters in my_word
    are not in different_chars(the list where different letters 
    from other_word stored), else otherwise and when amount of 
    letters in inputs are different.
    '''
    my_word_list = re.findall(r'\S', my_word)
    different_chars = list()
    result = True
    if len(my_word_list) == len(other_word):
        for char in my_word_list:
            ind = my_word_list.index(char)
            if char in different_chars:
                result = False
                break
            else:
                if char == "_":
                    different_chars.append(other_word[ind])
                    continue
                elif other_word[ind] == char:
                    continue
                else:
                    result = False
                    break
    else:
        result = False
    return result


def manywords(l = []):
    word = input()
    if word == "0":
        return l
    l += [word]   
    return manywords(l)


'''if len(words) == 1:
    words_string = " ".join(words)
    print(words_string)
elif len(words) == 2:
    for el in words:
        print(el," and ", end = "")
else:
    for el in words:
        ind = words.index(el)
        if ind == len(words) - 2:
            print(el, ", and ", end = "", )
        elif ind == len(words) - 1:
            print(el)
        else:
            print(el, ", ", end = "")'''


def sub(a, b):
    print("a - b =")
    d = a - b
    return d

d = sub(1, 3)
print(d)
print("hello")
