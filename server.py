import threading
from flask import Flask, render_template, redirect, url_for, request
from query import insert
from bot import start, new_request

application = Flask(__name__)


@application.route('/')
def main_page():
    return render_template('index.html', title='PW Tech')


@application.route('/technology')
def technology():
    return render_template('technology.html', title='Технология')


@application.route('/team')
def team():
    return render_template('team.html', title='Команда')


@application.route('/projects')
def projects():
    return render_template('projects.html', title='Проекты')


@application.route('/contact')
def contact():
    return render_template('contact.html', title='Связаться с нами')


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
    application.run(port=8080)


if __name__ == '__main__':
    thread1 = threading.Thread(target=start_server)
    thread2 = threading.Thread(target=start)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
