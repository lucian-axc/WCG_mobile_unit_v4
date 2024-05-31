from flask import Flask, render_template, request, url_for
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mu4.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = 'wcg-rulz'

# db = SQLAlchemy(app)

import routes

# if __name__ == '__main__':
#     app.run(debug=True, port=8001)