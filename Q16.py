from flask import Flask, jsonify, request

app = Flask(__name__)
heart_records = [
    {
        "heart_id" : "1",
        "date" : "08/10/2024",
        "heart_rate" : "64"
    },
    {
        "heart_id" : "2",
        "date" : "08/11/2024",
        "heart_rate" : "80"
    }
]
@app.route('/heart_records', methods=['GET'])
def getHeartRecord():
    return jsonify(heart_records)
@app.route('/heart_records', methods=['POST'])
def addHeartRecord():
    heart_record = request.get_json()
    heart_records.append(heart_record)
    return {'Successful, id': len(heart_records)}, 200
@app.route('/heart_records/<int:index>',methods=['PUT'])
def update_heartrecord(index):
    heart_record = request.get_json()
    heart_records[index] = heart_record
    return jsonify(heart_records[index]), 200
@app.route('/heart_records/<int:index>',methods=['DELETE'])
def deleteHeartRecord(index):
    heart_records.pop(index)
    return 'The Heart Record has been delete', 200
if __name__ == '__main__':
    app.run()