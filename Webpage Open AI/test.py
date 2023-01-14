from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        'animals': {
            'mammals': {
                'dogs': ['Golden Retriever', 'Bulldog', 'Beagle'],
                'cats': ['Siamese', 'Persian', 'Sphynx']
            },
            'birds': {
                'parrots': ['African Grey', 'Amazon', 'Cockatiel'],
                'penguins': ['Emperor', 'King', 'Little']
            }
        }
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()
