from models.TsrShopDetails_models import *


#   or show(mobile & name)
# http://127.0.0.1:5000/TsrShopDetailsProject/get/or/mobile/name/data?Mobile_number=7097535317&name=sagar

@app.route('/TsrShopDetailsProject/get/or/mobile/name/data', methods=['GET'])
def or_method_fetch():
    mobileNumber = request.args.get('Mobile_number')
    NameFull = request.args.get('name')
    results = session.query(TsrShopDetailsProject).filter(
        or_(TsrShopDetailsProject.Mobile_number == mobileNumber, TsrShopDetailsProject.Name == NameFull)).all()
    results4 = [item.__dict__ for item in results]
    for item in results4:
        del item['_sa_instance_state']
    return json.dumps(results4)


if __name__ == "__main__":
    # Run the APP
    app.run(debug=False)

