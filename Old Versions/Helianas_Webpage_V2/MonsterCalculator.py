from Monster_Dictionarys import type_selection , essence

class HarvestCalculator():
    
    
    def __init__(self,monster_CR,monster_type,monster_components) -> None:
        self.essence = essence
        self.monster_type = monster_type
        self.monster_CR = monster_CR
        self.monster_components = monster_components
        self.components = {}
        self.type_dict = {}
        self.comp_list = "Component List: "
        self.DC = 0
        self.DC_calc = "DC Calculation: "
        
        
        
    #Calculates the Type of Essence for the Spesific Monster CR
    def calc_essence(self):
        self.monster_CR = int(self.monster_CR)
        for k,v in self.essence.items():
            if self.monster_CR <= 6 and self.monster_CR >= 0 and k == "Frail essence":
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
            
             
    #Replaces input Essence with Key form Essence Dict   
    def replace_essence (self):
        
        #self.monster_components = self.monster_components.split(",")
        
        #self.monster_components = list(map(lambda x: x.replace('essence', self.calc_essence()), self.monster_components))
        for i in range(0,len(self.monster_components)):
            if self.monster_components[i] == "essence":
                self.monster_components[i] = self.calc_essence()

    #Builds a new Dict from the User inputed Components for use in The Calculation
    def build_comp_dict(self):
        self.replace_essence()
        self.type_dict = self.typ_check()
        for k ,v in self.type_dict.items():
            if k in self.monster_components:
                self.components[k] = v
            else:
                continue
        return self.components
    
    #Selects the right dictionary for the Spesific Monster Typ 
    def typ_check(self):
        return type_selection[str(self.monster_type)]

    #Calculates the Values and Returns it to the Console
    def calculation(self):
        self.build_comp_dict()
        self.DC         = sum(self.components[item] for item in self.monster_components)
        self.DC_calc    = self.DC_calc + "+".join(str(self.components[item]) for item in self.monster_components)
        self.comp_list  = self.comp_list + ", ".join(self.monster_components).title()
        
                
        return [ "Monster Type : "+ str(self.monster_type).capitalize(), "DC: " + str(self.DC), str(self.DC_calc), str(self.comp_list)]
    
    