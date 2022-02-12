from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Здесь будет главная"


@app.route("/all")
def all_teachers():
    return "Здесь будут все преподаватели"


@app.route("/goals/<goal>/")
def goal(goal):
    return "Здесь будет цель " + goal


@app.route("/profiles/<teacher_id>/")
def teachers_profiles(teacher_id):
    return "Здесь будет преподаватель " + teacher_id


@app.route("/request/")
def order():
    return "Здесь будет заявка на подбор"


@app.route("/request_done/")
def order_done():
    return "Заявка на подбор отправлена"


@app.route("/booking/<teacher_id>/<week_day>/<time>/")
def booking(teacher_id, week_day, time):
    return "Здесь будет форма бронирования " + teacher_id


@app.route("/booking_done/")
def booking_done():
    return "Заявка отправлена"


if __name__ == "__main__":
    app.run(debug=True)