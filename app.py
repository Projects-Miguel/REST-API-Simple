from flask import Flask, jsonify, request
#from flask import jsonify

app = Flask(__name__)




from products import products
from inventary import inventary


@app.route('/prueba')
def prueba():
    return jsonify({"message": "pong!"})

@app.route('/products')
def getProducts():
    return jsonify({"products": products, "message": "List of products" })

@app.route('/inventarios')
def getInventary():
    return jsonify({"inventarios": inventary})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name ]
    #capturar el error
    if (len(productFound) > 0):
        return jsonify({"product":  productFound[0]})
    return jsonify({"message" :  "Product not found"})

@app.route('/products', methods=['POST'])
def addProducts():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity" : request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"message": "Product Added Succesfully", "products": products})



if __name__ == '__main__':
    app.run(debug=True, port=4000)