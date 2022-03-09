def boring(s):
    count =0
    rhs = []
    lhs = []
    i=0
    while i <(len(s)-6):
        j=i+3
        while j <(len(s)-3):
            rhs1 = s[i:i+3]
            rhs.append(rhs1)

            lhs1 = s[j:j+3]
            lhs.append(lhs1)

            j+=1
        i+=1

    for k in range(len(lhs)):
        if lhs[k]==rhs[k]:
            count+=1

    if count>=1:
        return True
    else:
        return False
print("JONATHON LIKES PYTHON : "+ str(boring("JONATHON LIKES PYTHON")))
print("ALICE LIKES PYTHON : "+str(boring("ALICE LIKES PYTHON")))
print("I HEAR THE ART: "+str(boring("I HEAR THE ART")))
