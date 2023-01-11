#Dicionarys for the unique monster typs
essence = {"Frail essence":25,"Robust essence":30,"Potent essence":35,"Mythic essence":40,"Deific essence":50}
aberation = {"antenna":5,"eye":5,"flesh":5,"phial of blood":5,"bone":10,"egg":10,"fat":10,"pouch of claws":10,"pouch of teeth":10,"heart":15,"phial of mucus":15,"liver":15,"stinger":15,"tentacle":15,"brain":20,"chitin":20,"hide":20,"main eye":20}
beast = {"antenna":5,"eye":5,"flesh":5,"phial of blood":5,"antler":10,"beak":10,"bone":10,"egg":10,"fat":10,"fin":10,"horn":10,"pincer":10,"pouch of claws":10,"pouch of teeth":10,"talon":10,"tusk":10,"heart":15,"liver":15,"poison gland":15,"pouch of feathers":15,"pouch of scales":15,"stinger":15,"tentacle":15,"chitin":20,"pelt":20}
celestial = {"eye":5,"flesh":5,"phial of blood":5,"pouch of dust":5,"bone":10,"fat":10,"horn":10,"pouch of teeth":10,"heart":15,"liver":15,"pouch of feathers":15,"pouch of scales":15,"brain":20,"skin":20,"soul":25}
construct = {"phial of blood":5,"phial of oil":5,"phial of sap":5,"pouch of dust":5,"flesh":10,"metal plating":10,"stone":10,"bone":15,"heart":15,"liver":15,"gears":15,"brain":20,"instructions":20,"lifespark":25}
dragon = {"eye":5,"flesh":5,"phial of blood":5,"bone":10,"fat":10,"pouch of claws":10,"pouch of teeth":10,"horn":15,"liver":15,"pouch of scales":15,"heart":20,"breath sac":25}
elemental = {"eye":5,"primordial dust":5,"bone":10,"volatile mote of air":15,"volatile mote of earth":15,"volatile mote of fire":15,"volatile mote of water":15,"core of air":25,"core of earth":25,"core of fire":25,"core of water":25}
fey = {"antenna":5,"eye":5,"flesh":5,"phial of blood":5,"antler":10,"beak":10,"bone":10,"egg":10,"horn":10,"pouch of claws":10,"pouch of teeth":10,"talon":10,"tusk":10,"heart":15,"fat":15,"liver":15,"poison gland":15,"pouch of feathers":15,"pouch of scales":15,"tentacle":15,"tongue":15,"brain":20,"skin":20,"pelt":20,"psyche":25}
fiend = {"antenna":5,"eye":5,"flesh":5,"phial of blood":5,"pouch of dust":5,"bone":10,"horn":10,"pouch of teeth":10,"heart":15,"fat":15,"liver":15,"poison gland":15,"pouch of feathers":15,"pouch of scales":15,"brain":20,"skin":20,"soul":25}
giant = {"flesh":5,"nail":5,"phial of blood":5,"bone":10,"fat":10,"tooth":10,"heart":15,"liver":15,"skin":20}
humanoid = {"eye":5,"phial of blood":5,"bone":10,"egg":10,"pouch of teeth":10,"heart":15,"liver":15,"pouch of feathers":15,"pouch of scales":15,"brain":20,"skin":20}
monstrosity = {"antenna":5,"eye":5,"flesh":5,"phial of blood":5,"antler":10,"beak":10,"bone":10,"egg":10,"fat":10,"fin":10,"horn":10,"pincer":10,"pouch of claws":10,"pouch of teeth":10,"talon":10,"tusk":10,"heart":15,"liver":15,"poison gland":15,"pouch of feathers":15,"pouch of scales":15,"stinger":15,"tentacle":15,"chitin":20,"pelt":20}
ooze = {"phial of acid":5,"phial of mucus":10,"vesicle":15,"membrane":20}
plant = {"phial of sap":5,"tuber":5,"bundle of roots":10,"phial of wax":10,"pouch of hyphae":10,"pouch of leaves":10,"poison gland":15,"pouch of pollen":15,"pouch of spores":15,"bark":20,"fungal membrane":20}
undead = {"eye":5,"bone":5,"phial of congealed blood":5,"marrow":10,"pouch of teeth":10,"rancid fat":10,"ethereal ichor":15,"undying flesh":15,"undying heart":20}

#Dropdown Menue for Type Selection
type_selection = [aberation,beast,celestial,construct,dragon,elemental,fey,fiend,giant,humanoid,monstrosity,ooze,plant,undead]

#Essence Harvesting Variables: 
monster_type = ""
components = {}
monster_CR = 0
monster_components = ""

class HarvestCalculator():
    
    
    def __init__(self) -> None:
        self.essence = essence
        self.monster_type = monster_type
        self.monster_CR = monster_CR
        self.monster_components = monster_components
        self.components = components
        self.type_dict = {}
        self.comp_list = "Component List: "
        self.DC = 0
        self.DC_calc = "DC Calculation: "
        
        
    #UserInput:
    def usr_input(self):
        self.monster_type = input("Monster Type: ")
        self.monster_CR = input("Monster CR: ")
        self.monster_components = input("Monster Conponents: ")
        self.monster_type = self.monster_type.replace("Type:","")
        self.monster_CR = self.monster_CR.replace("Monster CR: ","")
        self.monster_components = self.monster_components.replace("Monster Conponents: ","")
        self.calculation()
        return int(self.monster_CR),self.monster_type,self.monster_components

    def calc_essence(self):
        self.monster_CR = int(self.monster_CR)
        for k,v in self.essence.items():
            if self.monster_CR <= 6 and self.monster_CR >= 3 and k == "Frail essence":
                self.components[k] = v
                return "Frail essence"
            elif self.monster_CR <= 11 and self.monster_CR >= 7 and k == "Robust essence":
                self.components[k] = v
                return "Robust essence"
            elif self.monster_CR <= 17 and self.monster_CR >= 12 and k == "Potent essence":
                self.components[k] = v
                return "Potent essence"
            elif self.monster_CR <= 24 and self.monster_CR >= 18 and k == "Mythic essence":
                self.components[k] = v
                return "Mythic essence"
            elif self.monster_CR >= 25 and k == "Deific essence":
                self.components[k] = v
                return "Deific essence"
            #else:
            #    return None
            
             
    #Replaces input Essence with Key form Essence Dict   
    def replace_essence (self):
        self.monster_components = self.monster_components.split(",")
        for i in range(0,len(self.monster_components)):
            if self.monster_components[i] == "essence":
                self.monster_components[i] = self.calc_essence()

    
    def build_comp_dict(self):
        self.replace_essence()
        self.type_dict = self.typ_check()
        for k ,v in self.type_dict.items():
            if k in self.monster_components:
                self.components[k] = v
            else:
                continue
        return self.components
    
    def comp_print(self):
        print(self.components)
        print(self.monster_components)
        
    
    
    
    def typ_check(self):
        if self.monster_type == "Aberation" or "aberation":
            self.type_dict = aberation
            return self.type_dict 
        elif self.monster_type == "beast" or "Beast":
            self.type_dict = beast
            return self.type_dict  
        elif self.monster_type == "celestial" or "Celestial":
            self.type_dict = celestial
            return self.type_dict  
        elif self.monster_type == "construct" or "Celestial":
            self.type_dict = construct
            return self.type_dict  
        elif self.monster_type == "dragon"or"Dragon":
            self.type_dict = dragon
            return self.type_dict     
        elif self.monster_type == "elemental"or"Elemental":
            self.type_dict = elemental
            return self.type_dict 
        elif self.monster_type == "fey"or"Fey":
            self.type_dict = fey
            return self.type_dict 
        elif self.monster_type == "fiend"or"Fiend":
            self.type_dict = fiend
            return self.type_dict 
        elif self.monster_type == "giant"or"Giant":
            self.type_dict = giant
            return self.type_dict 
        elif self.monster_type == "humanoid"or"Humanoid":
            self.type_dict = humanoid
            return self.type_dict 
        elif self.monster_type == "monstrosity"or"Monstrosity":
            self.type_dict = monstrosity
            return self.type_dict 
        elif self.monster_type == "ooze"or"Ooze":
            self.type_dict = ooze
            return self.type_dict 
        elif self.monster_type == "plant"or"Plant":
            self.type_dict = plant
            return self.type_dict 
        elif self.monster_type == "undead"or"Undead":
            self.type_dict = undead
            return self.type_dict 
        else:
            return "No Type Found"

    def calculation(self):
        self.build_comp_dict()
        for i in range(0,len(self.monster_components)):
                if self.monster_components[i] in self.components:
                    self.DC += self.components[self.monster_components[i]]    
                    self.comp_list = self.comp_list  + str(self.monster_components[i]).capitalize()+ " , "
                    self.DC_calc = self.DC_calc + str(self.components[self.monster_components[i]]) + "+"
                
        return print("\n" + "Monster Type : "+ str(self.monster_type).capitalize()+"\n" +"DC: " + str(self.DC) + "\n" + str(self.DC_calc[0:-1]) + "\n" + str(self.comp_list[0:-2]) + "\n")




if __name__ == "__main__":
    a = HarvestCalculator()
    a.usr_input()
    
    
    
   
   