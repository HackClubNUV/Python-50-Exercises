''' Pig Latin problem
1) If the word begins with a vowel (a, e, i, o, or u), add “way” to the end of the
word. So “air” becomes “airway” and “eat” becomes “eatway.”
2) If the word begins with any other letter, then we take the first letter, put it on
the end of the word, and then add “ay.” Thus, “python” becomes “ythonpay”
and “computer” becomes “omputercay.”   '''

def pig_latin(a):
    if a[0] in 'aeiou':
        return a+'way'
    else:
        return a[1:]+a[0]+'ay'

print(pig_latin(input("Enter any string p.s first letter should not be capital :")))

#Hardik Raval

