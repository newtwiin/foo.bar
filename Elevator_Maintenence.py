#Elevator_Maintenence
def answer(l):

    leng = len(l)
    preFin = []
    ones= []
    twos = []
    threes = []
    final = []
    maxim1 = 0;
    maxim2 = 0;
    maxim3 = 0;

    for s in l:
        preFin.append(s.split('.'))

    for n in preFin:
        temp = []
        for k in n:
            temp.append(int(k))
        if (len(temp) == 1):
            if max(temp)> maxim1:
                maxim1 = max(temp)
            ones.append(temp)
        if (len(temp) == 2):
            twos.append(temp)
            if max(temp)> maxim2:
                maxim2 = max(temp)
        if (len(temp) == 3):
            threes.append(temp)
            if max(temp)> maxim3:
                maxim3 = max(temp)
        del temp

    a = 0
    b = 0
    c = 0
    onA = True
    onB = True
    onC = True
    maxim = max([maxim1, maxim2, maxim3])
    
    while(len(final) < leng):
        if (([a] in ones) and onA):
            final.append(str(a))
            onA = False
        if([a, b] in twos and onB):
            final.append("%d.%d" %(a, b))
            onB = False
        if([a, b, c] in threes):
            final.append("%d.%d.%d" % (a, b, c))
        c+= 1
        if c > maxim:
            c = 0
            b += 1
            onB = True
            if b > maxim:
                b = 0
                c = 0
                onB = True
                onA = True
                a+=1
              
    return final


def main():
    answer(["0", "0.1.1", "2.3.4", "2.1.2", "1.1.2", "1", "1.0.0", "1.0", "1.3.3", "1.0.12", "1.0.2"])

main()
