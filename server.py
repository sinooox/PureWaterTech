import threading
from flask import Flask, render_template, redirect, url_for, request
from query import insert
from bot import start, new_request


application = Flask(__name__)


@application.route('/')
def main_page():
    return render_template('test.html')


@application.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        data = []
        for list_type in request.form.keys():
            list = request.form.getlist(list_type)
            data.append(list[0])

        id = insert(f"""INSERT INTO contacts (name, phone, city, company) VALUES ('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}')""")
        new_request(id)

    return redirect(url_for('main_page'))


def start_server():
    while True:
        try:
            application.run(port=8080)
        except Exception as error:
            print(error)


if __name__ == '__main__':
    thread1 = threading.Thread(target=start_server)
    thread2 = threading.Thread(target=start)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
