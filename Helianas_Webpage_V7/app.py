from MonsterCalculator import HarvestCalculator
from MundaneMaterialCalculator import MundaneIngredients
from flask import Flask, render_template, request
from Monster_Dictionarys import type_selection , region_selection , unrefined_dict
app = Flask(__name__)



@app.route('/')

def index():
    return render_template("index.html")

@app.route('/calc', methods = ["POST"])
def calc_mainpage():
    options = type_selection
    options2 ={}
    return render_template("MonsterCalculator.html", options=options, options2 = options2)

@app.route('/dict_selected', methods=["POST"])
def dict_select():
    monster_type = str(request.form["dropdown"])
    selected_monster_type = {}
    selected_monster_type[monster_type] = type_selection[monster_type]
    options = selected_monster_type
    options2 = type_selection[monster_type]
    return render_template("MonsterCalculator.html", options=options, options2=options2 , monster_type=monster_type)

@app.route('/calculate', methods=["POST"])
def calculate():
    monster_type = str(request.form["monster_type"])
    # Abrufen der ausgewählten Option aus dem Dropdown-Menü
    #monster_type = str(request.form["dropdown"])
    # Abrufen der Zahl aus der Eingabe-Fläche
    monster_CR = int(request.form["number"])
    # Abrufen des Texts aus der Eingabe-Fläche
   # monster_components = str(request.form["text"]).lower()
    monster_components = str(request.form["resultString"])
    monster_components = monster_components[:-1].split(",")
    
    
    
    # Beispiel-Funktion, die die übergebenen Parameter verarbeitet
    result  = process_inputs_monster_parts(monster_CR,monster_type,monster_components)
    options = type_selection
    options2 = {}
    return render_template("MonsterCalculator.html", result=result , options=options, options2=options2)


@app.route("/mundaneitems", methods= ["POST"])
def mundane_main():
    options = region_selection
    options2 ={}
    return render_template("MundaneMaterial.html", options=options, options2 = options2)

@app.route('/region', methods=["POST"])
def region_select():
    region = str(request.form["dropdown"])
    selected_region = {}
    selected_region[region] = region_selection[region]
    options = selected_region
    options2 = region_selection[region]
    return render_template("MundaneMaterial.html", options=options, options2=options2 , region=region)

@app.route('/region_calculate', methods=["POST"])
def calculate_DC():
    region = str(request.form["region"])
    # Abrufen der ausgewählten Option aus dem Dropdown-Menü
    material = str(request.form["material"])
    dc = int(request.form["number"])
    result = process_inputs_material(region,material,dc)
    options2 = {}
    options = region_selection
    return render_template("MundaneMaterial.html", options=options, options2=options2 , result=result)


#Functions needed for Calculations
def process_inputs_monster_parts(monster_CR,monster_type, monster_components):
    a = HarvestCalculator(monster_CR,monster_type, monster_components)
   
    
    return a.calculation()

def process_inputs_material(region,material,dc):
    b = MundaneIngredients(region,material,dc)
    return b.calculate()

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
    #<form method="GET" action="/" style = "margin: 25px">