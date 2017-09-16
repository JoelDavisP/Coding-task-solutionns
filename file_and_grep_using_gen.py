def readfiles(fnames):
    for i in fnames:
        f = open(i, 'r') 
        for line in f:
            yield line
def grep(pattern, lines):
    a = []
    for line in lines:
        if pattern in line:
            a.append(line)
    return a

def printlines(lines):
    for line in lines:
        print line

def main(pattern, fnames):
    lines = readfiles(fnames)
    answr = grep(pattern, lines)
    printlines(answr)


main('ok', ['data.txt', 'data2.txt', 'data3.txt','data4.txt','data5.txt'])
    
