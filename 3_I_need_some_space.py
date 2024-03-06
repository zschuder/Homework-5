import numpy as np

myarr = np.array(['python','is','cool!'])
def spaceBetween(myarr):
    update_words = []
    for word in myarr:
        result = ""
        for character in word:
            result = result + character + " "
        update_words.append(result)
    newarr = np.array(update_words)
    print(newarr)
print(spaceBetween(myarr))