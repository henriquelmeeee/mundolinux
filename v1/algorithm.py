import config

# Created by Henrique: github.com/henriquelmeeee // 2022

# The algorithm below checks if the tweet is actually referring to Linux and tries to filter out only tweets that 
# really favor something, as many just tag Linux in a tweet that has nothing to do with it.

def is_alphanum(text : str):
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z'
    ]
    for letter in text.lower():
        if not letter in letters:
            return False
    return True

def check_stage_three(text):
    if text == 'linux' or text == 'xfce' or text == 'gnome' or text == 'mundolinux':
        return False # remove tweets very simple because even involving linux, they do not contribute anything
    if not ' ' in text:
        return False # it will probably be a link
    if "tag" in text or "tags" in text:
        return False # probably the word linux is just a tag
    word = ''
    for letter in text: # sometimes some tweets get passed to the bot even though it's not in the word list, so this script will check that
        if letter == ' ':
            if word in config.words:
                return True
            else:
                word = ''
        else:
            word += letter
    return True if word in config.words else False

def check_stage_two(text):
    for letter in text:
        if letter in config.words_not_accepted:
            return False
    return True

def check_stage_one(text):
    hashtag_number = 0
    word = ''
    for letter in text:
        if ' ' in letter:
            if word in config.words_not_accepted:
                return False
            word = ''
        else:
            word += letter
        if '#' in letter:
            hashtag_number += 1
    if hashtag_number > 3:
        return False
    return True if not word.replace(' ', '') in config.words_not_accepted else False

def check(text : str):
    text = text.lower()
    if check_stage_one(text) and check_stage_two(text) and check_stage_three(text):
        return True
    return False

def test_algorithm():
    while True:
        text = input('Text: ')
        print('Result: ' + str(check(str(text))))
