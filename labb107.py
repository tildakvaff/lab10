#DENNA FUNGERAR NU MED NEXT-PEKARE

from kön import *
from sys import stdin
from molgrafik import *

class Ruta:

    def __init__(self, atom = "()", num = 1):
        self.atom = atom
        self.num = num
        self.next=None
        self.down=None




class Syntaxfel(Exception):
    pass
atomlagring = LinkedQ()

def readformel(q):
    print("1a")
    mol = readmol(q) 
    return mol




def readmol(q):
    print("50a")
    mol = readgroup(q)
    if q.peek() != "&":
        print("51a")
        mol.next = readmol(q)
    print("52a")
    return mol
    
    



def readgroup(q):
    print("4a")
    rutan = Ruta()
    

    #Fall 1
    if q.peek().isnumeric() == True:
        print("5a")
        raise Syntaxfel(f'Felaktig gruppstart vid radslutet {restutskrivare(q)}')
    
    #Fall 2
    if q.peek() == "(":
        print("6a")
        q.dequeue()        
        while q.peek() != ")":   
            print("7a")                                                               
            if q.peek() == "&":    
                print("8a")
                raise Syntaxfel(f'Saknad högerparentes vid radslutet {restutskrivare(q)}')
            

            print("80a")
            rutan.down = readgroup(q) 
                                                                                         
        q.dequeue()                               
        if q.peek().isnumeric() != True: 
            print("9a")
            raise Syntaxfel(f'Saknad siffra vid radslutet {restutskrivare(q)}')
        else:
            print("60")
            rutan.num = readnum(q)
            return rutan 

    
    #Fall 3
    elif q.peek() == ")":
        print("10a")
        raise Syntaxfel(f'Felaktig gruppstart vid radslutet {restutskrivare(q)}')


    #Fall 4
    if q.peek().isalpha() == True:
        print("11a") 
        if q.peek().islower() == True:
            print("12a")
            raise Syntaxfel(f'Saknad stor bokstav vid radslutet {restutskrivare(q)}')
        if q.peek().isupper() == True:
            print("13a")
            värde = readatom(q)
            rutan.atom = värde
            print("det returnerade värdet från readatom sätts som rutan.atom är " + värde)
        try:
            print("14a")
            int(q.peek())
            rutan.num = readnum(q)
            print("40a")
        except (ValueError, TypeError): None


        print("ute ur readgroup, nästa tecken i molekylen är: " + q.peek())
        print("numret är "+ str(rutan.num))
        print("atomen är " +rutan.atom)
        return rutan





def readnum(q):
    #Om siffran är en 1a
    if q.peek() == "1":
        print("15a")
        q.dequeue()
        if q.peek().isnumeric() == False:               
            print("16a")
            raise Syntaxfel(f'För litet tal vid radslutet {restutskrivare(q)}')
        if q.peek().isnumeric() == True:                

            print("17a")
            siffersträng = "1"
            while q.peek().isnumeric() == True:            
                siffersträng += q.dequeue()
            int_siffersträng=int(siffersträng)
            
            return int_siffersträng
    
    #Om siffran är en 0a        
    if q.peek() == "0":         
        print("18a")
        q.dequeue()                                 
        raise Syntaxfel(f'För litet tal vid radslutet {restutskrivare(q)}')
    
    #Om siffran är större än 1
    else: 
        print("19a")
        siffersträng = ""
        while q.peek().isnumeric() == True:
            siffersträng += q.dequeue()
        int_siffersträng=int(siffersträng)
        
        return int_siffersträng
    


def readatom(q):
    print("22a")
    atomlagring = LinkedQ()
    atomlagring.enqueue(q.dequeue())
    if q.peek().isalpha() == True:    
        print("23a")   
        if q.peek().islower():
            atomlagring.enqueue(q.dequeue())
    atomlagring.enqueue("$")
    atomstr = atomcheck(atomlagring,q)
    return atomstr

def atomcheck(atomlagring,q):
    print("24a")
    #print("ATOMCHECK")
    atomlista= ["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y",
            "Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir",
            "Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Fl","Lv"]
    atomstr = ""
    #print("atomlagringspeeken är "+atomlagring.peek())
    while atomlagring.peek() != "$":
        
        print("25a")
        atomstr += atomlagring.dequeue()
    if atomstr in atomlista:
        print("26a")
        return atomstr

    else:
        print("27a")
        raise Syntaxfel(f'Okänd atom vid radslutet {restutskrivare(q)}')

def restutskrivare(q):
    radslut = ""
    while not q.peek() =="&":
        print("28a")
        radslut += str(q.dequeue())
    return radslut
########################################################################################################################################################################


def dela_upp_molekyl(molekyl):
        q = LinkedQ()
        for varje_tecken in molekyl:
                q.enqueue(varje_tecken)
        q.enqueue("&")
        kollamolekyl(q)
        

def kollamolekyl(q):
    try:
        mol = readformel(q)
        print("Formeln är syntaktiskt korrekt")
        mg = Molgrafik()
        mg.show(mol)
        
    except Syntaxfel as fel:
        print(str(fel))



def main():
    molekyl = input("skriv molekyl: ")
    dela_upp_molekyl(molekyl)

  

if __name__ == "__main__":
    main()
