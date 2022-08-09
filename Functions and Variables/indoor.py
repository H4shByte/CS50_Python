# prompts the user for input and then outputs that same input in lowercase.

def main():
    name = input("what is your input? ")
    lowercase(name)

def lowercase(x):
    print(x.lower())

main()
