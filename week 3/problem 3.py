#problem 3
import string
def getAvailableLetters(lettersGuessed):
	alph = string.ascii_lowercase
    remain = []
    for i in alph:
        if i not in lettersGuessed:
            remain.append(i)
    return ''.join(remain)
