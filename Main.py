#Dicionarys for the unique monster typs
essence = {"Frail essence":25,"Robust essence":30,"Potent essence":35,"Mythic essence":40,"Deific essence":50}
aberation = {"antenna":5,"eye":5,"flesh":5,"phial of blood":5,"bone":10,"egg":10,"fat":10,"pouch of claws":10,"pouch of teeth":10,"heart":15,"phial of mucus":15,"liver":15,"stinger":15,"tentacle":15,"brain":20,"chitin":20,"hide":20,"main eye":20}
beast = {"antenna":5,"eye":5,"flesh":5,"phial of blood":5,"antler":10,"beak":10,"bone":10,"egg":10,"fat":10,"fin":10,"horn":10,"pincer":10,"pouch of claws":10,"pouch of teeth":10,"talon":10,"tusk":10,"heart":15,"liver":15,"poison gland":15,"pouch of feathers":15,"pouch of scales":15,"stinger":15,"tentacle":15,"chitin":20,"pelt":20}
celestial = {"eye":5,"flesh":5,"phial of blood":5,"pouch of dust":5,"bone":10,"fat":10,"horn":10,"pouch of teeth":10,"heart":15,"liver":15,"pouch of feathers":15,"pouch of scales":15,"brain":20,"skin":20,"soul":25}
construct = {"phial of blood":5,"phial of oil":5,"phial of sap":5,"pouch of dust":5,"flesh":10,"metal plating":10,"stone":10,"bone":15,"heart":15,"liver":15,"gears":15,"brain":20,"instructions":20,"lifespark":25}
dragon = {}
elemental = {}
fey = {}
fiend = {}
gigant = {}
humanoid = {}
monstrosity = {}
ooze = {}
plant = {}
undead = {}
    
#UserInput of Type and Components
type = ""
components = ""
def usr_input():
    type = input("Type: ")
    components = input("Conponents: ")
    type = type.replace("Type:","")
    components = components.replace("Conponents:","")
    #print(components,type)
    return type,components
    

class Calculator():
    
    def __init__(self):
        type,components = usr_input()
        #type,components = inp
        self.type = type
        self.components = components
        self.type_dict = {}
        self.comp_list = "Component List:"
        self.DC = 0
        self.DC_calc = "DC Calc: "
    
    def typ_check(self):
        print(type,components)
        if self.type == "Aberation" or "aberation":
            self.type_dict = aberation
            print(self.type_dict) 
        elif self.type == "beast" or "Beast":
            self.type_dict = beast
            print(self.type_dict) 
        elif self.type == "celestial" or "Celestial":
            self.type_dict = celestial
            print(self.type_dict) 
        elif self.type == "construct" or "Celestial":
            self.type_dict = construct
            print(self.type_dict) 
        elif self.type == "dragon"or"Dragon":
            self.type_dict = dragon
            print(self.type_dict)  
        else:
            return "No Type Found"
        
    def calculation(self):
        print(self.components)
        single_comp = []
        single_comp = self.components.split(",")
        for i in range(0,len(single_comp)):
            #print(single_comp[i])
            if single_comp[i] in self.type_dict:
                self.DC += self.type_dict[single_comp[i]]    
                self.comp_list = self.comp_list + " " + str(single_comp[i])
                self.DC_calc = self.DC_calc + "+" + str(self.type_dict[single_comp[i]])
            
            else:
                continue
        return print(str(self.DC) + "\n" + str(self.DC_calc) + "\n" + str(self.comp_list) + "\n")
            




if __name__ == "__main__":
    tom = Calculator()
    tom.typ_check()
    tom.calculation()
    #print(tom)
    