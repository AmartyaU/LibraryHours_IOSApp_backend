from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.types import PickleType

db = SQLAlchemy()

class Time(db.Model):

  __tablename__ = 'schedule'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  times = db.Column(db.PickleType, nullable=False)
  information = db.Column(db.PickleType, nullable=False)
  # coordinates = db.Column(ARRAY(db.String, dimensions=2), nullable=False)
  coordinates = db.Column(db.PickleType, nullable=False)

  def __init__(self, **kwargs):
    self.name = kwargs.get('name', "NA")
    self.times = kwargs.get('times', ["NA", "NA", "NA", "NA", "NA", "NA", "NA"])
    self.information = kwargs.get('information', ["NA", "NA"])
    self.coordinates = kwargs.get('coordinates', ["NA", "NA"])

  def serialize(self):
    return {
        'name': self.name,
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
          {
            "Nooks": self.information[0],
            "Services": self.information[1]
          },
        'coordinates':
          {
            "Latitude": self.coordinates[0],
            "Longitude": self.coordinates[1]
          }
    }
