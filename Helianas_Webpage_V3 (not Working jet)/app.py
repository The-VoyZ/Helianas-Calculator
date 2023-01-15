from MonsterCalculator import HarvestCalculator
from flask import Flask, render_template, request
from Monster_Dictionarys import type_selection
app = Flask(__name__)



@app.route('/')

def index():
    # Beispiel-Dictionary für das Dropdown-Menü
    options = type_selection
    options2 ={}
    return render_template("index.html", options=options, options2 = options2)
@app.route('/', methods=["POST"])

def dict_select():
    monster_type = str(request.form["dropdown"])
    options = type_selection
    options2 = type_selection[monster_type]
    return render_template("index.html", options=options, options2 = options2)

@app.route('/', methods=["POST"])
def calculate():
    # Abrufen der ausgewählten Option aus dem Dropdown-Menü
    monster_type = str(request.form["dropdown"])
    # Abrufen der Zahl aus der Eingabe-Fläche
    monster_CR = int(request.form["number"])
    # Abrufen des Texts aus der Eingabe-Fläche
   # monster_components = str(request.form["text"]).lower()
    monster_components = str(request.form["components"])
    
    
    
    # Beispiel-Funktion, die die übergebenen Parameter verarbeitet
    result  = process_inputs(monster_CR,monster_type,monster_components)
    options = type_selection
    return render_template("index.html", result=result , options=options)

def process_inputs(monster_CR,monster_type, monster_components):
    a = HarvestCalculator(monster_CR,monster_type, monster_components)
    
    
    return a.calculation()

 

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
    calculate()