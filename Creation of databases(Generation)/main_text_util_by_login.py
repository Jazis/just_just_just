import time
from string import digits
ldigits = [1,2,3,4,5,6,7,8,9,0]

digits = '1234567890'
upper = 'QWERTYUIOPASDFGHJKLZXCVBNM'
lowwer = 'qwertyuiopasdfghjklzxcvbnm'

i = 1000
x = 0 
new_line0 = ''


print "\tText file with logins please!"
base = raw_input()
name_sts = 'base_' + str(time.time()) + '.txt'
output = open(name_sts, 'w')

with open(base, 'r') as file:
    for line in file:
        line = line.replace('\n','')
        new_line0 = line.split('@')[0]
        new_line1 = line + ':' + new_line0
        output.write(str(new_line1) + '\n')
        line = line.replace('\n','')
        new_line0 = line.split('@')[0]
        new_line1 = line + ':' + new_line0
        output.write(str(new_line1) + '\n')
        for i in range(1050):
            if str(i) in line:
                new_line2 = line + ':' + new_line0.replace(str(i), '2019')
                output.write(str(new_line2) + '\n')
                new_line3 = line + ':' + new_line0.replace('-', '')
                output.write(str(new_line3) + '\n')
                new_line4 = line + ':' + new_line0.replace('_', '')
                output.write(str(new_line4) + '\n')
                new_line5 = line + ':' + new_line0.replace('.', '')
                output.write(str(new_line5) + '\n')
        for x in range(len(ldigits)):
            new_line6 = line + ':' + new_line0.replace(str(ldigits.index(x)), '')
            output.write(str(new_line6) + '\n')
            new_line7 = line + ':' + '123' + new_line0
            output.write(str(new_line7) + '\n')
            new_line8 = line + ':' + '321' + new_line0
            output.write(str(new_line8) + '\n')  
            new_line9 = line + ':' + '123456' + new_line0
            output.write(str(new_line9) + '\n')
            new_line10 = line + ':' + '123' + new_line0.replace('-', '')    
            output.write(str(new_line10) + '\n')
            new_line11 = line + ':' + '321' + new_line0.replace('_', '')
            output.write(str(new_line11) + '\n')  
            new_line12 = line + ':' + '123456' + new_line0.replace('.', '')
            output.write(str(new_line12) + '\n')
            new_line13 = line + ':' + new_line0.translate(None, digits)
            output.write(str(new_line13) + '\n')
            new_line14 = line + ':' + '123' + new_line0.lower()
            output.write(str(new_line14) + '\n')
            new_line15 = line + ':' + '321' + new_line0.lower()
            output.write(str(new_line15) + '\n')  
            new_line16 = line + ':' + '123456' + new_line0.lower()
            output.write(str(new_line16) + '\n')
            new_line17 = line + ':' + '123' + new_line0.replace('-', '').lower()
            output.write(str(new_line17) + '\n')
            new_line18 = line + ':' + '321' + new_line0.replace('_', '').lower()
            output.write(str(new_line18) + '\n')  
            new_line19 = line + ':' + '123456' + new_line0.replace('.', '').lower()
            output.write(str(new_line19) + '\n')
            new_line20 = line + ':' + new_line0.translate(None, digits).lower()
            output.write(str(new_line20) + '\n')
            new_line21 = line + ':' + new_line0 + '2019'
            output.write(str(new_line21) + '\n')
            new_line22= line + ':' + new_line0 + '2019'.lower()
            output.write(str(new_line22) + '\n')
            new_line21 = line + ':' + new_line0 + '2018'
            output.write(str(new_line21) + '\n')
            new_line23 = line + ':' + new_line0 + '2018'.lower()
            output.write(str(new_line23) + '\n')
            new_line24 = line + ':' + new_line0[::-1]
            output.write(str(new_line24) + '\n') 
            new_line25 = line + ':' + new_line0.lower()[::-1]
            output.write(str(new_line25) + '\n') 
            new_line26 = line + ':' + new_line0.upper()[::-1]
            output.write(str(new_line26) + '\n')
            new_line27 = line + ':' + '123' + new_line0.upper()
            output.write(str(new_line27) + '\n')
            new_line28 = line + ':' + '321' + new_line0.upper()
            output.write(str(new_line28) + '\n')  
            new_line29 = line + ':' + '123456' + new_line0.upper()
            output.write(str(new_line29) + '\n')
            new_line30 = line + ':' + '123' + new_line0.replace('-', '').upper()
            output.write(str(new_line30) + '\n')
            new_line31 = line + ':' + '321' + new_line0.replace('_', '').upper()
            output.write(str(new_line31) + '\n')  
            new_line32 = line + ':' + '123456' + new_line0.replace('.', '').upper()
            output.write(str(new_line32) + '\n')
            new_line33 = line + ':' + new_line0.translate(None, digits).upper()
            output.write(str(new_line33) + '\n')
            new_line34 = line + ':' + new_line0 + '2019'.upper()
            output.write(str(new_line34) + '\n')
            new_line35 = line + ':' + new_line0 + '2018'.upper()
            output.write(str(new_line35) + '\n')

        line = line.replace('\n','')
        new_line0 = line.split('@')[0]
        # ---------------------------default-------------- 
        new_line11 = new_line0
        output.write(str(line + ':' + new_line11) + '\n')
        # -------
        sum_da = line + ':2019' + new_line11
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':2018' + new_line11
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':123' + new_line11
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':321' + new_line11
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':aaa' + new_line11
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':12345' + new_line11
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':123456' + new_line11
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':1234567' + new_line11
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':12345678' + new_line11
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':123456789' + new_line11
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line11 + '2018'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line11  + '2019'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line11  + '123'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line11  + '321'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line11  + '000'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line11  + 'aaa'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line11  + '123'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line11  + '1234'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line11  + '12345'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line11  + '123456'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line11  + '1234567'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line11  + '1235678'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line11  + '123456789'
        output.write(str(sum_da) + '\n')
        # ---------------------------upper--------------
        new_line22 = new_line0.upper()
        output.write(str(line + ':' + new_line22) + '\n')
        # -------
        sum_da = line + ':2019' + new_line22
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':2018' + new_line22
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':123' + new_line22
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':321' + new_line22
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':aaa' + new_line22
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':12345' + new_line22
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':123456' + new_line22
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':1234567' + new_line22
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':12345678' + new_line22
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':123456789' + new_line22
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line22 + '2018'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line22  + '2019'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line22  + '123'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line22  + '321'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line22  + '000'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line22  + 'aaa'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line22  + '123'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line22  + '1234'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line22  + '12345'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line22  + '123456'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line22  + '1234567'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line22  + '1235678'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line22  + '123456789'
        output.write(str(sum_da) + '\n')
        # ---------------------------lower--------------
        new_line33 = new_line0.lower()
        output.write(str(line + ':' + new_line33) + '\n')
        # -------
        sum_da = line + ':2019' + new_line33
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':2018' + new_line33
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':123' + new_line33
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':321' + new_line33
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':aaa' + new_line33
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':12345' + new_line33
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':123456' + new_line33
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':1234567' + new_line33
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':12345678' + new_line33
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':123456789' + new_line33
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line33 + '2018'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line33  + '2019'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line33  + '123'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line33  + '321'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line33  + '000'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line33  + 'aaa'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line33  + '123'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line33  + '1234'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line33  + '12345'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line33  + '123456'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line33  + '1234567'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line33  + '1235678'
        output.write(str(sum_da) + '\n')
        # 
        sum_da = line + ':' + new_line33  + '123456789'
        output.write(str(sum_da) + '\n')
output.close()

i = 1000
x = 0 
new_line0 = ''
new_out = open('final_out.txt', 'w')
with open(name_sts, 'r') as file:
    for line in file:
        line = line.replace('\n','')
        new_line1 = line.split(':')[1]
        nn = line.split(':')[0]
        new_line0 = nn + ':' + new_line1
        new_out.write(str(new_line0) + '\n')
        for i in range(1050):
            if str(i) in line:
                new_line2 = nn + ':' + new_line1.replace(str(i), '2019')
                new_out.write(str(new_line2) + '\n')
        new_line3 = nn + ':' + new_line1.replace('-', '')
        new_out.write(str(new_line3) + '\n')
        new_line4 = nn + ':' + new_line1.replace('_', '')
        new_out.write(str(new_line4) + '\n')
        new_line5 = nn + ':' + new_line1.replace('.', '')
        new_out.write(str(new_line5) + '\n')
        for x in range(len(ldigits)):
            new_line6 = nn + ':' + new_line1.replace(str(ldigits.index(x)), '')
            new_out.write(str(new_line6) + '\n')
        new_line7 = nn + ':' + '123' + new_line1
        new_out.write(str(new_line7) + '\n')
        new_line8 = nn + ':' + '321' + new_line1
        new_out.write(str(new_line8) + '\n')  
        new_line9 = nn + ':' + '123456' + new_line1
        new_out.write(str(new_line9) + '\n')
        new_line10 = nn + ':' + '123' + new_line1.replace('-', '')    
        new_out.write(str(new_line10) + '\n')
        new_line11 = nn + ':' + '321' + new_line1.replace('_', '')
        new_out.write(str(new_line11) + '\n')  
        new_line12 = nn + ':' + '123456' + new_line1.replace('.', '')
        new_out.write(str(new_line12) + '\n')
        new_line13 = nn + ':' + new_line1.translate(None, digits)
        new_out.write(str(new_line13) + '\n')
        new_line14 = nn + ':' + '123' + new_line1.lower()
        new_out.write(str(new_line14) + '\n')
        new_line15 = nn + ':' + '321' + new_line1.lower()
        new_out.write(str(new_line15) + '\n')  
        new_line16 = nn + ':' + '123456' + new_line1.lower()
        new_out.write(str(new_line16) + '\n')
        new_line17 = nn + ':' + '123' + new_line1.replace('-', '').lower()
        new_out.write(str(new_line17) + '\n')
        new_line18 = nn + ':' + '321' + new_line1.replace('_', '').lower()
        new_out.write(str(new_line18) + '\n')  
        new_line19 = nn + ':' + '123456' + new_line1.replace('.', '').lower()
        new_out.write(str(new_line19) + '\n')
        new_line20 = nn + ':' + new_line1.translate(None, digits).lower()
        new_out.write(str(new_line20) + '\n')
        new_line21 = nn + ':' + new_line1 + '2019'
        new_out.write(str(new_line21) + '\n')
        new_line22= nn + ':' + new_line1 + '2019'.lower()
        new_out.write(str(new_line22) + '\n')
        new_line21 = nn + ':' + new_line1 + '2018'
        new_out.write(str(new_line21) + '\n')
        new_line23 = nn + ':' + new_line1 + '2018'.lower()
        new_out.write(str(new_line23) + '\n')
        new_line24 = nn + ':' + new_line1[::-1]
        new_out.write(str(new_line24) + '\n') 
        new_line25 = nn + ':' + new_line1.lower()[::-1]
        new_out.write(str(new_line25) + '\n') 
        new_line26 = nn + ':' + new_line1.upper()[::-1]
        new_out.write(str(new_line26) + '\n')
        new_line27 = nn + ':' + '123' + new_line1.upper()
        new_out.write(str(new_line27) + '\n')
        new_line28 = nn + ':' + '321' + new_line1.upper()
        new_out.write(str(new_line28) + '\n')  
        new_line29 = nn + ':' + '123456' + new_line1.upper()
        new_out.write(str(new_line29) + '\n')
        new_line30 = nn + ':' + '123' + new_line1.replace('-', '').upper()
        new_out.write(str(new_line30) + '\n')
        new_line31 = nn + ':' + '321' + new_line1.replace('_', '').upper()
        new_out.write(str(new_line31) + '\n')  
        new_line32 = nn + ':' + '123456' + new_line1.replace('.', '').upper()
        new_out.write(str(new_line32) + '\n')
        new_line33 = nn + ':' + new_line1.translate(None, digits).upper()
        new_out.write(str(new_line33) + '\n')
        new_line34 = nn + ':' + new_line1 + '2019'.upper()
        new_out.write(str(new_line34) + '\n')
        new_line35 = nn + ':' + new_line1 + '2018'.upper()
        new_out.write(str(new_line35) + '\n')
new_out.close()

base = 'final_out.txt'

count0 = 0
count1 = 0
name_ = 'obrabot_' + str(time.time()) + '.txt'
save_ = open(name_, 'w') 

with open(base, 'r') as file:
    for line in file:
        count0 +=1
        new_line = line.split(':')[1]
        if len(new_line) > 6:
            save_.write(line)
            count1 += 1

save_.close()
print 'All lines ' + str([count0]) + ' | Good lines '  + str([count1]) 
print '\t Anti DUB processing. wait...'

chuva = []

count1 = 0
antidub = open('mail_pass.txt', 'w')
with open(name_, 'r') as file:
    for line in file:
        if line not in chuva:
            chuva.append(line)
            antidub.write(line)
            count1 += 1
        else:
            pass

print 'All lines ' + str([count0]) + ' | Good lines '  + str([count1])
print '\t\tDone!' 

raw_input()