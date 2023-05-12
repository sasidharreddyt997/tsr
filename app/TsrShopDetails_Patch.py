from models.TsrShopDetails_models import *


# http://127.0.0.1:5000/TsrShopDetailsProject/update-city?mobile=7097535317&city=tiruapti


@app.route('/TsrShopDetailsProject/update-city', methods=['PATCH'])
def tsr_shop_details_update_address():
    mobile = request.args.get('mobile_number')
    City = request.args.get('city')
    session.query(TsrShopDetailsProject).filter(TsrShopDetailsProject.Mobile_number == mobile).update({"City": City})
    session.commit()
    return "address has been updated"


if __name__ == "__main__":
    # Run the APP
    app.run(debug=False)
