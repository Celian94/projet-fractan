class Fraction :
    def __init__(self, numérateur, dénominateur):
        if dénominateur == 0:
            raise ValueError
        self.numérateur=numérateur
        self.dénominateur=dénominateur
    def est_entier(self, n):
        return (type(n/(self.dénominateur))==int)
    def valeur(self, n):
        return (self.numérateur*n//(self.dénominateur))

class Facteur :
    def __init__(self, facteurs: list[int]):
        self.facteurs=facteurs
    def nombre(self, L):
        a=1
        for i in range(len(L)):
            a=a*(self.facteurs[i]**L[i])
        return a
    def décomposition(self,n):
        L=[0]*len(self.facteurs)
        for i in range(len(self.facteurs)):
            while n%self.facteurs[i]==0:
                L[i]+=1
                n=n//self.facteurs[i]
        return L

class Fractran:
    def __init__(self, programme):
        self.programme = programme
    def run(self, n):
        i = 0
        while i < len(self.programme):
            if self.programme[i].est_entier(n):
                n = self.programme[i].valeur(n)
                i = 0
            else:
                i += 1
        return n

    def suite(self, n: int, N: int):
        L = [n]
        i=0
        while i < len(self.programme) and len(L) < N:
            if self.programme[i].est_entier(n):
                n = self.programme[i].valeur(n)
                L.append(n)
                i = 0
            else:
                i += 1
                
        return L