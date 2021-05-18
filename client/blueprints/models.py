from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
      student_id = db.Column('student_id', db.Integer, primary_key = True)
      first_name = db.Column(db.String(80), nullable=False)
      last_name = db.Column(db.String(80), nullable=False)
      urlImg = db.Column(db.String(500))