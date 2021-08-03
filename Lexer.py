
from typing import Counter


text_file = open("C:/testLexer.txt", "r")

data = text_file.read()





def trys():
    counter = 0
    for elem in data :
        if counter == 0:
            if elem != ' ':
                if elem.isdigit():
                    print("TOKEN_DIGIT:" + elem)
                elif elem == '{':
                    print("TOKEN_OPENBRACKET:" + elem)
                elif elem == '}':
                    print("TOKEN_CLOSINGBRACKET:" + elem)
                elif elem.isalpha():
                    pos = data.find(elem)
                    posSecond = data.find(' ')
                    secondElem = data[pos:posSecond]
                    substring = ""
                    for part in secondElem:
                        
                        if part == ' ':
                            break
                        else:
                            substring += part
                        counter = counter + 1
                    print("TOKEN_KEYWORD:" + substring)
                    counter = counter - 1
        else:
                counter = counter -  1

                

                    

        
   
               

trys()
    




text_file.close()

