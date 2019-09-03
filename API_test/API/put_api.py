
from flask import Blueprint,request,jsonify


put_api_blueprint = Blueprint('put_api', __name__)

@put_api_blueprint.route('/put-api',methods=['PUT'])
def put_api_():
    data = request.get_json()

    res_data = {"success": True,
            "Message": "data updated",
            "data": data,
            "update": True
            }
    resp = jsonify(res_data)
    resp.status_code = 200
    return resp