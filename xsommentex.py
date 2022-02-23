import random
import string
from tabulate import tabulate

seta = [1, 3, 4, 5, 6, 7, 8, 9]
setb = [1, 3, 4, 5, 6, 7, 8, 9]

# f1.write( de .tex file
f1=open('/Users/janvanhulzen/Documents/Courses/driemaster/xsommen_opgaven.tex','w+')
f2=open('/Users/janvanhulzen/Documents/Courses/driemaster/xsommen_antwoorden.tex','w+')


for p in range(0,5):
    f1.write( '\n')
    f2.write( '\n')
    f1.write( '\\begin{tabular}{l c r }\n')
    f2.write( '\\begin{tabular}{l c r }\n')
    f1.write( '\\vspace{3cm}\n')
    f2.write( '\\vspace{3cm}\n')
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
                f1.write( '&')
                f2.write( '&')
            f1.write( '\n')
            f2.write( '\n')
            f1.write( '\\begin{tabular}{llllll}\n')
            f2.write( '\\begin{tabular}{llllll}\n')
            f1.write( '&'+'&'+astr[0]+'&'+astr[1]+'&'+astr[2]+'&'+'\\\\\n')
            f2.write( '&'+'&'+astr[0]+'&'+astr[1]+'&'+astr[2]+'&'+'\\\\\n')
            f1.write( '&'+'&'+'&'+bstr[0]+'&'+bstr[1]+'&'+'x'+'\\\\\n')
            f2.write( '&'+'&'+'&'+bstr[0]+'&'+bstr[1]+'&'+'x'+'\\\\\n')
            f1.write( '\hline\n')
            f2.write( '\hline\n')
            f1.write( tstr[0]+'&'+tstr[1]+'&'+tstr[2]+'&'+tstr[3]+'&'+tstr[4]+'&'+'\\\\\n')
            f2.write( '&'+'&'+'&'+'&'+'&'+'\\\\\n')
            f1.write( "\end{tabular}")
            f2.write( "\end{tabular}")
            if c==2 :
                f1.write( "\\\\")
                f2.write( "\\\\")
                f1.write( "\\vspace{3cm}")
                f2.write( "\\vspace{3cm}")
                
    f1.write( "\end{tabular}")
    f2.write( "\end{tabular}")
    f1.write( "\\newpage")
    f2.write( "\\newpage")
    
f1.close()
f2.close()
