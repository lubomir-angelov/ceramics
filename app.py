from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

import models

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ceramics:DYC42S3BVZjyrylfcCD0@localhost/GK_Pottery'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/load_tbl_layers")
def load_tbl_layers():
    return render_template("tbl_layers.html")


@app.route("/load_tbl_layer_includes")
def load_tbl_layer_includes():
    return render_template("tbl_layer_includes.html")


@app.route("/load_tbl_fragments")
def load_tbl_fragments():
    return render_template("tbl_fragments.html")


@app.route("/load_tbl_ornaments")
def load_tbl_ornaments():
    return render_template("tbl_ornaments.html")


@app.route("/load_tbl_pok")
def load_tbl_pok():
    return render_template("tbl_pok.html")


@app.route("/load_layers", methods=['POST'])
def load_layers():
    site = request.form["site"]
    sector = request.form["sector"]
    square = request.form["square"]
    context = request.form["context"]
    layer = request.form["layer"]
    stratum = request.form["stratum"]
    level = request.form["level"]
    structure = request.form["structure"]
    includes = request.form["includes"]
    color1 = request.form["color1"]
    color2 = request.form["color2"]
    recordenteredby = request.form["recordenteredby"]
    recordcreatedby = request.form["recordcreatedby"]
    recordcreatedon = request.form["recordcreatedon"]
    description = request.form["description"]
    akb_num = request.form["akb_num"]
    entry = models.Tbllayer(site, sector, square, context, layer, stratum, level,
                 structure, includes, color1, color2, recordenteredby,
                     recordcreatedby, recordcreatedon, description, akb_num)
    db.session.add(entry)
    name = entry.recordenteredby
    print(name)
    #hist = inspect(entry).attrs.myattribute.history
    db.session.commit()

    layer_id = (models.Tbllayer.query.filter_by(recordenteredby=name).order_by(models.Tbllayer.layerid.desc()).first())
    flash(f'Your layer id is: {layer_id}')


    #return hist

    return render_template("tbl_layers.html")


@app.route("/load_layer_includes", methods=['POST'])
def load_layer_includes():
    includetype = request.form["includetype"]
    includetext = request.form["includetext"]
    includesize = request.form["includesize"]
    includeconc = request.form["includeconc"]
    entry = models.Tbllayerinclude(includetype, includetext, includesize, includeconc)
    db.session.add(entry)
    db.session.commit()

    return render_template("tbl_layer_includes.html")


@app.route("/load_fragments", methods=['POST'])
def load_fragments():
    technology = request.form["technology"]
    speed = request.form["speed"]
    baking = request.form["baking"]
    fract = request.form["fract"]
    primarycolor = request.form["primarycolor"]
    secondarycolor = request.form["secondarycolor"]
    covering = request.form["covering"]
    includesconc = request.form["includesconc"]
    includessize = request.form["includessize"]
    includestype = request.form["includestype"]
    surface = request.form["surface"]
    count = request.form["count"]
    onepot = request.form["onepot"]
    piecetype = request.form["piecetype"]
    wallthickness = request.form["wallthickness"]
    handlesize = request.form["handlesize"]
    handletype = request.form["handletype"]
    dishsize = request.form["dishsize"]
    topsize = request.form["topsize"]
    necksize = request.form["necksize"]
    bodysize = request.form["bodysize"]
    bottomsize = request.form["bottomsize"]
    dishheight = request.form["dishheight"]
    bottomtype = request.form["bottomtype"]
    outline = request.form["outline"]
    category = request.form["category"]
    form = request.form["form"]
    type = request.form["type"]
    subtype = request.form["subtype"]
    variant = request.form["variant"]
    note= request.form["note"]
    inventory = request.form["inventory"]
    decoration = request.form["decoration"]
    composition = request.form["composition"]
    parallels = request.form["parallels"]
    recordenteredby = request.form["recordenteredby"]
    entry = models.Tblfragment(technology, speed, baking, fract, primarycolor, secondarycolor, covering, includesconc, includessize,
                 includestype, surface, count, onepot, piecetype, wallthickness, handlesize, handletype, dishsize, topsize,
                 necksize, bodysize, bottomsize, dishheight, bottomtype, outline, category, form, type, subtype, variant,
                 note, inventory, decoration, composition, parallels, recordenteredby)
    db.session.add(entry)
    name = entry.recordenteredb
    db.session.commit()

    fragment_id  = (models.Tblfragments.query.filter_by(recordenteredby=name).order_by(models.Tblfragments.fragmentid.desc()).first())
    flash(f'Your fragment id is: {fragment_id}')

    return render_template("tbl_fragments.html")


@app.route("/load_ornaments", methods=['POST'])
def load_ornaments():
    location = request.form["location"]
    relationship = request.form["relationship"]
    onornament = request.form["onornament"]
    color1 = request.form["color1"]
    color2 = request.form["color2"]
    encrustcolor1 = request.form["encrustcolor1"]
    encrustcolor2 = request.form["encrustcolor2"]
    primary_ = request.form["primary_"]
    secondary = request.form["secondary"]
    tertiary = request.form["tertiary"]
    quarternary = request.form["quarternary"]
    entry = models.Tblornament(location, relationship, onornament, color1, color2, encrustcolor1, encrustcolor2, primary_, secondary,
                 tertiary, quarternary)
    db.session.add(entry)
    db.session.commit()

    return render_template("tbl_ornaments.html")


@app.route("/load_pok", methods=['POST'])
def load_pok():
    type = request.form["type"]
    quantity = request.form["quantity"]
    weight = request.form["weight"]
    entry = models.Tblpok(type, quantity, weight)
    db.session.add(entry)
    db.session.commit()

    return render_template("tbl_pok.html")


if __name__ == '__main__':
    app.run()