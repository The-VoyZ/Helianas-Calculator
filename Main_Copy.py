#Dicionarys for the unique monster typs
essence = {"Frail essence":25,"Robust essence":30,"Potent essence":35,"Mythic essence":40,"Deific essence":50}
aberation = {"antenna":5,"Eye":5,"flesh":5,"phial of blood":5,"bone":10,"egg":10,"fat":10,"pouch of claws":10,"pouch of teeth":10,"heart":15,"phial of mucus":15,"liver":15,"stinger":15,"tentacle":15,"brain":20,"chitin":20,"hide":20,"main eye":20}
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
type_dict = {}
def usr_input():
    type = input("Type: ")
    type = type.replace("Type: ","")
    components = input("Conponents: ")
    components = components.replace("Conponents:","")
    



    
def typ_check():
        if type == "Aberation" or "aberation":
            type_dict = aberation
            return print(type_dict)     
        
        
def calculation(self,type,components):
        
        for i in self.type:
            if self.components in type:
                print(i)
            else:
                continue


if __name__ == "__main__":
    usr_input()
    typ_check()