import time

from flask import Flask, render_template
from flask import request
import fake_data
from time_data import get_now_time_in_str

app = Flask(__name__)

i = 0


@app.route("/shift_clicked")
def shift_clicked():
    print("Shift-click detected!")
    return "<p>You shift-clicked the div!</p>"


DATA = [
    "Apple",
    "Banana",
    "Orange",
    "Mango",
    "Grapes",
    "Pineapple",
]


def is_htmx() -> bool:
    return request.headers.get("HX-Request") == "true"


@app.route("/search")
def search():
    time.sleep(2)
    print("xxx")
    print(
        "Remote addr",
        request.remote_addr,
    )
    print(request)

    if is_htmx():
        print("This is from htmx.")
    else:
        print("This is not from htmx from normal get.")

    print("yyy")
    q = request.args.get("q", "").lower()
    print(request.headers)
    print("zzz")
    print(request.args.get("q"))

    results = [item for item in DATA if q in item.lower()]

    return render_template(
        "partials/search_results.html",
        results=results,
    )


@app.route("/mouse_entered", methods=["POST"])
def mouse_entered():
    global i
    i += 1
    print(f"Mouse entered! {i}")
    return f"<p>You triggered the trap!{i}</p>"


# i will use this for the htmx just to replace the name
@app.route("/random-name")
def random_name():
    data = fake_data.generate_fake_name()  # thasdnk

    return render_template(
        "partials/name.html",
        data=data,
    )


@app.route("/messages")
def htmx1():
    global i
    i += 1

    if request.headers.get("HX-Request"):
        print("This is an HTMX request")
    else:
        print("Normal browser request")

    return f"<div>You have {i} new messages</div>"


# @app.route("/random-name")
# def random_name():
#     return fake_data.generate_fake_name()


@app.context_processor
def inject_globals():
    return {
        "now_str_time": get_now_time_in_str(),
        "site_name": "🚀 Rana Universe",
    }


@app.route(rule="/")
def index_page():
    data = fake_data.generate_fake_name()

    return render_template(
        "index.html",
        data=data,
    )


@app.route("/click")
def click():
    time.sleep(5)
    return "<p>Request completed!</p>"


@app.route("/hello")
def hello_small():
    return "<p>Done!</p>"


# Route 2: Handles the htmx account deletion request
@app.route("/account", methods=["DELETE"])
def delete_account():
    # In a real app, you'd delete the user from the database here ❌ 💾

    # htmx replaces the button with whatever HTML text we return here!
    print("Request Came Now")
    return """
    <div style="color: #dc3545; font-weight: bold; margin-top: 20px;">
        💔 Your account has been permanently deleted. We are sad to see you go!
    </div>
    """


@app.route(rule="/2")
def two_page():

    return render_template(
        "2.html",
    )


@app.route(rule="/3")
def three_page():

    return render_template(
        "3.html",
    )


@app.route(rule="/get-status")
def two_page2():

    return "This is a status"


@app.delete(rule="/user/1")
def two_page22():

    return "This is USER 2"


@app.route("/welcome")
def welcome():
    return "<h4>Page loaded successfully 🚀</h4>"


@app.route("/lazy")
def lazy():
    return "<p>Lazy loaded content 👀</p>"


@app.route("/rana")
def rana_page():
    return render_template(
        template_name_or_list="rana.html",
    )


@app.route("/example")
def example_get():
    import random

    x = random.randint(1, 11111111)
    return f"<u>Thanks {x}</u>"


@app.route(rule="/about")
def about_page():
    return render_template(
        "about.html",
    )


@app.route(rule="/services")
def services_page():
    return render_template(
        "services.html",
    )


@app.route(rule="/contact")
def contact_page():
    return render_template(
        "contact.html",
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=9999,
        debug=True,
    )
