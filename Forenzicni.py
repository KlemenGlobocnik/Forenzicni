import logging

def forenzicni(DNKvnos):
    logging.info("+++dbg: {0}".format(DNKvnos))
    pogojlasje=0
    pogojobraz=0
    pogojoci=0
    pogojspol=0
    pogojrasa=0
    foren=str(DNKvnos)
    if pogojlasje==0:
        if foren.count(str("CCAGCAATCGC"))>0:
            barvalas="Barva las je crna"
        elif foren.count(str("GCCAGTGCCG"))>0:
            barvalas="barva las je rjava"
        elif foren.count(str("TTAGCTATCGC"))>0:
            barvalas="barva las je korenckasta"
        else:
            barvalas="barva las je neznana"
    if pogojobraz==0:
        if foren.count(str("GCCACGG"))>0:
            oblikaobraza="oblika obraza je kvadratna"
        elif foren.count(str("ACCACAA"))>0:
            oblikaobraza="oblika obraza je okrogla"
        elif foren.count(str("AGGCCTCA"))>0:
            oblikaobraza="oblika obraza je ovalna"
        else:
            oblikaobraza="oblika obraza je neznana"
    if pogojoci==0:
        if foren.count(str("TTGTGGTGGC"))>0:
            barvaoci="barva oci je modra"
        elif foren.count(str("GGGAGGTGGC"))>0:
            barvaoci="barva oci je zelena"
        elif foren.count(str("AAGTAGTGAC"))>0:
            barvaoci="barva oci je rjava"
        else:
            barvaoci="barva oci je neznana"
    if pogojspol==0:
        if foren.count(str("TGCAGGAACTTC"))>0:
            spol="spol je moski"
        elif foren.count(str("TGAAGGACCTTC"))>0:
            spol="spol je zenski"
        else:
            spol="spol je neznan"
    if pogojrasa==0:
        if foren.count(str("AAAACCTCA"))>0:
            rasa="oseba je bele rase"
        elif foren.count(str("CGACTACAG"))>0:
            rasa="oseba je crne rase"
        elif foren.count(str("CGCGGGCCG"))>0:
            rasa="oseba je bele rase"
        else:
            rasa="rasa je neznana"
    return barvalas, oblikaobraza, barvaoci, spol, rasa

def main():
    print forenzicni("ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA")

if __name__=="__main__":
    main()
