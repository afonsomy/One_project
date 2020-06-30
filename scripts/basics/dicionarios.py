
def birthady():

    birthday = {'Alice':'Apr 1', 'Bob':'Dec 12', 'Carol':'Mar 4'}

    while True:
        print('Enter a name: (blank to quit)')
        name = input()
        if name == '':
            break

        if name in birthday:
            print(birthday[name] + ' is the birthday of ' + name)
            print('What is their birthday information for ' + name)
            bday = input()
            birthday[name] = bday
            print("Birthday database updated.")

def teste():

    spam = {'color': 'red', "age": 42}

    for v in spam.values():
        print("\n Os valores são:",)

    for k in spam.keys():
        print("\n As chaves são: ", k)

    for i in spam.items():
        print("\n Os items: ", i)

def teste3():

    spam = {'color': 'red', "age": 42}

    for i, k in spam.items():
        print("key:", i, "valor: ", k)

def pega():

    import pprint

    message = "It was a bright cold day in April, and the clocks were striking thirteen."

    count = {}

    for character in message:
        count.setdefault(character, 0)
        count[character] = count[character] + 1

    pprint.pprint(count)


def main():

    pega()


if __name__ == "__main__":
    main()
