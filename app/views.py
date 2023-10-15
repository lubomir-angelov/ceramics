from flask import render_template, request, redirect, url_for, flash

from app import app
from app import db
from app import models
from app.forms import *
from flask_bootstrap import Bootstrap
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse
from app.forms import LoginForm, RegistrationForm


@app.route('/')
@login_required
def index():
    return render_template("index.html")

# Table Tbllayers
@app.route("/layers")
def layers():
    page = request.args.get('page', 1, type=int)
    all_data = models.Tbllayer.query.order_by(models.Tbllayer.recordenteredon.desc()).paginate(page=page,
                                                                                               per_page=5,
                                                                                               error_out=False)
    next_url = url_for('layers', page=all_data.next_num) \
        if all_data.has_next else None
    prev_url = url_for('layers', page=all_data.prev_num) \
        if all_data.has_prev else None
    return render_template("layers.html",
                           layers=all_data.items,
                           next_url=next_url,
                           prev_url=prev_url
                           )


# Add Layer form
@app.route("/layers/add", methods=['GET', 'POST'])
def layers_add():
    # we are adding not updating
    update = None
    # render the form
    flask_form_layers = AddLayerForm(request.form)
    if request.method == 'POST':
        if flask_form_layers.validate_on_submit():
            site = flask_form_layers.site.data
            sector = flask_form_layers.sector.data
            square = flask_form_layers.square.data
            context = flask_form_layers.context.data
            layer = flask_form_layers.layer.data
            stratum = flask_form_layers.stratum.data
            level = flask_form_layers.level.data
            structure = flask_form_layers.structure.data
            includes = flask_form_layers.includes.data
            color1 = flask_form_layers.color1.data
            color2 = flask_form_layers.color2.data
            recordenteredby = flask_form_layers.recordenteredby.data
            recordcreatedby = flask_form_layers.recordcreatedby.data
            recordcreatedon = flask_form_layers.recordcreatedon.data
            description = flask_form_layers.description.data
            akb_num = flask_form_layers.akb_num.data

            entry = flask_form_layers.save_entry(Tbllayer(site, sector, square, context, layer, stratum, level,
                                             structure, includes, color1, color2, recordenteredby,
                                             recordcreatedby, recordcreatedon, description, akb_num))
            db.session.add(entry)
            name = entry.recordenteredby
            try:
                db.session.commit()
                layer_id = (Tbllayer.query.filter_by(recordenteredby=name).order_by(
                    Tbllayer.recordenteredon.desc()).first()).__dict__['layerid']

                if request.form.to_dict()['action'] == 'ДОБАВИ ПЛАСТ':
                    # #flash(f'Пластът е добавен успешно! Нов пласт номер: {layer_id}')
                    return redirect(url_for('layers'))
                if request.form.to_dict()['action'] == 'ДОБАВИ ПРИМЕСИ':
                    return redirect(url_for('layer_includes_add', location_id=layer_id))
                if request.form.to_dict()['action'] == 'ДОБАВИ ПОК':
                    return redirect(url_for('pok_add', location_id=layer_id))
                return redirect(url_for('layers'))
            except Exception as e:
                flash("Грешка! Възникна проблем при въвеждането... опитайте отново.")
                return render_template('layer.html', form=flask_form_layers, update=update)
        else:
            flash('Формата съдържа невалидни данни! Опитайте отново.')
            return render_template('layer.html', form=flask_form_layers, update=update)
    else:
        # this is a get request, show the form
        return render_template('layer.html', form=flask_form_layers, update=update)


# Update Layer form
@app.route('/layers/update/<current_layerid>', methods = ['GET', 'POST'])
def layers_update(current_layerid):
    # we are updating not adding
    update = True
    flask_form = AddLayerForm(request.form)
    if request.method == 'POST':
        if flask_form.validate_on_submit():
            site = flask_form.site.data
            sector = flask_form.sector.data
            square = flask_form.square.data
            context = flask_form.context.data
            layer = flask_form.layer.data
            stratum = flask_form.stratum.data
            level = flask_form.level.data
            structure = flask_form.structure.data
            includes = flask_form.includes.data
            color1 = flask_form.color1.data
            color2 = flask_form.color2.data
            recordenteredby = flask_form.recordenteredby.data
            recordcreatedby = flask_form.recordcreatedby.data
            recordcreatedon = flask_form.recordcreatedon.data
            description = flask_form.description.data
            akb_num = flask_form.akb_num.data

            layer_record_to_update = Tbllayer.query.get_or_404(current_layerid)
            layer_record_to_update.site = site
            layer_record_to_update.sector = sector
            layer_record_to_update.square = square
            layer_record_to_update.context = context
            layer_record_to_update.layer = layer
            layer_record_to_update.stratum = stratum
            layer_record_to_update.level = level
            layer_record_to_update.structure = structure
            layer_record_to_update.includes = includes
            layer_record_to_update.color1 = color1
            layer_record_to_update.color2 = color2
            layer_record_to_update.recordenteredby = recordenteredby
            layer_record_to_update.recordcreatedby = recordcreatedby
            layer_record_to_update.recordcreatedon = recordcreatedon
            layer_record_to_update.description = description
            layer_record_to_update.akb_num = akb_num

            includes_location_id = current_layerid
            pok_location_id = current_layerid
            try:
                db.session.commit()
                if request.form.to_dict()['action'] == 'Пласт':
                    return redirect(url_for('layers'))
                if request.form.to_dict()['action'] == 'ДОБАВИ ПРИМЕСИ':
                    include_id = Tbllayerinclude.query.filter_by(locationid=includes_location_id).first().__dict__['includeid']
                    return redirect(url_for('layer_includes_update', current_includeid=include_id))
                if request.form.to_dict()['action'] == 'ДОБАВИ ПОК':
                    pok_id = Tblpok.query.filter_by(locationid=pok_location_id).first().__dict__['pokid']
                    return redirect(url_for('pok_update', current_pokid=pok_id))
                return redirect(url_for('layers'))
            except Exception as e:
                flash(f"Грешка! Възникна проблем при въвеждането... опитайте отново. {e}")
                return render_template('layer.html', form=flask_form, update=update)
        else:
            flash('Формата съдържа невалидни данни! Опитайте отново.')
            return render_template('layer.html', form=flask_form, update=update)
    else:
        # this is a get request, show the form
        # pre-populate form data from DB
        current_layer_data = Tbllayer.query.get_or_404(current_layerid)
        flask_form.site.data = current_layer_data.site
        flask_form.sector.data = current_layer_data.sector
        flask_form.square.data = current_layer_data.square
        flask_form.context.data = current_layer_data.context
        flask_form.layer.data = current_layer_data.layer
        flask_form.stratum.data = current_layer_data.stratum
        flask_form.level.data = current_layer_data.level
        flask_form.structure.data = current_layer_data.structure
        flask_form.includes.data = current_layer_data.includes
        flask_form.color1.data = current_layer_data.color1
        flask_form.color2.data = current_layer_data.color2
        flask_form.recordenteredby.data = current_layer_data.recordenteredby
        flask_form.recordcreatedby.data = current_layer_data.recordcreatedby
        flask_form.recordcreatedon.data = current_layer_data.recordcreatedon
        flask_form.description.data = current_layer_data.description
        flask_form.akb_num.data = current_layer_data.akb_num

        return render_template('layer.html', form=flask_form, update=update)


@app.route("/fragments")
def fragments():
    page = request.args.get('page', 1, type=int)
    all_data = Tblfragment.query.order_by(Tblfragment.recordenteredon.desc()).paginate(page=page,
                                                                                       per_page=6,
                                                                                       error_out=False)
    next_url = url_for('fragments', page=all_data.next_num) \
        if all_data.has_next else None
    prev_url = url_for('fragments', page=all_data.prev_num) \
        if all_data.has_prev else None
    return render_template("fragments.html",
                           fragments=all_data.items,
                           next_url=next_url,
                           prev_url=prev_url
                           )


@app.route("/fragments/add", methods=['GET', 'POST'])
def fragments_add():
    flask_form_fragments = AddFragmentForm(request.form)
    # we are adding not updating
    update = None
    if request.method == 'POST' and flask_form_fragments.validate_on_submit():
        technology = flask_form_fragments.technology.data
        #speed = flask_form_fragments.speed.data
        baking = flask_form_fragments.baking.data
        fract = flask_form_fragments.fract.data
        primarycolor = flask_form_fragments.primarycolor.data
        secondarycolor = flask_form_fragments.secondarycolor.data
        covering = flask_form_fragments.covering.data
        includesconc = flask_form_fragments.includesconc.data
        includessize = flask_form_fragments.includessize.data
        #includestype = flask_form_fragments.includestype.data
        surface = flask_form_fragments.surface.data
        count = flask_form_fragments.count.data
        onepot = flask_form_fragments.onepot.data
        piecetype = flask_form_fragments.piecetype.data
        wallthickness = flask_form_fragments.wallthickness.data
        #handlesize = flask_form_fragments.handlesize.data
        handletype = flask_form_fragments.handletype.data
        dishsize = flask_form_fragments.dishsize.data
        #topsize = flask_form_fragments.topsize.data
        #necksize = flask_form_fragments.necksize.data
        #bodysize = flask_form_fragments.bodysize.data
        #bottomsize = flask_form_fragments.bottomsize.data
        #dishheight = flask_form_fragments.dishheight.data
        bottomtype = flask_form_fragments.bottomtype.data
        outline = flask_form_fragments.outline.data
        category = flask_form_fragments.category.data
        form = flask_form_fragments.form.data
        type = flask_form_fragments.type.data
        subtype = flask_form_fragments.subtype.data
        variant = flask_form_fragments.variant.data
        note= flask_form_fragments.note.data
        inventory = flask_form_fragments.inventory.data
        #decoration = flask_form_fragments.decoration.data
        #composition = flask_form_fragments.composition.data
        #parallels = flask_form_fragments.parallels.data
        recordenteredby = flask_form_fragments.recordenteredby.data

        # get layerid from Tbllayers to add as location id
        location_id = Tbllayer.query.filter_by(recordenteredby=recordenteredby).order_by(
            Tbllayer.recordenteredon.desc()).first().__dict__['layerid']
        entry = flask_form_fragments.save_entry(
            Tblfragment(location_id, technology, baking, fract, primarycolor, secondarycolor, covering,
                        includesconc, includessize, surface, count, onepot, piecetype,
                        wallthickness, handletype, dishsize,
                        bottomtype, outline, category, form, type, subtype, variant,
                        note, inventory, recordenteredby))
        db.session.add(entry)
        try:
            db.session.commit()
            # get the fragment id of the new record
            fragment_id = Tblfragment.query.filter_by(recordenteredby=recordenteredby).order_by(
                Tblfragment.fragmentid.desc()).first().__dict__['fragmentid']
            if request.form.to_dict()['action'] == 'ДОБАВИ ФРАГМЕНТИ':
                return redirect(url_for('fragments'))
            if request.form.to_dict()['action'] == 'ДОБАВИ УКРАСА':
                return redirect(url_for('ornaments_add', fragment_id=fragment_id))
            return redirect(url_for('fragments'))
        except Exception as e:
            flash(f'Грешка! Възникна проблем при добавянето... Опитайте отново. {e}')
            return render_template('fragment.html', form=flask_form_fragments, update=update)
    else:
        # this is a get request, show the form
        return render_template('fragment.html', form=flask_form_fragments, update=update)


@app.route('/fragments/update/<current_fragmentid>', methods = ['GET', 'POST'])
def fragments_update(current_fragmentid):
    # we are updating not adding
    update = True
    flask_form = AddFragmentForm(request.form)
    if request.method == 'POST':
        if flask_form.validate_on_submit():
            technology = flask_form.technology.data
            #speed = flask_form.speed.data
            baking = flask_form.baking.data
            fract = flask_form.fract.data
            primarycolor = flask_form.primarycolor.data
            secondarycolor = flask_form.secondarycolor.data
            covering = flask_form.covering.data
            includesconc = flask_form.includesconc.data
            includessize = flask_form.includessize.data
            #includestype = flask_form.includestype.data
            surface = flask_form.surface.data
            count = flask_form.count.data
            onepot = flask_form.onepot.data
            piecetype = flask_form.piecetype.data
            wallthickness = flask_form.wallthickness.data
            #handlesize = flask_form.handlesize.data
            handletype = flask_form.handletype.data
            dishsize = flask_form.dishsize.data
            #topsize = flask_form.topsize.data
            #necksize = flask_form.necksize.data
            #bodysize = flask_form.bodysize.data
            #bottomsize = flask_form.bottomsize.data
            #dishheight = flask_form.dishheight.data
            bottomtype = flask_form.bottomtype.data
            outline = flask_form.outline.data
            category = flask_form.category.data
            form = flask_form.form.data
            type = flask_form.type.data
            subtype = flask_form.subtype.data
            variant = flask_form.variant.data
            note = flask_form.note.data
            inventory = flask_form.inventory.data
            #decoration = flask_form.decoration.data
            #composition = flask_form.composition.data
            #parallels = flask_form.parallels.data
            recordenteredby = flask_form.recordenteredby.data

            # get current record
            fragment_record_to_update = Tblfragment.query.get_or_404(current_fragmentid)
            # update record fields with data from form
            fragment_record_to_update.technology = technology
            fragment_record_to_update.baking = baking
            fragment_record_to_update.fract = fract
            fragment_record_to_update.primarycolor = primarycolor
            fragment_record_to_update.secondarycolor = secondarycolor
            fragment_record_to_update.covering = covering
            fragment_record_to_update.includesconc = includesconc
            fragment_record_to_update.includessize = includessize
            fragment_record_to_update.surface = surface
            fragment_record_to_update.count = count
            fragment_record_to_update.onepot = onepot
            fragment_record_to_update.piecetype = piecetype
            fragment_record_to_update.wallthickness = wallthickness
            fragment_record_to_update.handletype = handletype
            fragment_record_to_update.dishsize = dishsize
            fragment_record_to_update.bottomtype = bottomtype
            fragment_record_to_update.outline = outline
            fragment_record_to_update.category = category
            fragment_record_to_update.form = form
            fragment_record_to_update.type = type
            fragment_record_to_update.subtype = subtype
            fragment_record_to_update.variant = variant
            fragment_record_to_update.note = note
            fragment_record_to_update.inventory = inventory
            fragment_record_to_update.recordenteredby = recordenteredby
            try:
                # push updates
                db.session.commit()
                if request.form.to_dict()['action'] == 'ДОБАВИ ФРАГМЕНТИ':
                    return redirect(url_for('fragments'))
                if request.form.to_dict()['action'] == 'ДОБАВИ УКРАСА':
                    ornament_id = Tblornament.query.filter_by(fragmentid=current_fragmentid).first().__dict__['ornamentid']
                    return redirect(url_for('ornaments_update', current_ornamentid=ornament_id))
                return redirect(url_for('fragments'))
            except Exception as e:
                flash(f'Грешка! Възникна проблем при промяната... Опитайте отново. {e}')
                return render_template('fragment.html', form=flask_form, update=update)
        else:
            flash('Формата съдържа невалидни данни! Опитайте отново.')
            return render_template('fragment.html', form=flask_form, update=update)
    else:
        # this is a get request, show the form
        # pre-populate form data from DB
        current_fragment_data = Tblfragment.query.get_or_404(current_fragmentid)
        flask_form.technology.data = current_fragment_data.technology
        flask_form.baking.data = current_fragment_data.baking
        flask_form.fract.data = current_fragment_data.fract
        flask_form.includessize.data = current_fragment_data.includessize
        flask_form.includesconc.data = current_fragment_data.includesconc
        flask_form.surface.data = current_fragment_data.surface
        flask_form.covering.data = current_fragment_data.covering
        flask_form.primarycolor.data = current_fragment_data.primarycolor
        flask_form.secondarycolor.data = current_fragment_data.secondarycolor
        flask_form.category.data = current_fragment_data.category
        flask_form.form.data = current_fragment_data.form
        flask_form.type.data = current_fragment_data.type
        flask_form.subtype.data = current_fragment_data.subtype
        flask_form.variant.data = current_fragment_data.variant
        flask_form.piecetype.data = current_fragment_data.piecetype
        flask_form.wallthickness.data = current_fragment_data.wallthickness
        flask_form.dishsize.data = current_fragment_data.dishsize
        flask_form.handletype.data = current_fragment_data.handletype
        flask_form.bottomtype.data = current_fragment_data.bottomtype
        flask_form.outline.data = current_fragment_data.outline
        flask_form.count.data = current_fragment_data.count
        flask_form.onepot.data = current_fragment_data.onepot
        flask_form.note.data = current_fragment_data.note
        flask_form.inventory.data = current_fragment_data.inventory
        flask_form.recordenteredby.data = current_fragment_data.recordenteredby

        return render_template('fragment.html', form=flask_form, update=update)


@app.route("/layer_includes")
def layer_includes():
    page = request.args.get('page', 1, type=int)
    all_data = models.Tbllayerinclude.query.order_by(models.Tbllayerinclude.recordenteredon.desc()).paginate(page=page,
                                                                                                      per_page=10,
                                                                                                      error_out=False)
    next_url = url_for('layer_includes', page=all_data.next_num) \
        if all_data.has_next else None
    prev_url = url_for('layer_includes', page=all_data.prev_num) \
        if all_data.has_prev else None
    return render_template("layer_includes.html",
                           layer_includes=all_data.items,
                           next_url=next_url,
                           prev_url=prev_url
                           )

@app.route("/layer_includes/add", methods=['GET', 'POST'])
def layer_includes_add():
    # only available when redirected from layers_add !
    location_id = request.args.get('location_id')
    # we are adding not updating
    update = None
    flask_form = AddLayerIncludeForm(request.form)
    if request.method == 'POST':
        if flask_form.validate_on_submit():
            locationid = flask_form.locationid.data
            includetype = flask_form.includetype.data
            includetext = flask_form.includetext.data
            includesize = flask_form.includesize.data
            includeconc = flask_form.includeconc.data

            entry = flask_form.save_entry(models.Tbllayerinclude(locationid, includetype, includetext, includesize, includeconc))
            db.session.add(entry)
            try:
                db.session.commit()
                location_id = Tbllayerinclude.query.order_by(Tbllayerinclude.recordenteredon.desc()).first().__dict__['locationid']
                if request.form.to_dict()['action'] == 'ДОБАВИ ПРИМЕСИ':
                    return redirect(url_for('layer_includes'))
                if request.form.to_dict()['action'] == 'ДОБАВИ ПОК':
                    return redirect(url_for('pok_add', location_id=location_id))
                return redirect (url_for('layer_includes'))
            except Exception as e:
                flash(f'Грешка! Възникна проблем при добавянето... Опитайте отново. Error: {e}')
                return render_template('layer_include.html', form=flask_form, update=update)
        else:
            flash('Формата съдържа невалидни данни! Опитайте отново.')
            return render_template('layer_include.html', form=flask_form, update=update)
    else:
        # this is a get request, show the form
        flask_form.locationid.data = location_id
        return render_template('layer_include.html', form=flask_form, update=update)


@app.route("/layer_includes/update/<current_includeid>", methods = ['GET', 'POST'])
def layer_includes_update(current_includeid):
    # we are updating not adding
    update = True
    flask_form = AddLayerIncludeForm(request.form)
    if request.method == 'POST':
        if flask_form.validate_on_submit():
            locationid = flask_form.locationid.data
            includetype = flask_form.includetype.data
            includetext = flask_form.includetext.data
            includesize = flask_form.includesize.data
            includeconc = flask_form.includeconc.data
            # get current record
            layer_includes_record_to_update = Tbllayerinclude.query.get_or_404(current_includeid)
            # update record with data from form
            layer_includes_record_to_update.locationid = locationid
            layer_includes_record_to_update.includetype = includetype
            layer_includes_record_to_update.includetext = includetext
            layer_includes_record_to_update.includesize = includesize
            layer_includes_record_to_update.includeconc = includeconc
            try:
                db.session.commit()
                if request.form.to_dict()['action'] == 'ДОБАВИ АНТРОПОГЕННИ ПРИМЕСИ':
                    return redirect(url_for('layer_includes'))
                if request.form.to_dict()['action'] == 'ДОБАВИ ПОК':
                    pok_id = Tblpok.query.filter_by(locationid=locationid).first().__dict__['pokid']
                    return redirect(url_for('pok_update', current_pokid=pok_id))
                return redirect (url_for('layer_includes'))
            except:
                flash('Грешка! Възникна проблем при промяната... Опитайте отново.')
                return render_template('layer_include.html', form=flask_form, update=update)
        else:
            flash('Формата съдържа невалидни данни! Опитайте отново.')
            return render_template('layer_include.html', form=flask_form, update=update)
    else:
        # this is a get request, show the form
        # pre-populate form data from DB
        current_layer_includes_data = Tbllayerinclude.query.get_or_404(current_includeid)
        flask_form.locationid.data = current_layer_includes_data.locationid
        flask_form.includetype = current_layer_includes_data.includetype
        flask_form.includetext = current_layer_includes_data.includetext
        flask_form.includesize = current_layer_includes_data.includesize
        flask_form.includeconc = current_layer_includes_data.includeconc

        return render_template('layer_include.html', form=flask_form, update=update)


@app.route("/ornaments")
def ornaments():
    page = request.args.get('page', 1, type=int)
    all_data = models.Tblornament.query.order_by(models.Tblornament.recordenteredon.desc()).paginate(page=page,
                                                                                                     per_page=8,
                                                                                                     error_out=False)
    next_url = url_for('ornaments', page=all_data.next_num) \
        if all_data.has_next else None
    prev_url = url_for('ornaments', page=all_data.prev_num) \
        if all_data.has_prev else None
    return render_template("ornaments.html",
                           ornaments=all_data.items,
                           next_url=next_url,
                           prev_url=prev_url
                           )


@app.route("/ornaments/add", methods=['GET', 'POST'])
def ornaments_add():
    fragment_id = request.args.get('fragment_id')
    # we are adding not updating
    update = None
    flask_form = AddOrnamentForm(request.form)
    if request.method == 'POST':
        if flask_form.validate_on_submit():
            # assign db value for fragment_id to new entry to be added to ornaments
            fragmentid = fragment_id
            # get values from form
            location = flask_form.location.data
            encrustcolor1 = flask_form.encrustcolor1.data
            encrustcolor2 = flask_form.encrustcolor2.data
            primary_ = flask_form.primary_.data
            secondary = flask_form.secondary.data
            tertiary = flask_form.tertiary.data
            quarternary = flask_form.quarternary.data
            entry = flask_form.save_entry(models.Tblornament(fragmentid, location,
                                                             encrustcolor1, encrustcolor2, primary_, secondary,
                                                             tertiary, quarternary))
            db.session.add(entry)
            try:
                db.session.commit()
                flash('Добавянето е успешно!')
                return redirect(url_for('ornaments'))
            except:
                flash('Грешка! Възникна проблем при добавянето... Опитайте отново.')
                return render_template('ornament.html', form=flask_form, update=update)
        else:
            print(flask_form.errors)
            flash('Формата съдържа невалидни данни! Опитайте отново.')
            return render_template('ornament.html', form=flask_form, update=update)
    else:
        # this is a get request, show the form
        # prepoulate form
        flask_form.fragmentid.data = fragment_id
        return render_template('ornament.html', form=flask_form, update=update)


@app.route("/ornaments/update/<current_ornamentid>", methods = ['GET', 'POST'])
def ornaments_update(current_ornamentid):
    # we are updating not adding
    update = True
    flask_form = AddOrnamentForm(request.form)
    if request.method == 'POST':
        if flask_form.validate_on_submit():
            fragmentid = flask_form.fragmentid.data
            location = flask_form.location.data
            encrustcolor1 = flask_form.encrustcolor1.data
            encrustcolor2 = flask_form.encrustcolor2.data
            primary_ = flask_form.primary_.data
            secondary = flask_form.secondary.data
            tertiary = flask_form.tertiary.data
            quarternary = flask_form.quarternary.data
            # get current record
            ornament_record_to_update = Tblornament.query.get_or_404(current_ornamentid)
            # update record with data from form
            ornament_record_to_update.fragmentid = fragmentid
            ornament_record_to_update.location = location
            #ornament_record_to_update.color1 = color1
            #ornament_record_to_update.color2 = color2
            ornament_record_to_update.encrustcolor1 = encrustcolor1
            ornament_record_to_update.encrustcolor2 = encrustcolor2
            ornament_record_to_update.primary_ = primary_
            ornament_record_to_update.secondary = secondary
            ornament_record_to_update.tertiary = tertiary
            ornament_record_to_update.quarternary = quarternary
            try:
                db.session.commit()
                flash('Добавянето е успешно!')
                return redirect(url_for('ornaments'))
            except:
                flash('Грешка! Възникна проблем при промяната... Опитайте отново.')
                return render_template('ornament.html', form=flask_form, update=update)
        else:
            flash('Формата съдържа невалидни данни! Опитайте отново.')
            return render_template('ornament.html', form=flask_form, update=update)
    else:
        # this is a get request, show the form
        # pre-populate form data from DB
        current_ornament_data = Tblornament.query.get_or_404(current_ornamentid)
        flask_form.fragmentid.data = current_ornament_data.fragmentid
        flask_form.location.data = current_ornament_data.location
        #flask_form.color1.data = current_ornament_data.color1
        #flask_form.color2.data = current_ornament_data.color2
        flask_form.encrustcolor1.data = current_ornament_data.encrustcolor1
        flask_form.encrustcolor2.data = current_ornament_data.encrustcolor2
        flask_form.primary_.data = current_ornament_data.primary_
        flask_form.secondary.data = current_ornament_data.secondary
        flask_form.tertiary.data = current_ornament_data.tertiary
        flask_form.quarternary.data = current_ornament_data.quarternary

        return render_template('ornament.html', form=flask_form, update=update)


@app.route("/pok")
def pok():
    page = request.args.get('page', 1, type=int)
    all_data = models.Tblpok.query.order_by(models.Tblpok.recordenteredon.desc()).paginate(page=page,
                                                                                           per_page=10,
                                                                                           error_out=False)
    next_url = url_for('pok', page=all_data.next_num) \
        if all_data.has_next else None
    prev_url = url_for('pok', page=all_data.prev_num) \
        if all_data.has_prev else None
    return render_template("poks.html",
                           poks=all_data.items,
                           next_url=next_url,
                           prev_url=prev_url
                           )


@app.route("/pok/add", methods=['GET', 'POST'])
def pok_add():
    location_id = request.args.get('location_id')
    # we are adding not updating
    update = None
    flask_form = AddPokForm(request.form)
    if request.method == 'POST':
        if flask_form.validate_on_submit():
            locationid = flask_form.locationid.data
            type = flask_form.type.data
            quantity = flask_form.quantity.data
            weight = flask_form.weight.data
            sok_weight = flask_form.sok_weight.data

            entry = flask_form.save_entry(Tblpok(locationid, type, quantity, weight, sok_weight))
            db.session.add(entry)
            try:
                db.session.commit()
                flash('Добавянето е успешно!')
                return redirect(url_for('pok'))
            except:
                flash('Грешка! Възникна проблем при добавянето... Опитайте отново.')
                return render_template('pok.html', form=flask_form, update=update)
        else:
            flash('Формата съдържа невалидни данни! Опитайте отново.')
            return render_template('pok.html', form=flask_form, update=update)
    else:
        # this is a get request, show the form
        flask_form.locationid.data = location_id
        return render_template('pok.html', form=flask_form, update=update)


@app.route("/pok/update/<current_pokid>", methods = ['GET', 'POST'])
def pok_update(current_pokid):
    # we are updating not adding
    update = True
    flask_form = AddPokForm(request.form)
    if request.method == 'POST':
        if flask_form.validate_on_submit():
            locationid = flask_form.locationid.data
            type = flask_form.type.data
            quantity = flask_form.quantity.data
            weight = flask_form.weight.data
            sok_weight = flask_form.sok_weight.data
            # get current record
            print(f'This is debug:')
            print(int(current_pokid))
            pok_record_to_update = Tblpok.query.get_or_404(int(current_pokid))
            # update record with form data
            pok_record_to_update.locationid = locationid
            pok_record_to_update.type = type
            pok_record_to_update.quantity = quantity
            pok_record_to_update.weight = weight
            pok_record_to_update.sok_weight = sok_weight
            try:
                print('This is a test')
                db.session.commit()
                flash('Промяната е успешна!')
                print('Now we should redirect')
                return redirect(url_for('pok'))
            except:
                flash('Грешка! Възникна проблем при промяната... Опитайте отново.')
                return render_template("pok.html", form=flask_form, update=update)
        else:
            flash('Формата съдържа невалидни данни! Опитайте отново.')
            return render_template('pok.html', form=flask_form, update=update)
    else:
        # this is a get request, show the form
        # pre-populate form data from DB
        # Enum fields are not properly pre-populated with DB data due to choice option -> they are skipped
        current_pok_data = Tblpok.query.get_or_404(current_pokid)
        flask_form.locationid.data = current_pok_data.locationid
        flask_form.type.data = current_pok_data.type
        flask_form.quantity.data = current_pok_data.quantity
        flask_form.weight.data = current_pok_data.weight
        flask_form.sok_weight.data = current_pok_data.sok_weight

        return render_template('pok.html', form=flask_form, update=update)


#Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    flask_form = RegistrationForm(request.form)

    if flask_form.validate_on_submit():
        user = User(username=flask_form.username.data, email=flask_form.email.data)
        user.set_password(flask_form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')

        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=flask_form)


#Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    flask_form = LoginForm(request.form)

    if flask_form.validate_on_submit():
        user = User.query.filter_by(username=flask_form.username.data).first()

        if user is None or not user.check_password(flask_form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=flask_form.remember_me.data)
        next_page = request.args.get('next')

        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
            return redirect(next_page)

        return redirect(url_for('index'))

    return render_template('login.html', title='Sign In', form=flask_form)


#Logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
