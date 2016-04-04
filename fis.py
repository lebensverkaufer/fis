class MFunction:

    def __init__(self, mftype, parameters):
        self.type = mftype
        self.parameters = parameters #list

    def calc(self, x, a, b, c, d):
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
        self.mf = mf


class MFValue:
    def __init__(self, arg, value):
        self.arg = arg
        self.value = value


class Variable:
    def __init__(self, name, value, leftB, rightB, mfvalues):
        self.name = name
        self.value = value
        self.leftB = leftB
        self.rightB = rightB
        self.mfvalues = mfvalues


class Literal:
	def __init__(self, varname, ltname, neg, value):
        self.varname = varname
        self.ltname = ltname
        self.neg = neg
        self.value = value
    def calc(self, inputs): #нужен поиск и по ключу, и по индексу
    	#self.value = inputs


class Conjuct:
	def __init__(self, literals, value):
        self.literals = literals #list
        self.value = value
    def calc(self):


class Disjunct:        
    def __init__(self, conjuncts, value):
        self.conjuncts = conjuncts #list
        self.value = value
    def calc(self):


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
	def DefuzzMeth(self):
	def Fuzzyfication(self):
#	def Agregation(self):
	def Activation(self):
	def Accumulation(self):
	def CutAndUnion(self):
	def Defuzzification(self):
