from flask import Flask, jsonify
import constants
import read_loadfile
import json

app = Flask(__name__)



@app.route('/merchantdetails/getmerchantname/<string:merchant_id>', methods=['GET'])
def get_merchantname(merchant_id):
    db_merchant=read_loadfile.get_merchant_details(merchant_id,read_loadfile.merchants_dict)
    merchantdict={}
    merchantdict['id']=db_merchant.id
    merchantdict['name']=db_merchant.name
    return jsonify(merchantdict)

@app.route('/merchantdetails/getfullmerchant/<string:merchant_id>', methods=['GET'])
def get_fullmerchant(merchant_id):
    db_merchant=read_loadfile.get_merchant_details(merchant_id,read_loadfile.merchants_dict)
    merchantdict={}
    merchantdict['id']=db_merchant.id
    merchantdict['name']=db_merchant.name
    merchantdict['customer_id']=db_merchant.customer_id
    merchantdict['transact_amount']=db_merchant.transact_amount
    merchantdict['check_fraud']=db_merchant.check_fraud
    merchantdict['age']=db_merchant.age
    merchantdict['gender']=db_merchant.gender
    merchantdict['zipcode_ori']=db_merchant.zipcode_ori
    merchantdict['zipcode_dest']=db_merchant.zipcode_dest
    merchantdict['category']=db_merchant.category
    return jsonify(merchantdict)
    
if __name__ == '__main__':
    read_loadfile.load_merchants(constants.filename)
    app.run(debug=True)