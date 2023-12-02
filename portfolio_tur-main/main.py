# Import
from flask import Flask, render_template, request

app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        button_python = request.form.get('button_python')
        email = request.form.get('email')
        text = request.form.get('text')

        if button_python:
            return render_template('index.html', button_python=button_python)
       
        with open('form.txt', 'a') as file:
            file.write(f'Email: {email}\n')
            file.write(f'Text: {text}\n')
            file.write('\n')  # Verileri ayırmak için bir boş satır ekleme

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
