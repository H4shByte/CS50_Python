def main():
    fruit = input('what is your fruit? ')
    nutrition(fruit)
        
fruits = {
    "apple": "130",
    "banana": "110"
}

def nutrition(x):
    if x in fruits:
        print(fruits[x])
    
main()
