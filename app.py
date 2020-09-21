from flask import Flask, jsonify, request,render_template
app = Flask(__name__)


stores=[
{
    'name':'My Store',
    'items':[
                {
                    'name':'My Item',
                    'price':18.99
                }
            ]
},
{
    'name':'Test Store',
    'items':[
                {
                    'name':'test Item',
                    'price':99
                }
            ]


}

]
@app.route('/')
def home():
  return render_template('index.html')

@app.route('/store')
def get_stores():
  return jsonify({'stores':stores})

@app.route('/createstore', methods=['POST'])
def create_stores():
  req_data=request.get_json()
  new_store={
  'name':req_data['name'],
  'items':[]
  }
  stores.append(new_store)
  return jsonify(new_store)

@app.route('/store/<string:name>/item', methods=['POST'])
def create_stores_item(name):
  req_data=request.get_json()
  for i in stores:
      if(i['name']==name):
          new_item={
          'name':req_data['name'],
          'price':req_data['price']
          }
          i['items'].append(new_item)

  return jsonify(new_item)

@app.route('/store/<string:name>')
def get_store(name):
  for i in stores:
      if(i['name']==name):
          return jsonify(i)


  return jsonify({'message':'This is an error'})

@app.route('/store/<string:name>/item')
def get_store_item(name):
  for i in stores:
      return jsonify({'items':i['items']})

      # if(i['name']==name):
      #     for j in i['items']:
      #         j['name']==item


  return jsonify({'message':'This is an error'})

app.run(port=5000)
