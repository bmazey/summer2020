

def verify():
    return "congratulations! don't forget to email your github username to b.mazey@nyu.edu!"


def console(x):
    # for c in x:
       # if c == 'a' or c == 'y':
           # print(c)
    y = x + '!'
    return y


def fizzloop(x):
    for i in range(x):
        print('value of i is: ' + str(i))
        if i % 3 == 0:
            print('fizz')
        if i % 5 == 0:
            print('buzz')


if __name__ == '__main__':
    # z = console('Happy Tuesday')
    # print(z)
    # z = console('Tomorrow is Wednesday')
    # print(z)
    # console('Day after is Thursday')
    # console(str(2) + 'test')
    fizzloop(10)
