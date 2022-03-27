morse_dict = { 'A':'.-', 
              'B':'-...',
              'C':'-.-.', 
              'D':'-..', 
              'E':'.',
              'F':'..-.', 
              'G':'--.', 
              'H':'....',
              'I':'..', 
              'J':'.---', 
              'K':'-.-',
              'L':'.-..', 
              'M':'--', 
              'N':'-.',
              'O':'---', 
              'P':'.--.', 
              'Q':'--.-',
              'R':'.-.',
              'S':'...', 
              'T':'-',
              'U':'..-', 
              'V':'...-',
              'W':'.--',
              'X':'-..-', 
              'Y':'-.--', 
              'Z':'--..',
              '1':'.----', 
              '2':'..---', 
              '3':'...--',
              '4':'....-', 
              '5':'.....', 
              '6':'-....',
              '7':'--...', 
              '8':'---..', 
              '9':'----.',
              '0':'-----', 
              ', ':'--..--', 
              '.':'.-.-.-',
              '?':'..--..',
              '/':'-..-.', 
              '-':'-....-',
              '(':'-.--.',
              ')':'-.--.-'}

def translate_english_to_morse(txt):
    res = ''
    for ch in txt:
        if ch != ' ':
            res += morse_dict[ch] + ' '
        else:
            res += ' '
    return res


def translate_morse_to_english(txt):
    txt += ' '
    res = ''
    morsetxt = ''
    for ch in txt:
        if ch != ' ':
            i = 0
            morsetxt += ch
        else:
            i += 1
            if i == 2 :
                morsetxt += ' '
            else:
                res += list(morse_dict.keys())[list(morse_dict.values()).index(morsetxt)]
                morsetxt = ''
    return res
