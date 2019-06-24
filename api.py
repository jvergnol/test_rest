import datetime
from flask import Flask,request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Format(Resource):
    def post(self):
        data = request.json
        local_datetime = '%s %s'%(data['time_1'],  data['time_2'])
        _time = datetime.datetime.strptime(data['time_1'], "%H:%M")
        # UTC_OFFSET = 10
        result_utc_datetime = _time - datetime.timedelta(hours=data['time_2'])
        result_utc_datetime.strftime("%H:%M:%S")
        print(_time)
        return {'time': result_utc_datetime.strftime("%H:%M:%S"), 'time_zone':'UTC'}

api.add_resource(Format, '/')

if __name__ == '__main__':
    app.run(debug=True)
