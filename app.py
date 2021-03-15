from flask import Flask, render_template, request, redirect
from datetime import date
from forms import InputParams
from sklearn.ensemble import RandomForestRegressor
import pickle

app = Flask(__name__)
app.config['SECRET_KEY']='566f97b31e1f9229cf57999ac0e7d89e'

def getModel():
  with open('models/model_rfr.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

  return loaded_model

def onehot(values, cat):
  #values = ['S', 'SA', 'SP', 'VB']
  for i in range(len(values)):
    if values[i]==cat:
      values[i]=1

    else:
      values[i]=0

  return values


@app.route('/', methods=['GET', 'POST'])
def index():
  form = InputParams()
  if request.method=='GET':
    return render_template('index.html', form=form)
  else:
    rooms = form.rooms.data
    method = form.method.data
    ptype = form.ptype.data
    postcode = form.postcode.data
    distance = form.distance.data
    region = form.region.data
    propertycount = form.propertycount.data
    bedrooms = form.bedrooms.data
    bathrooms = form.bathrooms.data
    cars = form.cars.data
    landsize = form.landsize.data
    buildingarea = form.buildingarea.data
    yearbuilt = form.yearbuilt.data
    latitude = form.latitude.data
    longitude = form.longitude.data

    ptype_oh = ['t', 'u']
    ptype_oh = onehot(ptype_oh, ptype)

    method_oh = ['S', 'SA', 'SP', 'VB']
    method_oh = onehot(method_oh, method)

    pc_oh = [3073, 3020, 3121, 3040, 3046, 3165, 3058, 3163, 3012, 3072, 3032, 3204, 3056]
    pc_oh = onehot(pc_oh, postcode)

    yearbuilt_missing = 0
    if yearbuilt==None:
      yearbuilt_missing=1

    region_oh = ['Eastern Victoria', 'Northern Metropolitan', 'Northern Victoria', 'South-Eastern Metropolitan', 'Southern Metropolitan', 'Western Metropolitan', 'Western Victoria']
    region_oh = onehot(region_oh, region)

    test_data = [rooms] + ptype_oh + method_oh + [float(distance)] + pc_oh + [bedrooms, bathrooms, cars, float(landsize), float(buildingarea), yearbuilt_missing, yearbuilt, float(latitude), float(longitude)] + region_oh + [propertycount]

    model = getModel()
    pred = model.predict([test_data])
    pred = round(pred[0], 2)

    return render_template('index.html', form=form, test_data=test_data, pred=pred)

@app.route('/about')
def about():
  return render_template('about.html')


@app.route('/contact')
def contact():
  return render_template('contact.html')


if __name__ == "__main__":
  app.run(debug=True)
