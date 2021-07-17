from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ceramics:<some_password>@localhost/GK_Pottery'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

db = SQLAlchemy(app)

@app.route('/')
def home():
    return (
            '<a href="/addperson"><button> Load into tbl_layers </button></a>',
            '<a href="/addperson"><button> Load into tbl_layer_includes </button></a>',
            '<a href="/addperson"><button> Load into tbl_fragments </button></a>',
            '<a href="/addperson"><button> Load into tbl_ornaments </button></a>',
            '<a href="/addperson"><button> Load into tbl_pok </button></a>'
    )


@app.route("/load_tbl_layers")
def load_tbl_layers():
    return render_template("tbl_layers.html")


@app.route("/load_tbl_layer_includes")
def load_tbl_layers():
    return render_template("tbl_layer_includes.html")


@app.route("/load_tbl_fragments")
def load_tbl_layers():
    return render_template("tbl_fragments.html")


@app.route("/load_tbl_ornaments")
def load_tbl_layers():
    return render_template("tbl_ornaments.html")


@app.route("/load_tbl_pok")
def load_tbl_layers():
    return render_template("tbl_pok.html")


@app.route("/load_layers", methods=['POST'])
def load_layers():
    pname = request.form["pname"]
    color = request.form["color"]
    entry = People(pname, color)
    db.session.add(entry)
    db.session.commit()

    return render_template("tbl_layers.html")


@app.route("/load_layer_includes", methods=['POST'])
def load_layer_includes():
    pname = request.form["pname"]
    color = request.form["color"]
    entry = People(pname, color)
    db.session.add(entry)
    db.session.commit()

    return render_template("tbl_layer_includes.html")


@app.route("/load_fragments", methods=['POST'])
def load_fragments():
    pname = request.form["pname"]
    color = request.form["color"]
    entry = People(pname, color)
    db.session.add(entry)
    db.session.commit()

    return render_template("tbl_fragments.html")


@app.route("/load_ornaments", methods=['POST'])
def load_ornaments():
    pname = request.form["pname"]
    color = request.form["color"]
    entry = People(pname, color)
    db.session.add(entry)
    db.session.commit()

    return render_template("tbl_ornaments.html")


@app.route("/load_pok", methods=['POST'])
def load_pok():
    pname = request.form["pname"]
    color = request.form["color"]
    entry = People(pname, color)
    db.session.add(entry)
    db.session.commit()

    return render_template("tbl_pok.html")


if __name__ == '__main__':
    app.run()