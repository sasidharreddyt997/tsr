from models.TsrShopDetails_models import *


# 'limite&offset'
# http://127.0.0.1:5000/TsrShopDetailsProject/get/limite/offset/data

@app.route('/TsrShopDetailsProject/get/limite/offset/data', methods=['GET'])
def get_limited_data():
    # Limit: How many leads to distribute, offset: Stating point
    result = session.query(TsrShopDetailsProject).limit(1).offset(2).all()
    results5 = [item.__dict__ for item in result]
    for item in results5:
        del item['_sa_instance_state']
    return json.dumps(results5)


if __name__ == "__main__":
    # Run the APP
    app.run(debug=False)
