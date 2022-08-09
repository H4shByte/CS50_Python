def main():
    ans = input("what is the answer to the question of life? ")
    life(ans)

def life(x):
    match x:
        case "42" | "forty-two" | "forty two":
            print("yes")
        case _:
            print("no")

main()
