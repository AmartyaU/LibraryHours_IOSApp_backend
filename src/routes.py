import json
from flask import Flask, request
from db import db, Time
import requests
from threading import Timer
from constants import *

db_filename = "todo.db"
app = Flask(__name__)


# Run update and initial how?
#times help take
#imagelink check

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % db_filename
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/api/test/')
def initirral():
  """
  Hardcoding fixed data
  """
  times_json = requests.get(CORNELL_LIBRARY_TIMES_URL).json()
  for value in times_json["locations"]:
    if value["name"] == "Manndible":
        record = Time.query.filter_by(name="Mann Library").first()
        info = record.information
        info[4] = value["weeks"][0]["Sunday"]["rendered"]
        record.information = info
        print(record.information)
        db.session.commit()
        print(record.information)
  return json.dumps({'success': True, 'data': [Time.query.filter_by(name="Mann Library").first().information]}), 200



@app.route('/api/initial/')
def initial():
  """
  Hardcoding fixed data
  """
  for i in range(len(LIBRARY_NAMES)):
    record = Time(
    name = LIBRARY_NAMES[i],
    json_name = LIBRARY_NAMES_JSON[i],
    image_url = IMAGE_GITHUB_URL + IMAGE_NAMES[i],
    information = LIBRARY_INFORMATION[i],
    location = LIBRARY_LOCATION[i]
    )
    print(i)
    db.session.add(record)
    db.session.commit()
  return json.dumps({'success': True, 'data': [post.serialize() for post in Time.query.all()]}), 200

@app.route('/api/update/')
def update():
  """
  Update times of all libraries every 24 hours
  """
  times_json = requests.get(CORNELL_LIBRARY_TIMES_URL).json()
  try:
    COUNTER = 0
    for value in times_json["locations"]:
      # if value["name"] == "Manndible":
      #     record = Time.query.filter_by(name="Mann Library").first()
      #     record.information[4] = value["weeks"][0]["Sunday"]["rendered"]
      #     db.session.commit()
      # if value["name"] == "Amit Bhatia Libe Cafe":
      #     record = Time.query.filter_by(name="Olin Library").first()
      #     record.information[4] = value["weeks"][0]["Sunday"]["rendered"]
      #     db.session.commit()

      record = Time.query.filter_by(json_name=value["name"]).first()
      if record is not None:
        record.times = [value["weeks"][0]["Sunday"]["rendered"], value["weeks"][0]["Monday"]["rendered"],
        value["weeks"][0]["Tuesday"]["rendered"], value["weeks"][0]["Wednesday"]["rendered"],
        value["weeks"][0]["Thursday"]["rendered"], value["weeks"][0]["Friday"]["rendered"],
        value["weeks"][0]["Saturday"]["rendered"]]
        db.session.commit()
    return json.dumps({'success': True, 'data': [post.serialize() for post in Time.query.all()]}), 200
  except Exception as e:
    print('Update failed: ', e)
  finally:
    Timer(UPDATE_TIME, update).start()

@app.route('/api/times/')
def get_times():
    """
    Gets all information for all libraries
    """
    return json.dumps({
      'success': True,
      'data': { "libraries": [post.serialize() for post in Time.query.all()] }
    }), 200

@app.route('/api/names/')
def get():
    """
    Gets name all libraries
    """
    data = []
    for value in times_json["locations"]:
      data.append(value["name"])
    return json.dumps({
      'success': True,
      'data': data
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
