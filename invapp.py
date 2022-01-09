from flask import Flask, jsonify, request 

appinv = Flask (__name__) 

from inventarys import inventarys

@appinv.route('/pruebas')
def pruebas():
    return jsonify({"Message": " Prueba exitosa"})


@appinv.route('/inventarys')
def getInventarys():
    return jsonify({"inventary": inventarys ,"Message": "List of inventary"})


@appinv.route('/inventary/<string:inventary_name>')
def getInventary(inventary_name):
    inventaryFound = [inventary for inventary in inventarys if inventary['name'] == inventary_name]
    if (len(inventaryFound) > 0):
        return jsonify({"inventary": inventaryFound[0]})
    return jsonify({"message": "Inventary not Found"})

@appinv.route('/inventary', methods=['POST'])
def addInventary():
    new_inventary = {
        "name" : request.json['name'],
        "codigo": request.json['codigo'],
        "referencia": request.json['referencia']
    }
    inventarys.append(new_inventary)
    return jsonify({"message": "Inventary Added Succesfully", "inventary": inventarys})

@appinv.route('/inventarys/string:inventary_name', methods=['PUT'])
def editInventary(inventary_name):
    inventaryFound = [inventary for inventary in inventarys if inventary ['name'] == inventary_name ]
    if (len(inventaryFound) > 0):
        inventaryFound[0]['name'] = request.json['name']
        inventaryFound[0]['codigo'] = request.json['codigo']
        inventaryFound[0]['referencia'] = request.json['referencia']
        return jsonify({
            "message": "inventary Updated",
            "inventary": inventaryFound[0]
        })
    return jsonify({'message': "Inventary Not found"})

@appinv.route('/inventary/<string:inventary_name>', methods= ['DELETE'])
def deleteInventary(inventary_name):
    inventaryFound = [inventary for inventary in inventarys if inventary ['name'] == inventary_name]
    if len(inventaryFound) > 0:
        inventarys.remove(inventaryFound)
        return jsonify({
            "message": "inventary deleted",
            "inventary": inventarys
        })
    return jsonify({"message": "Inventary Not Found"})


if __name__ == '__main__':
    appinv.run(debug=True, port=3000)