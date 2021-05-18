from flask import Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from blueprints.models import Student

about = Blueprint('about', __name__)

@about.route('/about')
def abo():
   return render_template("about.html", students = Student.query.all())