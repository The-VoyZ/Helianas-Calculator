# mycode.py
from flask import Flask, render_template, request

app = Flask(__name__)

# Beispiel-Daten
data = {
    "essence"     : {"Frail essence":25,"Robust essence":30,"Potent essence":35,"Mythic essence":40,"Deific essence":50},
    "aberation"   : {"antenna":5,"eye":5,"flesh":5,"phial of blood":5,"bone":10,"egg":10,"fat":10,"pouch of claws":10,"pouch of teeth":10,"heart":15,"phial of mucus":15,"liver":15,"stinger":15,"tentacle":15,"brain":20,"chitin":20,"hide":20,"main eye":20},
    "beast"       : {"antenna":5,"eye":5,"flesh":5,"phial of blood":5,"antler":10,"beak":10,"bone":10,"egg":10,"fat":10,"fin":10,"horn":10,"pincer":10,"pouch of claws":10,"pouch of teeth":10,"talon":10,"tusk":10,"heart":15,"liver":15,"poison gland":15,"pouch of feathers":15,"pouch of scales":15,"stinger":15,"tentacle":15,"chitin":20,"pelt":20},
    "celestial"   : {"eye":5,"flesh":5,"phial of blood":5,"pouch of dust":5,"bone":10,"fat":10,"horn":10,"pouch of teeth":10,"heart":15,"liver":15,"pouch of feathers":15,"pouch of scales":15,"brain":20,"skin":20,"soul":25},
    "construct"   : {"phial of blood":5,"phial of oil":5,"phial of sap":5,"pouch of dust":5,"flesh":10,"metal plating":10,"stone":10,"bone":15,"heart":15,"liver":15,"gears":15,"brain":20,"instructions":20,"lifespark":25},
    "dragon"      : {"eye":5,"flesh":5,"phial of blood":5,"bone":10,"fat":10,"pouch of claws":10,"pouch of teeth":10,"horn":15,"liver":15,"pouch of scales":15,"heart":20,"breath sac":25},
    "elemental"   : {"eye":5,"primordial dust":5,"bone":10,"volatile mote of air":15,"volatile mote of earth":15,"volatile mote of fire":15,"volatile mote of water":15,"core of air":25,"core of earth":25,"core of fire":25,"core of water":25},
    "fey"         : {"antenna":5,"eye":5,"flesh":5,"phial of blood":5,"antler":10,"beak":10,"bone":10,"egg":10,"horn":10,"pouch of claws":10,"pouch of teeth":10,"talon":10,"tusk":10,"heart":15,"fat":15,"liver":15,"poison gland":15,"pouch of feathers":15,"pouch of scales":15,"tentacle":15,"tongue":15,"brain":20,"skin":20,"pelt":20,"psyche":25},
    "fiend"       : {"antenna":5,"eye":5,"flesh":5,"phial of blood":5,"pouch of dust":5,"bone":10,"horn":10,"pouch of teeth":10,"heart":15,"fat":15,"liver":15,"poison gland":15,"pouch of feathers":15,"pouch of scales":15,"brain":20,"skin":20,"soul":25},
    "giant"       : {"flesh":5,"nail":5,"phial of blood":5,"bone":10,"fat":10,"tooth":10,"heart":15,"liver":15,"skin":20},
    "humanoid"    : {"eye":5,"phial of blood":5,"bone":10,"egg":10,"pouch of teeth":10,"heart":15,"liver":15,"pouch of feathers":15,"pouch of scales":15,"brain":20,"skin":20},
    "monstrosity" : {"antenna":5,"eye":5,"flesh":5,"phial of blood":5,"antler":10,"beak":10,"bone":10,"egg":10,"fat":10,"fin":10,"horn":10,"pincer":10,"pouch of claws":10,"pouch of teeth":10,"talon":10,"tusk":10,"heart":15,"liver":15,"poison gland":15,"pouch of feathers":15,"pouch of scales":15,"stinger":15,"tentacle":15,"chitin":20,"pelt":20},
    "ooze"        : {"phial of acid":5,"phial of mucus":10,"vesicle":15,"membrane":20},
    "plant"       : {"phial of sap":5,"tuber":5,"bundle of roots":10,"phial of wax":10,"pouch of hyphae":10,"pouch of leaves":10,"poison gland":15,"pouch of pollen":15,"pouch of spores":15,"bark":20,"fungal membrane":20},
    "undead"      : {"eye":5,"bone":5,"phial of congealed blood":5,"marrow":10,"pouch of teeth":10,"rancid fat":10,"ethereal ichor":15,"undying flesh":15,"undying heart":20}
}


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Speichere ausgewähltes Dictionary
        selected_dict = request.form["dict"]
        return render_template('keys.html', data=data[selected_dict], selected_dict=selected_dict)
    return render_template('index.html', data=data)

@app.route('/sum', methods=["POST"])
def sum_values():
    # Summe der ausgewählten Werte
    keys = request.form.getlist("keys")
    selected_dict = request.form["dict"]
    total = sum(data[selected_dict][key] for key in keys)
    return str(total)

if __name__ == '__main__':
    app.run()


# index.html
"""<!DOCTYPE html>
<html>
<head>
    <title>Dictionary Selection</title>
</head>
<body>
    <h1>Select a Dictionary</h1>
    <form method="post">
        <select name="dict">
            {% for name, values in data.items() %}
                <option value="{{ name }}">{{ name }}</option>
            {% endfor %}
        </select>
        <input type="submit" value="Select">
    </form>
</body>
</html>
"""
# keys,html
"""
<!DOCTYPE html>
<html>
<head>
    <title>Key Selection</title>
</head>
<body>
    <h1>Select Keys</h1>
    <h2>{{selected_dict}}</h2>
    <form method="post">
        {% for key in data.keys() %}
            <input type="checkbox" name="keys" value="{{ key }}"> {{ key }}<br>
        {% endfor %}
        <input type="hidden" name="dict" value="{{ selected_dict }}">
        <input type="submit" value="Calculate Sum" formaction="/sum">
    </form>
</body>
</html>"""