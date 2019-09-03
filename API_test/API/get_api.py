
from flask import Blueprint,request,jsonify


get_api_blueprint = Blueprint('get_api', __name__)

@get_api_blueprint.route('/get-api',methods=['GET'])
def get_api_():

    res_data = {"success": "True",
            "Message": "showing Results",
            "data": {"Name":"Sagar",
                      "roll_no.":1410922
                    }
            }
    resp = jsonify(res_data)
    resp.status_code = 200
    return resp