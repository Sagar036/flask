
from flask import Blueprint,request,jsonify


delete_api_blueprint = Blueprint('delete_api', __name__)

@delete_api_blueprint.route('/delete-api',methods=['DELETE'])
def delete_api_():

    res_data = {"success": "True",
            "Message": "data deleted",
            "data": None
            }
    resp = jsonify(res_data)
    resp.status_code = 200
    return resp