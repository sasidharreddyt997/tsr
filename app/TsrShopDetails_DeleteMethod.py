from models.TsrShopDetails_models import *


# http://127.0.0.1:5000/TsrShopDetailsProject/delete?mobile_number=99090


@app.route('/TsrShopDetailsProject/delete', methods=['DELETE'])
def tsr_delete_records():
    mobileNumber = int(request.args.get('mobile_number'))
    session.query(TsrShopDetailsProject).filter(TsrShopDetailsProject.Mobile_number == mobileNumber).delete()
    session.commit()
    return "Customer record with {} number has been deleted".format(mobileNumber)


if __name__ == "__main__":
    # Run the APP
    app.run(debug=False)

