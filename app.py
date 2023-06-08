from flask import *
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('sitio/index.html')

@app.route('/registro_admin/')
def registro_admin():
    return render_template('sitio/registro_admin.html')

if __name__ == 'main':
    app.run()

