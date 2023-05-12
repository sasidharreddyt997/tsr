from models.TsrShopDetails_models import *


# http://127.0.0.1:5000/TsrShopDetails/task1/getmethod

@app.route('/TsrShopDetails/task1/getmethod', methods=['GET'])
def tsr_shop_details():
    results = session.query(TsrShopDetailsProject).all()
    results_1 = [item.__dict__ for item in results]
    for item in results_1:
        del item['_sa_instance_state']
    return json.dumps(results_1)


if __name__ == "__main__":
    # Run the APP
    app.run(debug=False)
