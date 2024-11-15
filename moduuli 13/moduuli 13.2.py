from flask import Flask, request, jsonify
import mysql.connector


def get_airport_location_by_icao(icao):
    sql = f'SELECT ident, name, municipality FROM airport WHERE ident=%s'
    cursor = db_connection.cursor()
    cursor.execute(sql, (icao,))
    airport_name = cursor.fetchone()
    cursor.close()
    return airport_name


db_connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='Possu2929',
    autocommit=True,
    collation="utf8mb4_general_ci"
)


app = Flask(__name__)
@app.route('/kenttä/<string:icao>', methods=['GET'])
def kenttä(icao):
    info=get_airport_location_by_icao(icao)
    ident, name, municipality = info
    return jsonify({"Icao": ident,"name": name,"municipality": municipality})



if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)