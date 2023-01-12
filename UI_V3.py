import tkinter as tk
from tkinter import ttk

# Beispieldictionaries
dicts = {
    "Dictionary 1": {"key1": 1, "key2": 2, "key3": 3},
    "Dictionary 2": {"key4": 4, "key5": 5, "key6": 6},
    "Dictionary 3": {"key7": 7, "key8": 8, "key9": 9}
}

def calculate():
    # Code zur Berechnung des Ergebnisses
    result = 0
    for key in selected_keys:
        result += dicts[selected_dict.get()][key.get()]
    output_label.config(text=result)

def reset_selections():
    selected_dict.set("")
    dict_dropdown.current(0)
    output_label.config(text="")
    for key_var in key_dropdowns:
        key_var.set("")
    selected_keys.clear()

def reset_all():
    reset_selections()
    key_dropdowns.clear()
    for widget in root.winfo_children():
        widget.destroy()
    initialize_gui()

def initialize_gui():
    global selected_dict, dict_dropdown, selected_keys, key_dropdowns, output_label
    # Überschrift
    heading_label = tk.Label(root, text="Helianas Harvesting Calculator")
    heading_label.pack()

    # Dropdown Menü für Dictionaries
    selected_dict = tk.StringVar(root)
    dict_dropdown = ttk.Combobox(root, textvariable=selected_dict, values=list(dicts.keys()))
    dict_dropdown.pack()

    # Liste für ausgewählte Schlüssel
    selected_keys = []
    key_dropdowns = []

    # Funktion zum Erstellen eines neuen Key-Dropdown
    def add_key_dropdown():
        key_var = tk.StringVar(root)
        key_dropdown = ttk.Combobox(root, textvariable=key_var, values=list(dicts[selected_dict.get()].keys()))
        key_dropdown.pack()
        key_dropdowns.append(key_var)
        key_var.trace("w", lambda *args: calculate())

    # Button zum Hinzufügen eines neuen Key-Dropdown
    add_key_button = tk.Button
    add_key_button.pack()

    # Button zum Berechnen
    calculate_button = tk.Button(root, text="Calculate Heist", command=calculate)
    calculate_button.pack()

    # Reset button
    reset_button = tk.Button(root, text="Reset", command=reset_selections)
    reset_button.pack()

    # Reset all button
    reset_all_button = tk.Button(root, text="Reset All", command=reset_all)
    reset_all_button.pack()

    # Ausgabefeld
    output_label = tk.Label(root, text="")
    output_label.pack()

root = tk.Tk()
root.title("Helianas Harvesting Calculator")
initialize_gui()
root.mainloop()