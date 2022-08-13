def main():
    string = input("camelcase: ")
    camelcase(string)
    print()


def camelcase(word):
    # for each letter in word
     for i in word: 
         # if letter is capitalized = True
         if i.isupper():
             #print that letter in lower case and prevent print function from going to next line
             print("_" + i.lower(), end="")
         #print letter
         else:
             print(i, end="")

main()
