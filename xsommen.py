import random
import string
from tabulate import tabulate

seta = [1, 3, 4, 5, 6, 7, 8, 9]
setb = [1, 3, 4, 5, 6, 7, 8, 9]



for p in range(0,2):
    print ""
    print "\\begin{tabular}{ccc}"
    print "\\vspace{3cm}"
    for r in range(0,5):
        for c in range(0, 3): 
            random.shuffle(seta)
            a1=seta[0]
            a2=seta[1]
            a3=seta[2]
            asom=a1+10*a2+100*a3
            random.shuffle(setb)
            b1=setb[0]
            b2=setb[1]
            bsom=b1+10*b2
            somt=asom*bsom
        
            astr = str(asom)
            bstr = str(bsom)
            tstr = str(somt)
            if len(tstr)<5:
                tstr=string.join([" ",tstr],'')
            if len(tstr)<5:
                tstr=string.join([" ",tstr],'')   
            if c>0 :
                print "&"
            print ""
            print "\\begin{tabular}{llllll}"
            print '&','&',astr[0],'&',astr[1],'&',astr[2],'&','\\\\'
            print '&','&','&',bstr[0],'&',bstr[1],'&','x','\\\\'
            print "\hline"
            print tstr[0],'&',tstr[1],'&',tstr[2],'&',tstr[3],'&',tstr[4],'&','\\\\'
            print "\end{tabular}"
            if c==2 :
                print "\\\\"
                print "\\vspace{3cm}"
    print "\end{tabular}"
    print "\\newpage"