def snergle(initial, weeksToSimulate, weeksUntilFullMoon):
    popp = {}
    i=0
    while i<=weeksToSimulate-1:
        if weeksUntilFullMoon == 0:
            if i == 0:
                popp[str(i+1)] = initial*3
            else:
                if i % 4 == 0:
                    popp[str(i+1)] = popp[str(i)] * 3
                else:
                    popp[str(i+1)] = popp[str(i)] * 2

        else:
            if i == 0:
                popp[str(i + 1)] = initial * 2
            elif i<weeksUntilFullMoon:
                popp[str(i + 1)] = popp[str(i)] * 2
            elif i==weeksUntilFullMoon:
                popp[str(i + 1)] = popp[str(i)] * 3
            elif i>weeksUntilFullMoon:
                if (i-weeksUntilFullMoon)%4==0:
                    popp[str(i + 1)] = popp[str(i)] * 3
                else:
                    popp[str(i + 1)] = popp[str(i)] * 2


        i+=1
    return (tuple(popp.values()))

print(snergle(3,36,2))