from models.TsrShopDetails_models import *

#                                   "one column show(mobile)"
# http://127.0.0.1:5000/KxnCompany/get/mobileColumn/details?mobile_number=7097535317
@app.route('/TsrShopDetailsProject/get/mobileColumn/details', methods=['GET'])
def one_column_show():
    mobileNumber = request.args.get('mobile_number')
    results = session.query(TsrShopDetailsProject).filter(TsrShopDetailsProject.Mobile_number == mobileNumber).all()
    results_3=[item.__dict__ for item in results]
    for item in results_3:
        del item['_sa_instance_state']
    return json.dumps(results_3)


if __name__ == "__main__":
    # Run the APP
    app.run(debug=False)