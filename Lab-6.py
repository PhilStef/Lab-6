def main():
    print("Menu")
    print('-------------')
    opas = ''
    while True:
        print("1. Encode\n2. Decode\n3. Quit")
        inp = int(input('Please enter an option: '))
        
        #Comment
        if inp == 1:
            pas = input("Please enter your password to encode: ")
            opas = encode(pas)
            print("Your password has been encoded and saved!")
        if inp == 2:
            opas2 = decode(opas)
            print('The encoded password is', opas, ', and the original password is', opas2)
        if inp == 3:
            break


def encode(num):
    numm = list(num)
    new = ''
    for i in range(len(numm)):
        numm[i] = int(num[i]) + 3
        new += str(numm[i])
    return new

def decode(opas):
    temp_string = ''        
    for i in opas:
        i = int(i)
        i -= 3
        temp_string += str(i)
    return temp_string



if __name__ == "__main__":
    main()