import os
import time
print "><"
print "Link to base"
output = open('out_' + str(time.time()) + '.txt', 'w')
base = raw_input()
ldigits = [1,2,3,4,5,6,7,8,9,0]
digits = '1234567890'
upper = 'QWERTYUIOPASDFGHJKLZXCVBNM'
lowwer = 'qwertyuiopasdfghjklzxcvbnm'

with open(base, 'r') as file:
    for line in file:
        line = line.replace('\n','')
        new_line1 = line.split(':')[1]
        nn = line.split(':')[0]
        new_line0 = nn + ':' + new_line1
        output.write(str(new_line0) + '\n')
        for i in range(1050):
            if str(i) in line:
                new_line2 = nn + ':' + new_line1.replace(str(i), '2019')
                output.write(str(new_line2) + '\n')
        new_line3 = nn + ':' + new_line1.replace('-', '')
        output.write(str(new_line3) + '\n')
        new_line4 = nn + ':' + new_line1.replace('_', '')
        output.write(str(new_line4) + '\n')
        new_line5 = nn + ':' + new_line1.replace('.', '')
        output.write(str(new_line5) + '\n')
        for x in range(len(ldigits)):
            new_line6 = nn + ':' + new_line1.replace(str(ldigits.index(x)), '')
            output.write(str(new_line6) + '\n')
        new_line7 = nn + ':' + '123' + new_line1
        output.write(str(new_line7) + '\n')
        new_line8 = nn + ':' + '321' + new_line1
        output.write(str(new_line8) + '\n')  
        new_line9 = nn + ':' + '123456' + new_line1
        output.write(str(new_line9) + '\n')
        new_line10 = nn + ':' + '123' + new_line1.replace('-', '')    
        output.write(str(new_line10) + '\n')
        new_line11 = nn + ':' + '321' + new_line1.replace('_', '')
        output.write(str(new_line11) + '\n')  
        new_line12 = nn + ':' + '123456' + new_line1.replace('.', '')
        output.write(str(new_line12) + '\n')
        new_line13 = nn + ':' + new_line1.translate(None, digits)
        output.write(str(new_line13) + '\n')
        new_line14 = nn + ':' + '123' + new_line1.lower()
        output.write(str(new_line14) + '\n')
        new_line15 = nn + ':' + '321' + new_line1.lower()
        output.write(str(new_line15) + '\n')  
        new_line16 = nn + ':' + '123456' + new_line1.lower()
        output.write(str(new_line16) + '\n')
        new_line17 = nn + ':' + '123' + new_line1.replace('-', '').lower()
        output.write(str(new_line17) + '\n')
        new_line18 = nn + ':' + '321' + new_line1.replace('_', '').lower()
        output.write(str(new_line18) + '\n')  
        new_line19 = nn + ':' + '123456' + new_line1.replace('.', '').lower()
        output.write(str(new_line19) + '\n')
        new_line20 = nn + ':' + new_line1.translate(None, digits).lower()
        output.write(str(new_line20) + '\n')
        new_line21 = nn + ':' + new_line1 + '2019'
        output.write(str(new_line21) + '\n')
        new_line22= nn + ':' + new_line1 + '2019'.lower()
        output.write(str(new_line22) + '\n')
        new_line21 = nn + ':' + new_line1 + '2018'
        output.write(str(new_line21) + '\n')
        new_line23 = nn + ':' + new_line1 + '2018'.lower()
        output.write(str(new_line23) + '\n')
        new_line24 = nn + ':' + new_line1[::-1]
        output.write(str(new_line24) + '\n') 
        new_line25 = nn + ':' + new_line1.lower()[::-1]
        output.write(str(new_line25) + '\n') 
        new_line26 = nn + ':' + new_line1.upper()[::-1]
        output.write(str(new_line26) + '\n')
        new_line27 = nn + ':' + '123' + new_line1.upper()
        output.write(str(new_line27) + '\n')
        new_line28 = nn + ':' + '321' + new_line1.upper()
        output.write(str(new_line28) + '\n')  
        new_line29 = nn + ':' + '123456' + new_line1.upper()
        output.write(str(new_line29) + '\n')
        new_line30 = nn + ':' + '123' + new_line1.replace('-', '').upper()
        output.write(str(new_line30) + '\n')
        new_line31 = nn + ':' + '321' + new_line1.replace('_', '').upper()
        output.write(str(new_line31) + '\n')  
        new_line32 = nn + ':' + '123456' + new_line1.replace('.', '').upper()
        output.write(str(new_line32) + '\n')
        new_line33 = nn + ':' + new_line1.translate(None, digits).upper()
        output.write(str(new_line33) + '\n')
        new_line34 = nn + ':' + new_line1 + '2019'.upper()
        output.write(str(new_line34) + '\n')
        new_line35 = nn + ':' + new_line1 + '2018'.upper()
        output.write(str(new_line35) + '\n')
output.close()
print 'Done!'