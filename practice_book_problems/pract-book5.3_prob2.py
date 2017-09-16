def readlines(fnames):
    for fn in fnames:
        f = open(fn,'r')
        for line in f:
            if len(line) > 40:
                yield line


def printlines(lines):
    for l in lines:
        print l

def main(fnames):
    l = readlines(fnames)
    printlines(l)

main(['data.txt','data2.txt','data3.txt','data4.txt','data5.txt'])
