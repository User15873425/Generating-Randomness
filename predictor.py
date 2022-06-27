from random import choice


def get_input():
    recd = input('Print a random string containing 0 or 1:\n')
    if recd == 'enough':
        print('Game over!')
        exit()
    else:
        return ''.join(i for i in recd if i in '01')


def prediction():
    global balance
    test = get_input()
    if test.count('0') == 0 and test.count('1') == 0:
        test = get_input()
    kit = [test[i:i+4] for i in range(len(test)-3)]
    predict = choice(kit)[:3] + ''.join('0' if triad[kit[i][:3]][0] > triad[kit[i][:3]][1] else '1' for i in range(len(kit)))
    print(f'prediction:\n{predict}')
    coincide = len([1 for i in range(len(test)-3) if test[i+3] == predict[i+3]])
    accuracy = round(coincide/(len(test)-3)*100, 2)
    balance += (len(test)-3) - coincide * 2
    print(f'\nComputer guessed right {coincide} out of {len(test)-3} symbols ({accuracy} %)\nYour balance is now ${balance}\n')
    prediction()


data = str()
print('Please give AI some data to learn...')
while len(data) < 100:
    print(f'The current data length is {len(data)}, {100 - len(data)} symbols left')
    data += get_input()
print(f'\nFinal data string:\n{data}\n')

data_kit = [data[i:i+4] for i in range(len(data)-3)]
triad = {'000': {0: data_kit.count('0000'), 1: data_kit.count('0001')},
         '001': {0: data_kit.count('0010'), 1: data_kit.count('0011')},
         '010': {0: data_kit.count('0100'), 1: data_kit.count('0101')},
         '011': {0: data_kit.count('0110'), 1: data_kit.count('0111')},
         '100': {0: data_kit.count('1000'), 1: data_kit.count('1001')},
         '101': {0: data_kit.count('1010'), 1: data_kit.count('1011')},
         '110': {0: data_kit.count('1100'), 1: data_kit.count('1101')},
         '111': {0: data_kit.count('1110'), 1: data_kit.count('1111')}}

balance = 1000
print('You have $1000. Every time the system successfully predicts your next press, you lose $1.'
      '\nOtherwise, you earn $1. Print "enough" to leave the game. Let\'s go!\n')
prediction()
