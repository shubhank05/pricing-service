import os
from flask import Flask, render_template
from views.alerts import alert_blueprint
from views.stores import store_blueprint
from views.users import user_blueprint
from views.logout import logout_blueprint
from libs.mailgun import Mailgun
from dotenv import load_dotenv
app = Flask(__name__)
app.secret_key = '12324343'
app.config.update(
    ADMIN = os.environ.get('ADMIN')
)
load_dotenv()
print("os.eviron")
@app.route('/')
def home():
    return render_template('home.html')
app.register_blueprint(alert_blueprint, url_prefix = '/alerts')
app.register_blueprint(store_blueprint, url_prefix = '/stores')
app.register_blueprint(user_blueprint, url_prefix = '/users')
app.register_blueprint(logout_blueprint, url_prefix = '/logout')
if __name__ == "__main__":
    app.run(debug=True)
