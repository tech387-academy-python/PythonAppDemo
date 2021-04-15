from flask import Flask, Response, request, json
from mongo_api import MongoAPI
from validators import Validators

app = Flask(__name__)


@app.route('/')
def base():
    return Response(response=json.dumps({'Status':'OK'}),
                    status=200,
                    mimetype='application/json')


@app.route('/user', methods=['GET'])
def mongo_read():
    
    data = request.json
    
    if data is None or data == {}:
        return Response(response=json.dumps({'Error': 'Invalid data request format'}),
                        status=400,
                        mimetype='application/json')
    
    obj1 = MongoAPI(data)
    response = obj1.read()
    
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')
    

@app.route('/user', methods=['POST'])
def mongo_write():
    
    data = request.json
    
    if data == None or data == {} or 'document' not in data:
        return Response(response=json.dumps({'Error': 'Invalid data request format'}),
                        status=400,
                        mimetype='application/json')
    
    if 'email' in data['document'].keys():
        if Validators.validateEmail(data['document']['email']):
            pass
        else:
            return Response(response=json.dumps({'Error': 'Invalid data request format'}),
                            status=400,
                            mimetype='application/json')
    
    obj1 = MongoAPI(data)
    response = obj1.write()
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')        
                    

@app.route('/user', methods=['DELETE'])
def mongo_remove():
     
    data = request.json
    
    if data == None or data == {} or 'document' not in data:
        return Response(response=json.dumps({'Error': 'Invalid data request format'}),
                        status=400,
                        mimetype='application/json')
        
    obj1 = MongoAPI(data)
    response = obj1.delete()
    
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')
                    
if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')




