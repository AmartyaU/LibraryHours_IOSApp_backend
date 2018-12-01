import json
from flask import Flask, request
from db import db, Time
import requests
from threading import Timer
from constants import *
from datetime import datetime as dt, date, timedelta

db_filename = "todo.db"
app = Flask(__name__)

#times help format do

# Run update and initial how?
#imagelink check

#cafes eateries use?

#hardcode all data
#deploy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % db_filename
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
with app.app_context():
    db.create_all()


def make_time_format(time):
  """
  Takes in time string and convert it to the proper time format
  """
  time = time.replace("pm", ":00 PM")
  time = time.replace("am", ":00 AM")
  return time

def get_all_times(weeks):
  """
  Gets array of times of 7 days from today
  """
  date_today = date.today()
  upper_date_bound = date_today + timedelta(days=7)
  result = []
  for value in weeks:
    for day in DAYS:
      times_date = dt.strptime(value[day]["date"], "%Y-%m-%d").date()
      if times_date >= date_today and times_date < upper_date_bound:
        result.append(make_time_format(value[day]["rendered"]))
  print(result)
  return result




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
        record.times = get_all_times(value["weeks"])
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

@app.route('/api/test/')
def initirral():
  """
  Hardcoding fixed data
  """
  # times_json = requests.get(CORNELL_LIBRARY_TIMES_URL).json()
  # for value in times_json["locations"]:
  #   if value["name"] == "Manndible":
  #       record = Time.query.filter_by(name="Mann Library").first()
  #       info = record.information
  #       info[4] = value["weeks"][0]["Sunday"]["rendered"]
  #       record.information = info
  #       print(record.information)
  #       db.session.commit()
  #       print(record.information)

  times_date = dt.strptime('2018-12-02', "%Y-%m-%d").date()
  date_today = date.today()
  print("AFSFASFasjgfhzkbdwajfabkas")
  # d.replace(days=d.da + 7)
  print(make_time_format("2pm - 3pm"))
  return json.dumps({'success': True, 'data': [Time.query.filter_by(name="Mann Library").first().information]}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
