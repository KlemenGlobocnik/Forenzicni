import logging

def forenzicni(a):
    logging.info("+++dbg: {0}".format(a))
    b=0
    c=0
    d=0
    e=0
    f=0
    foren=str(a)
    if b==0:
        if foren.count(str("CCAGCAATCGC"))>0:
            bb="Barva las je crna"
        elif foren.count(str("GCCAGTGCCG"))>0:
            bb="barva las je rjava"
        elif foren.count(str("TTAGCTATCGC"))>0:
            bb="barva las je korenckasta"
        else:
            bb="barva las je neznana"
    if c==0:
        if foren.count(str("GCCACGG"))>0:
            cc="oblika obraza je kvadratna"
        elif foren.count(str("ACCACAA"))>0:
            cc="oblika obraza je okrogla"
        elif foren.count(str("AGGCCTCA"))>0:
            cc="oblika obraza je ovalna"
        else:
            cc="oblika obraza je neznana"
    if d==0:
        if foren.count(str("TTGTGGTGGC"))>0:
            dd="barva oci je modra"
        elif foren.count(str("GGGAGGTGGC"))>0:
            dd="barva oci je zelena"
        elif foren.count(str("AAGTAGTGAC"))>0:
            dd="barva oci je rjava"
        else:
            dd="barva oci je neznana"
    if e==0:
        if foren.count(str("TGCAGGAACTTC"))>0:
            ee="spol je moski"
        elif foren.count(str("TGAAGGACCTTC"))>0:
            ee="spol je zenski"
        else:
            ee="spol je neznan"
    if f==0:
        if foren.count(str("AAAACCTCA"))>0:
            ff="oseba je bele rase"
        elif foren.count(str("CGACTACAG"))>0:
            ff="oseba je crne rase"
        elif foren.count(str("CGCGGGCCG"))>0:
            ff="oseba je bele rase"
        else:
            ff="rasa je neznana"
    return bb, cc, dd, ee, ff

def main():
    print forenzicni("ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA")

if __name__=="__main__":
    main()
