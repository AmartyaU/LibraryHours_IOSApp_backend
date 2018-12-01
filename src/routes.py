import json
from flask import Flask, request
from db import db, Time
import requests
from threading import Timer
from constants import *
from datetime import datetime as dt, date, timedelta
import calendar

db_filename = "todo.db"
app = Flask(__name__)

# Run update and initial how?
#imagelink check
#after deployment change?

#hardcode all data
##cafes eateries use one function to update all
#deploy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % db_filename
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
with app.app_context():
    db.create_all()


def make_time_format(time):
  """
  Helper function that takes in time string and convert it to the proper time format
  """
  time = time.replace("pm", ":00 PM")
  time = time.replace("am", ":00 AM")
  return time

def get_all_times(weeks):
  """
  Helper function that gives array of times of 7 days from today
  """
  date_today = date.today()
  upper_date_bound = date_today + timedelta(days=7)
  result = []
  for value in weeks:
    for day in DAYS:
      times_date = dt.strptime(value[day]["date"], "%Y-%m-%d").date()
      if times_date >= date_today and times_date < upper_date_bound:
        result.append(make_time_format(value[day]["rendered"]))
  return result

def update_cafe():
  """
  Updates Cafe time
  """
  cafe_names = ["Amit Bhatia Libe Café"]
  cafe_names_libraries = {"Amit Bhatia Libe Café": "Olin Library"}
  jsons = requests.get("https://now.dining.cornell.edu/api/1.0/dining/eateries.json").json()
  for value in jsons["data"]["eateries"]:
    if value["name"] in cafe_names:
      for day in value["operatingHours"]:
        if day["date"] == str(date.today()):
          time = day["events"][0]["start"]+" - "+ day["events"][0]["end"]
          time = time.replace("am", " AM")
          time = time.replace("pm", " PM")
          record = Time.query.filter_by(name=cafe_names_libraries[value["name"]]).first()
          record.information = [record.information[0], record.information[1], record.information[2], record.information[3], time, record.information[5]]
          db.session.commit()


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

    update_cafe()
    COUNTER = 0
    for value in times_json["locations"]:
      if value["name"] == "Manndible":
          record = Time.query.filter_by(name="Mann Library").first()
          cafe_time = value["weeks"][0][calendar.day_name[date.today().weekday()]]["rendered"]
          record.information = [record.information[0], record.information[1], record.information[2], record.information[3], cafe_time, record.information[5]]
          db.session.commit()

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
