from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import PickleType

db = SQLAlchemy()

class Time(db.Model):

  __tablename__ = 'schedule'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  json_name = db.Column(db.String, nullable=False)
  image_url = db.Column(db.String, nullable=False)
  times = db.Column(db.PickleType, nullable=False)
  information = db.Column(db.PickleType, nullable=False)
  location = db.Column(db.PickleType, nullable=False)

  def __init__(self, **kwargs):
    self.name = kwargs.get('name', "")
    self.json_name = kwargs.get('json_name', "")
    self.image_url = kwargs.get('image_url', "")
    self.times = kwargs.get('times', ["", "", "", "", "", "", ""])
    self.information = kwargs.get('information', [[], [], [], "", "", False])
    self.location = kwargs.get('location', [0, 0, ""])

  def serialize(self):
    return {
        'name': self.name,
        'image_url': self.image_url,
        'times':
          [
            self.times[0],
            self.times[1],
            self.times[2],
            self.times[3],
            self.times[4],
            self.times[5],
            self.times[6]
          ],
         'information':
           {'nooks': self.information[0],
           "services":
               {"electronic": self.information[1],
                "resources": self.information[2]},
           "cafe":
               {
                "name": self.information[3],
                "time": self.information[4],
                "brb": self.information[5]
               }
           },
        'location':
         {
          'coordinates': [self.location[0], self.location[1]],
          'campus' : self.location[2]
         }
    }
