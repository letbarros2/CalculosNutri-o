from Tkinter import*

#janela(w)
w=Tk()
w.title("cálculo IMC/GET/GMB")
w.geometry("300x210")

#função cálculo masculino->(0)
def calc_masc():
    if(g.get()==0):   
        texto.insert(END,"")

#função cálculo feminino->(1)
def calc_fem():
    if(g.get()==1):
        texto.insert(END,"")

#função nível de atividade física->(2,3,4)
def leve():
    if(g1.get()==2):
        texto.insert(END,"")
def medio():
    if(g1.get()==3):
        texto.insert(END,"")
def intenso():
    if(g1.get()==4):
        texto.insert(END,"")
def gestante():
    if(g2.get()==5):
        texto.insert(END,"")
        
# dados de entrada/janela(i)
def dados():
    i=Tk()
    i.title("dados")
    i.geometry("300x300")
    age=int(idade.get())
    p=float(peso.get())
    h=float(altura.get())
    Pd=float(peso_d.get())

    #IMC
    calc_imc=(p/h**2)
    imc=str(calc_imc)
    imc=Label(i,text="IMC= " +imc)
    imc.grid(row=1,sticky=W)
    
    #IMC-cálculo
    if(calc_imc<18.5):
        a=Label(i,text="[baixo peso]")
        a.grid(row=2,sticky=W)
    elif(calc_imc>=18.5 and calc_imc<=24.9):
        a=Label(i,text="[normal]")
        a.grid(row=2,sticky=W)
    elif(calc_imc>=25.0 and calc_imc<=29.9):
        a=Label(i,text="[pré obeso]")
        a.grid(row=2,sticky=W)
    elif(calc_imc>=30.0 and calc_imc<=34.9):
        a=Label(i,text="[obeso classe.I]")
        a.grid(row=2,sticky=W)
    elif(calc_imc>=35.0 and calc_imc<=39.9):
        a=Label(i,text="[obeso classe.II]")
        a.grid(row=2,sticky=W)
    elif(calc_imc>40):
        a=Label(i,text="[obeso classe.III]")
        a.grid(row=2,sticky=W)

    #GMB-masculino
    if(g.get()==0):
        if (age>=1 and age<=3):
            gmb=(60.9 * p) - 54
            gb=str(gmb)
            gb=Label(i,text="GMB="+gb)
            gb.grid(row=3,sticky=W)
        elif (age>=4 and age<=10):
            gmb=(22.7 * p) + 495
            gb=str(gmb)
            gb=Label(i,text="GMB="+gb)
            gb.grid(row=3,sticky=W)
        elif (age>=11 and age<=18):
            gmb=(17.5*p) + 651
            gb=str(gmb)
            gb=Label(i,text="GMB="+gb)
            gb.grid(row=3,sticky=W)
        elif (age>=19 and age<=30):
            gmb=(15.3*p) + 679
            gb=str(gmb)
            gb=Label(i,text="GMB="+gb)
            gb.grid(row=3,sticky=W)
        elif (age>=31 and age<=60):
            gmb=(11.6*p) + 879
            gb=str(gmb)
            gb=Label(i,text="GMB="+gb)
            gb.grid(row=3,sticky=W)
        elif (age>60):
            gmb=(13.5*p) + 487
            gb=str(gmb)
            gb=Label(i,text="GMB="+gb)
            gb.grid(row=3,sticky=W)
        #MASC-GET-leve/fator de correção
        if (g1.get()==2):
            get=(gmb*1.55)
            gt=str(get)
            if(g2.get()==5):
                gestante=Label(i,text="[fator inválido-gestante]")
                gestante.grid(row=10)
            elif(g2.get()==6):
                gmb=gmb
            if(age>=13 and age<=15):
                correc=(get*0.13)
                get=(get+correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=13%]")
                fator.grid(row=5,sticky=W)
            elif(age>=16 and age<=19):
                correc=(get*0.05)
                get=(get+correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=50%]")
                fator.grid(row=5,sticky=W)
            elif(age>=40 and age<=49):
                correc=(get*0.05)
                get=(get-correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=-50%]")
                fator.grid(row=5,sticky=W)
            elif(age>=50 and age<=59):
                correc=(get*0.10)
                get=(get-correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=-10%]")
                fator.grid(row=5,sticky=W)
            elif(age>=60 and age<=69):
                correc=(get*0.20)
                get=(get-correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=-20%]")
                fator.grid(row=5,sticky=W)
            elif(age>70):
                correc=(get*0.30)
                get=(get-correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=-30%]")
                fator.grid(row=5,sticky=W)
            else:
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
        #MASC-GET-moderado/fator de correção
        elif (g1.get()==3):
            get=(gmb*1.78)
            gt=str(get)
            if(g2.get()==5):
                gestante=Label(i,text="[fator inválido-gestante]")
                gestante.grid(row=10)
            elif(g2.get()==6):
                gmb=gmb
            if(age>=13 and age<=15):
                correc=(get*0.13)
                get=(get+correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=13%]")
                fator.grid(row=5,sticky=W)
            elif(age>=16 and age<=19):
                correc=(get*0.05)
                get=(get+correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=50%]")
                fator.grid(row=5,sticky=W)
            elif(age>=40 and age<=49):
                correc=(get*0.05)
                get=(get-correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=-50%]")
                fator.grid(row=5,sticky=W)
            elif(age>=50 and age<=59):
                correc=(get*0.10)
                get=(get-correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=-10%]")
                fator.grid(row=5,sticky=W)
            elif(age>=60 and age<=69):
                correc=(get*0.20)
                get=(get-correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=-20%]")
                fator.grid(row=5,sticky=W)
            elif(age>70):
                correc=(get*0.30)
                get=(get-correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=-30%]")
                fator.grid(row=5,sticky=W)
            else:
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
        
        #MASC-GET-intenso/fator de correção
        elif (g1.get()==4):
            get=(gmb*2.10)
            if(g2.get()==5):
                gestante=Label(i,text="[fator inválido-gestante]")
                gestante.grid(row=10)
            elif(g2.get()==6):
                gmb=gmb
            if(age>=13 and age<=15):
                correc=(get*0.13)
                get=(get+correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=13%]")
                fator.grid(row=5,sticky=W)
            elif(age>=16 and age<=19):
                correc=(get*0.05)
                get=(get+correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=50%]")
                fator.grid(row=5,sticky=W)
            elif(age>=40 and age<=49):
                correc=(get*0.05)
                get=(get-correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=-50%]")
                fator.grid(row=4,sticky=W,column=1)
            elif(age>=50 and age<=59):
                correc=(get*0.10)
                get=(get-correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=-10%]")
                fator.grid(row=4,sticky=W,column=1)
            elif(age>=60 and age<=69):
                correc=(get*0.20)
                get=(get-correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=-20%]")
                fator.grid(row=4,sticky=W,column=1)
            elif(age>70):
                correc=(get*0.30)
                get=(get-correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=-30%]")
                fator.grid(row=4,sticky=W,column=1)
            else:
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
            
        #peso ideal masculino
        Pi=(22.0*(h**2))
        pesoI=str(Pi)
        pesoI=Label(i,text="Peso ideal:"+pesoI)
        pesoI.grid(row=6,sticky=W)
        #ganho/perda de peso
        if(Pd>p):
            win=Label(i,text="[ganho de peso]")
            win.grid(row=7,sticky=W)
            porcent=((Pd*100)/p)
            valorcent=porcent-100
            valorstr=str(valorcent)
            cent=Label(i,text="[porcentagem ganho]="+valorstr+"%")
            cent.grid(row=8,sticky=W)
            getG=(get*(porcent/100))
            getT=(get+getG)
            total=str(getT)
            get_ganho=Label(i,text="GET(ganho de peso)="+total)
            get_ganho.grid(row=9,sticky=W)
        else:
            lose=Label(i,text="[perda de peso]")
            lose.grid(row=7,sticky=W)
            porcent=((Pd*100)/p)
            valorcent=porcent-100
            valorstr=str(valorcent)
            cent=Label(i,text="[porcentagem perda]="+valorstr+"%")
            cent.grid(row=8,sticky=W)
            getP=(get*(porcent/100))
            getT=(get-getG)
            total=str(getT)
            get_perda=Label(i,text="GET(perda de peso)="+total)
            get_perda.grid(row=9,sticky=W)



    #GMB-feminino
    if(g.get()==1):
        if (age>=1 and age<=3):
            gmb=(61.0 * p) - 51
            gb=str(gmb)
            gb=Label(i,text="GMB="+gb)
            gb.grid(row=3,sticky=W)
        elif (age>=4 and age<=10):
            gmb=(22.5 * p) + 499
            gb=str(gmb)
            gb=Label(i,text="GMB="+gb)
            gb.grid(row=3,sticky=W)
        elif (age>=11 and age<=18):
            gmb=(12.2*p) + 746
            gb=str(gmb)
            gb=Label(i,text="GMB="+gb)
            gb.grid(row=3,sticky=W)
        elif (age>=19 and age<=30):
            gmb=(14.7*p) + 496
            gb=str(gmb)
            gb=Label(i,text="GMB="+gb)
            gb.grid(row=3,sticky=W)
        elif (age>=31 and age<=60):
            gmb=(8.7*p) + 829
            gb=str(gmb)
            gb=Label(i,text="GMB="+gb)
            gb.grid(row=3,sticky=W)
        elif (age>60):
            gmb=(10.5*p) + 596
            gb=str(gmb)
            gb=Label(i,text="GMB="+gb)
            gb.grid(row=3,sticky=W)
            
        #FEM-GET-leve/fator de correção
        if (g1.get()==2):
            #gestação
            if(g2.get()==5):
                gmb=gmb+200
                gestante=Label(i,text="[gestante]")
                gestante.grid(row=7,sticky=W)
            elif(g2.get()==6):
                gmb=gmb
            #GET    
            get=(gmb*1.56)
            gt=str(get)
            if(age>=13 and age<=15):
                correc=(get*0.13)
                get=(get+correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=13%]")
                fator.grid(row=5,sticky=W)
            elif(age>=16 and age<=19):
                correc=(get*0.05)
                get=(get+correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=50%]")
                fator.grid(row=5,sticky=W)
            elif(age>=40 and age<=49):
                correc=(get*0.05)
                get=(get-correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=-50%]")
                fator.grid(row=5,sticky=W)
            elif(age>=50 and age<=59):
                correc=(get*0.10)
                get=(get-correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=-10%]")
                fator.grid(row=5,sticky=W)
            elif(age>=60 and age<=69):
                correc=(get*0.20)
                get=(get-correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=-20%]")
                fator.grid(row=5,sticky=W)
            elif(age>70):
                correc=(get*0.30)
                get=(get-correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=-30%]")
                fator.grid(row=5)
            else:
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                
        #FEM-GET-moderado/fator de correção   
        elif (g1.get()==3):
            #gestação
            if(g2.get()==5):
                gmb=gmb+285
                gestante=Label(i,text="[gestante]")
                gestante.grid(row=7)
            elif(g2.get()==6):
                gmb=gmb
            #GET
            get=(gmb*1.64)
            gt=str(get)
            if(age>=13 and age<=15):
                correc=(get*0.13)
                get=(get+correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=13%]")
                fator.grid(row=5,sticky=W)
            elif(age>=16 and age<=19):
                correc=(get*0.05)
                get=(get+correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=50%]")
                fator.grid(row=5,sticky=W)
            elif(age>=40 and age<=49):
                correc=(get*0.05)
                get=(get-correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=-50%]")
                fator.grid(row=5,sticky=W)
            elif(age>=50 and age<=59):
                correc=(get*0.10)
                get=(get-correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=-10%]")
                fator.grid(row=5,sticky=W)
            elif(age>=60 and age<=69):
                correc=(get*0.20)
                get=(get-correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=-20%]")
                fator.grid(row=5,sticky=W)
            elif(age>70):
                correc=(get*0.30)
                get=(get-correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=-30%]")
                fator.grid(row=5,sticky=W)
            else:
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
            

        #FEM-GET-intenso/fator de correção
        elif (g1.get()==4):
            #gestação
            if(g2.get()==5):
                msg=Label(i,text="Gestantes não devem fazer atividade intensa")
                msg.grid(row=7,sticky=W)
            elif(g2.get()==6):
                gmb=gmb
            #GET
            get=(gmb*1.82)
            gt=str(get)
            if(age>=13 and age<=15):
                correc=(get*0.13)
                get=(get+correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=13%]")
                fator.grid(row=5,sticky=W)
            elif(age>=16 and age<=19):
                correc=(get*0.05)
                get=(get+correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=50%]")
                fator.grid(row=5,sticky=W)
            elif(age>=40 and age<=49):
                correc=(get*0.05)
                get=(get-correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=-50%]")
                fator.grid(row=5,sticky=W)
            elif(age>=50 and age<=59):
                correc=(get*0.10)
                get=(get-correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=-10%]")
                fator.grid(row=5,sticky=W)
            elif(age>=60 and age<=69):
                correc=(get*0.20)
                get=(get-correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=-20%]")
                fator.grid(row=5,sticky=W)
            elif(age>70):
                correc=(get*0.30)
                get=(get-correc)
                gt=str(get)
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)
                fator=Label(i,text="[correção=-30%]")
                fator.grid(row=5,sticky=W)
            else:
                gt=Label(i,text="GET="+gt)
                gt.grid(row=4,sticky=W)

        #peso ideal feminino   
        Pi=(20.8*(h**2))
        pesoI=str(Pi)
        pesoI=Label(i,text="peso ideal:"+pesoI)
        pesoI.grid(row=6,sticky=W)
        #ganho/perda de peso
        if(Pd>p):
            win=Label(i,text="[ganho de peso]")
            win.grid(row=7,sticky=W)
            porcent=((Pd*100)/p)
            valorcent=porcent-100
            valorstr=str(valorcent)
            cent=Label(i,text="[porcentagem ganho]="+valorstr+"%")
            cent.grid(row=8,sticky=W)
            getG=(get*(porcent/100))
            getT=(get+getG)
            total=str(getT)
            get_ganho=Label(i,text="GET(ganho de peso)-> GET="+total)
            get_ganho.grid(row=9,sticky=W)
        else:
            lose=Label(i,text="[perda de peso]")
            lose.grid(row=7,sticky=W)
            porcent=((Pd*100)/p)
            valorcent=porcent-100
            valorstr=str(valorcent)
            cent=Label(i,text="[porcentagem perda]="+valorstr+"%")
            cent.grid(row=8,sticky=W)
            getP=(get*(porcent/100))
            getT=(get-getG)
            total=str(getT)
            get_perda=Label(i,text="GET(perda de peso)-> GET="+total)
            get_perda.grid(row=9,sticky=W)
        


#variável
g=IntVar()
g1=IntVar()
g2=IntVar()

#Botão-calcular
imc_button=Button(w,text="calcular",command=dados)
imc_button.grid(row=10,columnspan=5)

#Botões 0/1-gênero
gen=Label(w,text="Gênero:")
gen.grid(row=1,sticky=W)
masc=Radiobutton(w,text="masculino",variable=g,value=0,command=calc_masc)
masc.grid(row=2,sticky=W)
fem=Radiobutton(w,text="feminino",variable=g,value=1,command=calc_fem)
fem.grid(row=3,sticky=W)

#Botões 0/1-nível de atividade física
nvf=Label(w,text="Nível de atividade física:")
nvf.grid(row=1,sticky=W,column=1)
opc3 = Radiobutton(w, text = "leve",variable = g1, value = 2, command = leve)
opc3.grid(row=2,sticky=W,column=1)
opc4 = Radiobutton(w, text = "moderado",variable = g1, value = 3, command = medio)
opc4.grid(row=3,sticky=W,column=1)
opc5 = Radiobutton(w, text = "intenso",variable = g1, value = 4, command = intenso)
opc5.grid(row=4,sticky=W,column=1)

#Botão gestante
gest=Checkbutton(w,text="gestante",variable=g2,onvalue=5,offvalue=6,command = gestante)
gest.grid(row=10,sticky=E,column=1)

#Entry/Label-dados de entrada
p=Label(w,text="Peso(Kg):")
p.grid(row=6,sticky=W)
h=Label(w,text="altura(M):")
h.grid(row=7,sticky=W)
peso=Entry(w)
peso.grid(row=6,column=1)
altura=Entry(w)
altura.grid(row=7,column=1)
age=Label(w,text="idade:")
age.grid(row=8,sticky=W)
idade=Entry(w)
idade.grid(row=8,column=1)
pesoD=Label(w,text="Peso desejado(Kg):")
pesoD.grid(row=9,column=0)
peso_d=Entry(w)
peso_d.grid(row=9,column=1)
texto = Text(w,height=0,width=0)
texto.grid(row=10,sticky=W)
w.mainloop()

    
    
    








