import time

print "\tText DB fileplease!"

base = raw_input()
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
antidub = open('anti_dub_' + str(time.time()) + '.txt', 'w')
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