from models.TsrShopDetails_models import *

"""
http://127.0.0.1:5000/TsrShopDetailsProject/post/method
Body- raw
[{"name": "tsr","email": "tsr123@gmail.com","city": "kadapa","state": "ap","dealer":"yyy","vehicle":"ap033333","dealer_city":"kadapa","mobile_number": 9876543}]
"""


@app.route('/TsrShopDetailsProject/post/method', methods=['POST'])
def insert_records():
    # Read the request body!
    try:
        request_body = request.get_json(force=True)
        for item in request_body:
            record = TsrShopDetailsProject(Name=item.get("name"),
                                           Email=item.get("email"),
                                           City=item.get("city"),
                                           State=item.get("state"),
                                           Dealer=item.get("dealer"),
                                           Vehicle=item.get("vehicle"),
                                           Dealer_city=item.get("dealer_city"),
                                           Mobile_number=item.get("mobile_number"))
            session.add_all([record])
        session.commit()

        return {"status": "Success"}
    except Exception as err:
        session.rollback()
        return {"status": "Failed", "msg": str(err)}


if __name__ == "__main__":
    # Run the APP
    app.run(debug=False)
