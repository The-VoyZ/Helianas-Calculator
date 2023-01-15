from Monster_Dictionarys import region_selection , unrefined_dict

class MundaneIngredients():
    
    #Calculation for the Return Materials: Units found = 5x(1+Check -DC) 
    #DC Calculation = Region + Material Type
    
    def __init__(self,region,material) -> None:
        self.region = str(region)
        self.material = str(material).lower()
        self.material_dict = {}
        self.check_input = 0
        self.material_units = 0
        self.console_output()
        
    def material_DC(self):
        self.material_dict = self.region_check()
        if self.material in self.material_dict:
            return self.material_dict[self.material]
            
    
    
    def region_check(self):
        return region_selection[self.region]
    
    
    def check_rolled(self):
        self.check_input = input("What have you Rolled?")
        return int(self.check_input)
    
    
    def material_calulation(self):
        self.material_units = 5 *(1 + self.check_input - self.material_DC())
        return int(self.material_units)
   
    def unrefined_materials(self):
        unrefined_units = unrefined_dict[self.material]*self.material_units
        return unrefined_units
    
    
    def console_output(self):
        print ("\n" + "Selected Region: "+ self.region.capitalize() + "\n" + "Selected Material: " + self.material.capitalize() + "\n" + "Dc =" + str(self.material_DC()) + "\n")
        self.check_input = self.check_rolled()
        return print("You gethered " + str(self.material_calulation()) + " Units of Copper " + self.material.capitalize() + " for a Total of " + str(self.unrefined_materials()) + " lbs")