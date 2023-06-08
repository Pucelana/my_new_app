from flask import *
from flask_bootstrap import Bootstrap
from flaskext.mysql import MySQL

app = Flask(__name__)
bootstrap = Bootstrap(app)
mysql = MySQL()

# Configuración de la conexión a la base de datos
app.config['MYSQL_DATABASE_HOST'] = 'Pucelana83.mysql.pythonanywhere-services.com'
app.config['MYSQL_DATABASE_USER'] = 'Pucelana83'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Z@p@titos83'
app.config['MYSQL_DATABASE_DB'] = 'Pucelana83$default'

mysql.init_app(app)

@app.route('/')
def index():
    return render_template('sitio/index.html')

@app.route('/registro_admin/')
def registro_admin():
    return render_template('sitio/registro_admin.html')

if __name__ == 'main':
    app.run()

