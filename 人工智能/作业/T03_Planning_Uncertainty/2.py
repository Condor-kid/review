class VariableElimination():
    @staticmethod
    def inference(factorList, queryVariables,
    orderedListOfHiddenVariables, evidenceList):
        #restrict factor related to evidence
        for ev in evidenceList:
            for i in range(len(factorList)):
                if ev in factorList[i].varList:
                    # restrict
                    factorList[i] = factorList[i].restrict(ev,evidenceList[ev])
        #multiply factor related to the variable
        for var in orderedListOfHiddenVariables:
            # factor related to the variable
            f_list = [f for f in factorList if var in f.varList]
            # error
            if not f_list:
                return None
            # multiply factor and then sumout
            g = f_list[0]
            for f in f_list[1:]:
                # multiply factor on var
                g = g.multiply(f)
            g = g.sumout(var)
            # remove factor f1, f2, f3...fn
            factorList = [factor for factor in factorList if factor not in f_list]
            # add factor g
            factorList.append(g)
        # print ("RESULT:")
        res = factorList[0]
        for factor in factorList[1:]:
            res = res.multiply(factor)
        total = sum(res.cpt.values())
        res.cpt = {k: v/total for k, v in res.cpt.items()}
        # res.printInf()
        return res.cpt
    @staticmethod
    def printFactors(factorList):
        for factor in factorList:
            factor.printInf()

class Node():
    def __init__(self, name, var_list):
        self.name = name
        self.varList = var_list
        self.cpt = {}
    def setCpt(self, cpt):
        self.cpt = cpt
    def printInf(self):
        print ("Name = " + self.name)
        print (" vars " + str(self.varList))
        for key in self.cpt:
            print ("   key: " + str(key) + " val : " , str(self.cpt[key]))
        print ("")
    def multiply(self, factor):
        """function that multiplies with another factor on variables"""
        def equal(key1, key2, indexs1, indexs2):
            for i in range(len(indexs1)):
                if key1[indexs1[i]] != key2[indexs2[i]]:
                    return False
            return True
        def get_new_key(key1, indexs1):
            new_key = [key1[i] for i in range(len(key1)) if i not in indexs1]
            new_key = tuple(new_key)
            return new_key

        variables = [var for var in self.varList if var in factor.varList]
        # variable location
        indexs1 = [self.varList.index(var) for var in variables]
        indexs2 = [factor.varList.index(var) for var in variables]
        # newList and new_cpt
        newList = [var for var in self.varList if var not in variables] + factor.varList
        new_cpt = {}
        for key1,val1 in self.cpt.items():
            for key2,val2 in factor.cpt.items():
                # the same value on variables, multiply
                if equal(key1, key2, indexs1, indexs2):
                    new_key = get_new_key(key1,indexs1)+ key2
                    new_cpt[new_key] = val1 * val2
        new_node = Node("f" + str(newList), newList)
        new_node.setCpt(new_cpt)
        return new_node
    def sumout(self, variable):
        """function that sums out a variable given a factor"""
        if len(self.varList) == 1:
            return None
        # variable location
        var_index = self.varList.index(variable)
        new_var_list = self.varList[:var_index] + self.varList[var_index+1:]
        new_cpt = {}
        new_keys = {key[:var_index] + key[var_index+1:] for key in self.cpt}
        values = {key[var_index] for key in self.cpt}
        for new_key in new_keys:
            probas = [self.cpt[new_key[:var_index]+(val,)+new_key[var_index:]] for val in values]
            # sumout
            new_cpt[new_key] = sum(probas)
        new_node = Node("f" + str(new_var_list), new_var_list)
        new_node.setCpt(new_cpt)
        return new_node
    def restrict(self, variable, value):
        """function that restricts a variable to some value
        in a given factor"""
        # variable location
        var_index = self.varList.index(variable)
        new_var_list = self.varList[:var_index] + self.varList[var_index+1:]
        new_cpt = {}
        for key,val in self.cpt.items():
            if key[var_index] == value:
                new_key = key[:var_index] + key[var_index+1:]
                # restrict
                new_cpt[new_key] = val
        new_node = Node("f" + str(new_var_list), new_var_list)
        new_node.setCpt(new_cpt)
        return new_node

# create nodes for Bayes Net
A = Node('A',['A'])
B = Node('B',['A','B'])
C = Node('C',['A','C'])
D = Node('D',['B','C','D'])
E = Node('E',['C','E'])
# Generate cpt for each node
A.setCpt({('1',):0.2,('0',):0.8})
B.setCpt({('1','1'):0.7,('1','0'):0.3,('0','1'):0.2,('0','0'):0.8})
C.setCpt({('1','1'):0.2,('1','0'):0.8,('0','1'):0.05,('0','0'):0.95})
D.setCpt({('1','1','1'):0.8,('1','1','0'):0.2,('1','0','1'):0.7,('1','0','0'):0.3,('0','1','1'):0.7,('0','1','0'):0.3,('0','0','1'):0.05,('0','0','0'):0.95})
E.setCpt({('1','1'):0.7,('1','0'):0.3,('0','1'):0.6,('0','0'):0.4})

Distribution = VariableElimination.inference([A,B,C,D,E],['A','B','C'],[],{'D':'0','E':'1'})
print(Distribution)

Distribution2 = VariableElimination.inference([A,B,C,D,E],['A',],['B','C'],{'D':'0','E':'1'})
print(Distribution2)
