def main():
    print("Menu")
    print('-------------')
    opas = ''
    while True:
        print("1. Encode\n2. Decode\n3. Quit")
        inp = int(input())
        if inp == 1:
            pas = input("Please enter your password to encode: ")
            opas = encode(pas)
            print("Your password has been encoded and saved!")
        if inp == 2:
            pass
        if inp == 3:
            break


def encode(num):
    numm = list(num)
    new = ''
    for i in range(len(numm)):
        numm[i] = int(num[i]) + 3
        new += str(numm[i])
    return new


if __name__ == "__main__":
    main()