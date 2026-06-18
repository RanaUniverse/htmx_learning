from flask import Flask, render_template


import fake_data
from time_data import get_now_time_in_str

app = Flask(__name__)


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
