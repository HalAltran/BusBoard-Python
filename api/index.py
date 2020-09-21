from http.server import BaseHTTPRequestHandler
from flask import Flask, render_template, request
from api.BusBoard import BusBoard

app = Flask(__name__)


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        return index()


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/busInfo")
def busInfo():
    postcode = request.args.get('postcode')
    max_distance = request.args.get('distance')
    bus_board = BusBoard(postcode, max_distance)
    return render_template('info.html', bus_board=bus_board)


if __name__ == "__main__":
    app.run()
