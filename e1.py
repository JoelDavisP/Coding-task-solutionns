f = open("marks.txt", 'r')
s = 0
for i in f:
    t= i.split(' ')[1]
    s += int(t)
f.close()
print s
