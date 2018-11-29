import json
from flask import Flask, request
from db import db, Time
import requests
from threading import Timer
# from cont file import var

db_filename = "todo.db"
app = Flask(__name__)
CORNELL_LIBRARY_TIMES_URL = "https://api3.libcal.com/api_hours_grid.php?iid=973&lid=0&format=json"
times_json = requests.get(CORNELL_LIBRARY_TIMES_URL).json()
# Run update once and put times_json in Update

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % db_filename
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route('/api/start/')
def initial():
  """
  Hardcoding fixed data
  """
  for value in times_json["locations"]:
    record = Time(
    name = value["name"],
    times = [value["weeks"][0]["Sunday"]["rendered"], value["weeks"][0]["Monday"]["rendered"],
    value["weeks"][0]["Tuesday"]["rendered"], value["weeks"][0]["Wednesday"]["rendered"],
    value["weeks"][0]["Thursday"]["rendered"], value["weeks"][0]["Friday"]["rendered"],
    value["weeks"][0]["Saturday"]["rendered"]],
    information = ["blah", "blahblah"],
    coordinates = [value["lat"], value["long"]]
    )
    db.session.add(record)
    db.session.commit()
  return json.dumps({'success': True, 'data': [post.serialize() for post in Time.query.all()]}), 201

@app.route('/api/update/')
def update():
  """
  Update times of all libraries every 24 hours
  """
  try:
    for value in times_json["locations"]:
      record = Time.query.filter_by(name=value["name"]).first()
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
    Timer(86400.0, update).start()


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
