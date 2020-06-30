import random


from moduloteste import hoje

def primeiro(qtde: int) -> None:
    for i in range(qtde):
        print(random.randint(1, 10))


def main():
    print("Hello World!")
    primeiro(8)
    print(hoje())

if __name__ == "__main__":
    main()