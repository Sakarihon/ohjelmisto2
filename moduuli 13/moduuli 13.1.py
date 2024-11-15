from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/alkuluku/<int:luku1>')
def alkuluku(luku1):

    if luku1 > 1:

        for i in range(2, (luku1 // 2) + 1):
            if (luku1 % i == 0):

                return jsonify({"luku1": luku1, "prime": False})
        else:
            return jsonify({"luku1": luku1, "prime": True})
    else:
        return jsonify({"luku1": luku1, "prime": False})



if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
