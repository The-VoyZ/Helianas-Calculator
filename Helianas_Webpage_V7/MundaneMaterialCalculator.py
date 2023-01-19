from Monster_Dictionarys import region_selection , unrefined_dict

class MundaneIngredients():
    
    #Calculation for the Return Materials: Units found = 5x(1+Check -DC) 
    #DC Calculation = Region + Material Type
    
    def __init__(self,region,material, dc) -> None:
        self.region = str(region)
        self.material = str(material)
        self.material_dict = {}
        self.DC = dc
        self.material_units = 0
        self.calculate()
        
    def material_DC(self):
        self.material_dict = self.region_check()
        if self.material in self.material_dict:
            return self.material_dict[self.material]
            
    
    
    def region_check(self):
        return region_selection[self.region]
    
    
    def material_calulation(self):
        if self.DC < int(self.material_DC()):
            return 0
        else:
            self.material_units = 5 *(1 + self.DC - self.material_DC())
        return int(self.material_units)
   
    def unrefined_materials(self):
        unrefined_units = unrefined_dict[self.material]*self.material_units
        return unrefined_units
    
    
    def calculate(self):
        
        return ["Selected Region: "+ self.region.capitalize(), "Selected Material: " + self.material.capitalize(),"Dc =" + str(self.material_DC()), "Rolled DC:"+ str(self.DC), "You gethered " + str(self.material_calulation()) + " Units of " + self.material.capitalize() + " for a Total of " + str(self.unrefined_materials()) + " lbs"]