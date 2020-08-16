import os
import random 


class checksum():
    count0 = 0
    count1 = 0
    count2 = 0

# def algoritm_searching_by_one_plus():
#     base = raw_input('File name ->')
#     with open(base, 'r') as file:
#         for line in file:


def algoritm_searching_by_one_mail():
    combb = []
    # email = raw_input('Email -> ')
    # email = 'test123@test.com'
    passw = raw_input('Password ->')
    # passw = 'test321'
    combinations = raw_input('You variants here -> ')
    # combinations = 'qwerty 123 321 test 43546546 67777'
    kol0 = input('How much tries? -> ')
    i = 0
    save = open('out.txt', 'w+')
    def start(combb, combinations): 
        try:
            save = open('out.txt', 'a+')
            trash = open('trash', 'a+')
            for i in range(len(combinations.split(' '))):
                rand0 = random.randint(0, len(combinations.split(' ')))
                rand1 = random.randint(0, len(combinations.split(' ')))
                comb = combinations.split(' ')[rand0] + combinations.split(' ')[rand1]
                checksum.count0 += 1
                checksum.count1 += 1
                # print s/tr([checksum.count0]) + comb
                if checksum.count1 == 10000:
                    checksum.count2 = checksum.count2 + 10000
                    print str([checksum.count2])
                    checksum.count1 = 0
                chars = comb
                n = 0
                x = 0
                for n in range(len(comb)):
                    password =''
                    for x in range(len(comb)):
                        password += random.choice(chars)
                    trash.write(password + '\n')
                    if password == passw:
                        save.write(password + ' | [' + str(rand0) + ':' + str(rand1) + ']\n')
                        exit()
                if comb in combb:
                    pass
                else:
                    combb.append(comb)
                    # save.write(comb + '\n')
                    if password == passw:
                        save.write(password + '\n')
                        # trash.write(password + '\n')
                        exit()
                    trash.write(password + '\n')
                if password in combb:
                    pass
                else:
                    if password == passw:
                        save.write(password + '\n')
                        # trash.write(password + '\n')
                        exit()
                    # combb.append(comb)
                    # save.write(password + '\n')    
                    # trash.write(password + '\n')


        except IndexError:
            pass

    for i in range(kol0):
        start(combb, combinations)

    print "done!"
    save.close()


if __name__ == '__main__':
    algoritm_searching_by_one_mail()
    # algoritm_searching_by_one_plus()