import threading
from flask import Flask, send_file, request
from client import Client
from bot import start, new_request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        data = []
        for list_type in request.form.keys():
            list = request.form.getlist(list_type)
            data.append(list[0])

        client = Client(data).insert()
        new_request()

    return send_file('templates/test.html')


def start_server():
    app.run(port=8080)


if __name__ == '__main__':
    thread1 = threading.Thread(target=start_server)
    thread2 = threading.Thread(target=start)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
