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
    
def essence_harvesting():
    harvest_essence = input("Do you want to Harvest the Essence of the Monster? Y/N ")
    if harvest_essence == "Y" or "y":
        monster_Cr = input("CR of the Monster: ")
        monster_Cr = monster_Cr.lstrip("CR of the Monster: ")
        if monster_Cr.isnumeric() == False:
            return print("Is not a Number please input a Number!")
        else:
            #Check for Essence Quality
            if monster_Cr <= 12:
                pass
    else:
        pass

    
    
class Calculator():
    
    def __init__(self):
        type,components = usr_input()
        self.type = type
        self.components = components
        self.type_dict = {}
        self.comp_list = "Component List: "
        self.DC = 0
        self.DC_calc = "DC Calculation: "
    #Checks if inputed type is in the Selection and Selects the Dictionary for further processing
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
        elif self.type == "elemental"or"Elemental":
            self.type_dict = elemental
            print(self.type_dict) 
        elif self.type == "fey"or"Fey":
            self.type_dict = fey
            print(self.type_dict) 
        elif self.type == "fiend"or"Fiend":
            self.type_dict = fiend
            print(self.type_dict)
        elif self.type == "giant"or"Giant":
            self.type_dict = giant
            print(self.type_dict)
        elif self.type == "humanoid"or"Humanoid":
            self.type_dict = humanoid
            print(self.type_dict)
        elif self.type == "monstrosity"or"Monstrosity":
            self.type_dict = monstrosity
            print(self.type_dict)
        elif self.type == "ooze"or"Ooze":
            self.type_dict = ooze
            print(self.type_dict)
        elif self.type == "plant"or"Plant":
            self.type_dict = plant
            print(self.type_dict)
        elif self.type == "undead"or"Undead":
            self.type_dict = undead
            print(self.type_dict)
        else:
            return "No Type Found"
    #Calculates the DC and outputs the DC, DC Calculation and The List of Selected Items.     
    def calculation(self):
        print(self.components)
        single_comp = []
        single_comp = self.components.split(",")
        for i in range(0,len(single_comp)):
            #print(single_comp[i])
            if single_comp[i] in self.type_dict:
                self.DC += self.type_dict[single_comp[i]]    
                self.comp_list = self.comp_list  + str(single_comp[i]).capitalize()+ ","
                self.DC_calc = self.DC_calc + str(self.type_dict[single_comp[i]]) + "+"
                
                
                
            else:
                continue
        
        return print("Monster Type : "+str(self.type.capitalize())+"\n" +"DC: " + str(self.DC) + "\n" + str(self.DC_calc[0:-1]) + "\n" + str(self.comp_list[0:-1]) + "\n")
        
            
class GUInput():
    def __init__(self) -> None:
        pass


if __name__ == "__main__":
    essence_harvesting()
    #cal = Calculator()
    #cal.typ_check()
    #cal.calculation()
    #print(tom)
    