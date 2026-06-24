#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]

app = Flask(__name__)

@app.route('/contract/<int:contract_id>')
def contractor_info(contract_id):
    c_id = "id"
    for i in contracts:
        if c_id in i:
            if contract_id == i[c_id]: 
                contact_information = i['contract_information']
                status_code = 200
                return make_response(contact_information, status_code)
    else:
        status_code = 404
        return make_response("", status_code, "")
    

@app.route('/customer/<string:customer_name>')
def customer_info(customer_name):
    if customer_name in customers:
        status_code = 204
        return make_response("", status_code, "")
    else:
        status_code = 404
        return make_response("", status_code, "")

if __name__ == '__main__':
    app.run(port=5555, debug=True)
