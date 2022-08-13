def main():
    string = input("camelcase: ")
    camelcase(string)
    print()


def camelcase(word):
     for i in word: 
         if i.isupper():
             print("_" + i.lower(), end="")
         else:
             print(i, end="")

main()
