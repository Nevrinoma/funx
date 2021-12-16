def arithmetic(a:float,b:float,c:str):
    if c in ["+","-","/","*"]:
        if c == "/" and b == 0:
            vastus="Div/0"
        else:
            vastus=eval(str(a)+c+str(b))
    else:
        print("Viga.")

def season(kuu:int)->str:
    """Võtame kuu number ja tagastame tekst:Talv;Kevad;Suvi;Sügis."""
    if kuu>=1 and kuu<=12:
        if kuu in[1,2,12]:
            s="Talv"
        elif kuu in[3,4,5]:
            s="Kevad"
        elif kuu in[6,7,8]:
            s="Suvi"
        elif kuu in[9,10,11]:
            s="Sügis"
        break
    else:
        kuu=int(input("-"))
    return s

def bank(a:float,years:int)->float:
    for i in range(years):
        a*=1.1
    return a

def is_prime(number:int)->bool:
    t=0
    for i in range(1,number+1):
        if number%i==0: t+=1
    if t==2:
        t=True
    else:
        t=False
    return t
