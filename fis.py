class MFunction:
    def __init__(self, mftype, parameters):
        self.type = mftype
        self.parameters = parameters #dictionary
    def calc(self, x):
        a = self.parameters('a')
        b = self.parameters('b')
        if self.parameters('c'):
            c = self.parameters('c')
        if self.parameters('d'):
            self.parameters('d')


        if self.name == "Pfunc":
            if x <= a:
                return 0
            elif a <= x <= b:
                return (x - a)/(b - a)
            elif b <= x <= c:
                return 1
            elif c <= x <= d:
                return (d - x)/(d - c)
            elif x >= d:
                return 0

        elif self.name == "Afunc":
            if x <= a:
                return 0
            elif a <= x <= b:
                return (x - a)/(b - a)
            elif b <= x <= c:
                return (c - x)/(c - b)
            elif c >= x :
                return 0

        elif self.name == "Zfunc":
            if x <= a:
                return 1
            elif a <= x <= b:
                return (b - x)/(b - a)
            elif x >= b:
                return 0

        elif self.name == "Sfunc":
            if x <= a:
                return 0
            elif a <= x <= b:
                return (b - x)/(b - a)
            elif x >= b:
                return 1

        if self.name == "GPfunc":
            if x <= a:
                return 0
            elif a <= x <= (a+b)/2:
                return 2*((x - a)/(b - a))**2
            elif (a + b)/2 <= x <= b:
                return 1 - 2*((b - x)/(b - a))**2
            elif b <= x <= c:
                return 1
            elif c <= x <= (c + d)/2:
                return 1 - 2*((x - c)/(d - c))**2
            elif (c + d)/2 <= x <= d:
                return 2*((x - c)/(d - c))**2
            elif x >= d:
                return 0

        elif self.name == "GAfunc":
            if x <= a:
                return 0
            elif a <= x <= (a + b)/2:
                return 2*((x - a)/(b - a))**2
            elif (a + b)/2 <= x <= b:
                return 1 - 2*((b - x)/(b - a))**2
            elif b <= x <= (b + c)/2:
                return 1 - 2*((x - b)/(c - b))**2
            elif (b + c)/2 <= x <= c:
                return 2*((c - x)/(c - b))**2
            elif x >= c :
                        return 0

        elif self.name == "GZfunc":
            if x <= a:
                return 1
            elif a <= x <= (a + b)/2:
                return 1 - 2*((x - a)/(b - a))**2
            elif (a + b)/2 <= x <= b:
                return 2*((b - x)/(b - a))**2
            elif x >= b :
                return 0

        elif self.name == "GZfunc":
            if x <= a:
                return 1
            elif a <= x <= (a + b)/2:
                return 2*((x - a)/(b - a))**2
            elif (a + b)/2 <= x <= b:
                return 1 - 2*((b - x)/(b - a))**2
            elif x >= b :
                return 0


class LTerms:
    def __init__(self, name, value, mf):
        self.name = name
        self.value = value
        self.mf = mf # MFunction-object


class MFValue:
    def __init__(self, arg, value):
        self.arg = arg # somewhere must be filled
        #take the size of array, разбиваем на н частей (100 или 300)
        #и записываем каждую точку деления, и для каждого н находим значение
        #с шагом который получился от деления и с шагом 
        self.value = value


class Variable:
    def __init__(self, name = "", value = None, leftB = None, rightB = None, lterms = [], mfvalues = []):
        self.name = name
        self.value = value
        self.leftB = leftB
        self.rightB = rightB
        self.lterms = lterms # list of LTterm-objects


class Literal:
    def __init__(self, varname, ltname, neg, value):
        self.varname = varname
        self.ltname = ltname
        self.neg = neg
        self.value = value
    def calc(self, inputs):
        self.value = inputs(self.varname).lterms(self.ltname).value
        if self.neg:
            self.value = 1 - self.value


class Conjuct:
    def __init__(self, literals, value):
        self.literals = literals #list
        self.value = value
    def calc(self, inputs):
        self.value = 1
        for l in self.literals:
            l.calc(inputs)
            self.value = min(me.value, l.value)


class Disjunct:        
    def __init__(self, conjuncts, value):
        self.conjuncts = conjuncts #list
        self.value = value
    def calc(self, inputs):
        for c in self.conjuncts:
            c.calc(inputs)
            self.value = max(self.value, c.value)



class Production:
    def __init__(self, antecendent, consequent,bf):
        self.antecendent = antecendent #disjunct
        self. consequent = consequent # literal
        self.bf = bf

class Parameter:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class FIS:
    def __init__(self, inputs, outputs, productions, parameters):
        self.inputs = inputs #list of variables
        self.outputs = outputs #list of varibles
        self.productions = productions #list of productions
        self.parameters = parameters #list of parameters
    def DefuzzMeth(self, mfvalues):
        # Yvalue = (sum of all arg*values from mfvalues)/sum of values from mfvalues        numerator = 0
        # Y - output variable
        # value = mfunc(arg)
        # args - Y domen
        if "centroid method":
            numerator = 0
            denominator = 0
            for x in mfvalues:
                numerator += x.arg*x.value
                denominator += x.value
        return numerator/denominator

    def Fuzzyfication(self):
        for x in self.inputs:
            for l in x.lterms:
                l.value = l.mf.calc(x.value)
    def Agregation(self):
        for p in productions:
            p.antecendent.calc(self.inputs)
    def Activation(self):
        for p in productions:
            p.consequent.value = min(p.antecendent.value, p.bf)
    def CutAndUnion(self):
        for y in outputs:
            for m in y.mfvalues:
                m.value = 0
                for l in y.lterms:
                    m.value = max(m.value, min(l.mf.calc(m.arg), l.value))

    def Defuzzification(self):
        for y in outputs:
            y.value = DefuzzMeth(y.mfvalues)        

    def CreateArgs(self, var, amount):
        interval = var.rightB - var.leftB
        step = interval/amount
        mfvalues = []
        i = leftB
        while i <= rightB:
            mfvalue = MFValue(i,0)
            mfvalues.append(mfvalue)
            i += step
        return mfvalues





