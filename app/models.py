# coding: utf-8
import datetime
import pydoc_data

from sqlalchemy import Boolean, CHAR, Column, Enum, ForeignKey, Integer, LargeBinary, Numeric, String, Text, text, Date
from sqlalchemy.orm import relationship
from sqlalchemy.orm import validates
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash




from app import db
from app import login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

Base = declarative_base()
metadata = Base.metadata


class Tbllayer(db.Model):
    __tablename__ = 'tbllayers'

    layerid = Column(Integer, primary_key=True, server_default=text("nextval('tbllayers_layerid_seq'::regclass)"))
    layertype = Column(db.Enum('механичен', 'контекст', '', name='layer_type_'))
    layername = Column(Text)
    @validates('layername')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value

    site = Column(Text)
    @validates('site')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value

    sector = Column(Text)
    @validates('sector')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value

    square = Column(Text)
    @validates('square')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value

    context = Column(Text)
    @validates('context')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value

    layer = Column(Text)
    @validates('layer')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value

    stratum = Column(Text)
    @validates('stratum')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value
    parentid = Column(Integer)

    level = Column(Text)
    @validates('level')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value

    structure = Column(Text)
    @validates('structure')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value

    includes = Column(Text)
    @validates('includes')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value

    color1 = Column(db.Enum('бял', 'жълт', 'охра', 'червен', 'сив', 'тъмносив', 'кафяв', 'светлокафяв', 'тъмнокафяв', 'черен', '', name='color1_type_'))
    color2 = Column(db.Enum('бял', 'жълт', 'охра', 'червен', 'сив', 'тъмносив', 'кафяв', 'светлокафяв', 'тъмнокафяв', 'черен', '', name='color2_type_'))

    photos = Column(LargeBinary)
    @validates('photos')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value

    drawings = Column(LargeBinary)
    @validates('drawings')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value

    handfragments = Column(Integer)
    @validates('handfragments')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value

    wheelfragment = Column(Integer)
    @validates('wheelfragment')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value

    recordenteredby = Column(Text)
    @validates('recordenteredby')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value

    recordenteredon = Column(Date, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    recordcreatedby = Column(Text)
    @validates('recordcreatedby')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value

    recordcreatedon = Column(Date, nullable=False)
    description = Column(Text)
    @validates('description')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value

    akb_num = Column(Integer)
    @validates('akb_num')
    def empty_string_to_null(self, key, value):
        if isinstance(value,str) and value == '':
            return None
        else:
            return value
    #
    #fragments = db.relationship('Tblfragment', backref='layers')

    # TODO: fix relationships
    #tblfragments = relationship('Tblfragment', back_populates='tbllayers')
    #tbllayerincludes = relationship('Tbllayerinclude', back_populates='tbllayers')
    #tblornaments = relationship('Tblornament', back_populates='tbllayers')
    #tblpoks = relationship('Tblpok', back_populates='tbllayers')


    def __init__(self, site, sector, square, context, layer, stratum, level,
                 structure, includes, color1, color2, recordenteredby,
                 recordcreatedby, recordcreatedon, description, akb_num):
        self.site = site
        self.sector = sector
        self.square = square
        self.context = context
        self.layer = layer
        self.stratum = stratum
        self.level = level
        self.structure = structure
        self.includes = includes
        self.color1 = color1
        self.color2 = color2
        self.recordenteredby = recordenteredby
        self.recordcreatedby = recordcreatedby
        self.recordcreatedon = recordcreatedon
        self.description = description
        self.akb_num = akb_num

    def __repr__(self):
        return '<layerid {}>'.format(self.layerid)

    def serialize(self):
        return {
            'layerid': self.id,
            'layertype': self.layertype,
            'layername': self.layername,
            'site': self.site,
            'sector': self.sector,
            'square': self.square,
            'context': self.context,
            'layer': self.layer,
            'stratum': self.stratum,
            'level': self.level,
            'parentid': self.parentid,
            'structure': self.structure,
            'includes': self.includes,
            'color1': self.color1,
            'color2': self.color2,
            'handfragments': self.handfragments,
            'wheelfragment': self.wheelfragment,
            'recordenteredby': self.recordenteredby,
            'recordenteredon': self.recordenteredon,
            'recordcreatedby': self.recordcreatedby,
            'recordcreatedon': self.recordcreatedon,
            'description': self.description,
            'akb_num': self.akb_num,
        }


class Tblfragment(db.Model):
    __tablename__ = 'tblfragments'

    fragmentid = Column(Integer, primary_key=True, server_default=text("nextval('tblfragments_fragmentid_seq'::regclass)"))
    locationid = Column(Integer, ForeignKey('tbllayers.layerid'))
    fragmenttype = Column(db.Enum('1', '2', '', name='fragmenttype_type'))

    @validates('fragmenttype')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value
    technology = Column(db.Enum('1', '2', '2А', '2Б', '', name='technology_type'))
    #speed = Column(db.Enum('1', '2', '', name='speed_type_'))
    baking = Column(db.Enum('Р', 'Н', '', name='baking_type_'))
    fract = Column(db.Enum('1', '2', '3', '', name='fract_type_'))
    primarycolor = Column(db.Enum('бял', 'жълт', 'охра', 'червен', 'сив', 'тъмносив', 'кафяв', 'светлокафяв', 'тъмнокафяв', 'черен', '', name='primarycolor_type_'))
    secondarycolor = Column(db.Enum('бял', 'жълт', 'охра', 'червен', 'сив', 'тъмносив', 'кафяв', 'светлокафяв', 'тъмнокафяв', 'черен', '', name='secondarycolor_type_'))
    covering = Column(db.Enum('да', 'не', 'Ф1', 'Ф2', '', 'Б', 'Г', name='covering'))
    includesconc = Column(db.Enum('+', '-', '', name='includesconc_type_'))
    includessize = Column(db.Enum('М', 'С', 'Г', '', name='includessize_type_'))
    #includestype = Column(db.Enum('с', 'т', '', name='includestype_type_'))
    surface = Column(db.Enum('А', 'Б', 'В', 'В1', 'В2', 'Г', '', name='surface_type_'))
    count = Column(Integer, nullable=False)
    onepot = Column(db.Enum('да', 'не', '', name='onepot_type'))
    piecetype = Column(db.Enum('устие', 'стена', 'дръжка', 'дъно', 'профил', 'чучур', 'дъно+дръжка', 'профил+дръжка', 'устие+дръжка', 'стена+дръжка', 'псевдочучур', 'плавен прелом', 'биконичност', 'двоен съд', 'цял съд', name='piecetype_type'), nullable=False)
    wallthickness = Column(db.Enum('М', 'С', 'Г', '',  name='wallthickness_type_'))
    handlesize = Column(db.Enum('М', 'С', 'Г', '', name='handlesize_type'))
    handletype = Column(String(5))

    @validates('handletype')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value
    dishsize = Column(db.Enum('М', 'С', 'Г', '', name='dishsize_type_'))
    #topsize = Column(Numeric(5, 2))

    #@validates('topsize')
    #def empty_string_to_null(self, key, value):
        #if isinstance(value, str) and value == '':
            #return None
        #else:
            #return value
    #necksize = Column(Numeric(5, 2))

    #@validates('necksize')
    #def empty_string_to_null(self, key, value):
        #if isinstance(value, str) and value == '':
            #return None
        #else:
            #return value
    #bodysize = Column(Numeric(5, 2))

    #@validates('bodysize')
    #def empty_string_to_null(self, key, value):
        #if isinstance(value, str) and value == '':
            #return None
        #else:
            #return value
    #bottomsize = Column(Numeric(5, 2))

    #@validates('bottomsize')
    #def empty_string_to_null(self, key, value):
        #if isinstance(value, str) and value == '':
            #return None
        #else:
            #return value
    #dishheight = Column(Numeric(5, 2))

    #@validates('dishheight')
    #def empty_string_to_null(self, key, value):
        #if isinstance(value, str) and value == '':
            #return None
        #else:
            #return value
    bottomtype = Column(db.Enum('А', 'Б', 'В', 'А1', 'А2', 'Б1', 'Б2', 'В1', 'В2', '',  name='bottomtype_type_'))
    outline = Column(db.Enum('1', '2', '3', '',  name='outline_typee'))
    category = Column(String(5))

    @validates('category')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value
    form = Column(String(5))

    @validates('form')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value
    type = Column(Integer)

    @validates('type')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value
    subtype = Column(String(1))

    @validates('subtype')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value
    variant = Column(Integer)

    @validates('variant')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value
    note = Column(Text)

    @validates('note')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value
    inventory = Column(Text)

    @validates('inventory')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value
    #decoration = Column(Text)

    #@validates('decoration')
    #def empty_string_to_null(self, key, value):
        #if isinstance(value, str) and value == '':
            #return None
        #else:
            #return value
    #composition = Column(Text)

    #@validates('composition')
    #def empty_string_to_null(self, key, value):
        #if isinstance(value, str) and value == '':
            #return None
        #else:
            #return value
    #parallels = Column(Text)

    #@validates('parallels')
    #def empty_string_to_null(self, key, value):
        #if isinstance(value, str) and value == '':
            #return None
        #else:
            #return value
    #image = Column(LargeBinary)

    #@validates('image')
    #def empty_string_to_null(self, key, value):
        #if isinstance(value, str) and value == '':
            #return None
        #else:
            #return value
    recordenteredby = Column(Text)

    @validates('recordenteredby')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value
    recordenteredon = Column(String(50), server_default=text("CURRENT_TIMESTAMP"))


    #layerid = db.Column(db.Integer, db.ForeignKey('locationid'))
    #tbllayer = relationship('Tbllayer')
    # TODO: fix replationships
    #tbllayer = relationship('Tbllayer', back_populates='tblfragments')
    #tblornaments = relationship('Tblornament', back_populates='tblfragment')

    def __init__(self, locationid, technology, baking, fract, primarycolor, secondarycolor, covering, includesconc, includessize
                 , surface, count, onepot, piecetype, wallthickness, handletype, dishsize,
                    bottomtype, outline, category, form, type, subtype, variant,
                 note, inventory, recordenteredby):
        self.locationid = locationid
        self.technology = technology
        self.baking = baking
        self.fract = fract
        self.primarycolor = primarycolor
        self.secondarycolor = secondarycolor
        self.covering = covering
        self.includesconc = includesconc
        self.includessize = includessize
        #self.includestype = includestype
        self.surface = surface
        self.count = count
        self.onepot = onepot
        self.piecetype = piecetype
        self.wallthickness = wallthickness
        #self.handlesize = handlesize
        self.handletype = handletype
        self.dishsize = dishsize
        #self.topsize = topsize
        #self.necksize = necksize
        #self.bodysize = bodysize
        #self.bottomsize = bottomsize
        #self.dishheight = dishheight
        self.bottomtype = bottomtype
        self.outline = outline
        self.category = category
        self.form = form
        self.type = type
        self.subtype = subtype
        self.variant = variant
        self.note = note
        self.inventory = inventory
        #self.decoration = decoration
        #self.composition = composition
        #self.parallels = parallels
        self.recordenteredby = recordenteredby

        # some comment

    def __repr__(self):
        return '<fragmentid {}>'.format(self.fragmentid)

    def serialize(self):
        return {
            'fragmentid': self.fragmentid,
            'locationid': self.locationid,
            'fragmenttype': self.fragmenttype,
            'technology': self.technology,
            'speed': self.speed,
            'baking': self.baking,
            'fract': self.fract,
            'primarycolor': self.primarycolor,
            'secondarycolor': self.secondarycolor,
            'covering': self.covering,
            'includesconc': self.includesconc,
            'includessize': self.includessize,
            'includestype': self.includestype,
            'surface': self.surface,
            'count': self.count,
            'onepot': self.onepot,
            'piecetype': self.piecetype,
            'wallthickness': self.wallthickness,
            'handlesize': self.handlesize,
            'handletype': self.handletype,
            'dishsize': self.dishsize,
            'topsize': self.topsize,
            'necksize': self.necksize,
            'bodysize': self.bodysize,
            'bottomsize': self.bottomsize,
            'dishheight': self.dishheight,
            'bottomtype': self.bottomtype,
            'outline': self.outline,
            'category': self.category,
            'form': self.form,
            'type': self.type,
            'subtype': self.subtype,
            'variant': self.variant,
            'note': self.note,
            'inventory': self.inventory,
            'decoration': self.decoration,
            'composition': self.composition,
            'parallels': self.parallels,
            'recordenteredby': self.recordenteredby,
            'recordenteredon': self.recordenteredon
        }


class Tbllayerinclude(db.Model):
    __tablename__ = 'tbllayerincludes'

    includeid = Column(Integer, primary_key=True, server_default=text("nextval('tbllayerincludes_includeid_seq'::regclass)"))
    locationid = Column(ForeignKey('tbllayers.layerid'))
    includetype = Column(db.Enum('антропогенен', 'естествен', '', name='includetype_type'))
    includetext = Column(Text)

    @validates('includetext')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value
    includesize = Column(db.Enum('малки', 'средни', 'големи', '', name='includesize_type'))
    includeconc = Column(db.Enum('ниска', 'средна', 'висока', '', name='includeconc_type'))
    recordenteredon = Column(Date, nullable=False, server_default=text("CURRENT_TIMESTAMP"))


    #tbllayer = relationship('Tbllayer')
    # TODO: fix replationships
    #tbllayer = relationship('Tbllayer', back_populates='tbllayerincludes')

    def __init__(self, locationid, includetype, includetext, includesize, includeconc):
        self.locationid = locationid
        self.includetype = includetype
        self.includetext = includetext
        self.includesize = includesize
        self.includeconc = includeconc

    def __repr__(self):
        return '<includeid {}>'.format(self.includeid)

    def serialize(self):
        return {
            'includeid': self.includeid,
            'locationid': self.locationid,
            'includetype': self.includetype,
            'includetext': self.includetext,
            'includesize': self.includesize,
            'includeconc': self.includeconc,
            'recordenteredon': self.recordenteredon
        }

class Tblpok(db.Model):
    __tablename__ = 'tblpok'

    pokid = Column(Integer, primary_key=True, server_default=text("nextval('tblpok_pokid_seq'::regclass)"))
    locationid = Column(ForeignKey('tbllayers.layerid'))
    type = Column(Text)
    @validates('type')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value

    quantity = Column(Integer)
    @validates('quantity')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value

    weight = Column(Numeric(6, 3))
    @validates('weight')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value

    sok_weight = Column(Numeric(6, 3))
    @validates('sok_weight')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value

    recordenteredon = Column(Date, nullable=False, server_default=text("CURRENT_TIMESTAMP"))

    #tbllayer = relationship('Tbllayer')
    # TODO: fix replationships
    #tbllayer = relationship('Tbllayer', back_populates='tblpoks')

    def __init__(self, locationid, type, quantity, weight, sok_weight):
        self.locationid = locationid
        self.type = type
        self.quantity = quantity
        self.weight = weight
        self.sok_weight = sok_weight
        # to add new column sok weight!

    def __repr__(self):
        return '<pokid {}>'.format(self.pokid)

    def serialize(self):
        return {
            'pokid': self.pokid,
            'locationid': self.locationid,
            'type': self.type,
            'quantity': self.quantity,
            'weight': self.weight,
            'sok_weight': self.sok_weight,
            'recordenteredon': self.recordenteredon
        }


class Tblornament(db.Model):
    __tablename__ = 'tblornaments'

    ornamentid = Column(Integer, primary_key=True, server_default=text("nextval('tblornaments_ornamentid_seq'::regclass)"))
    fragmentid = Column(ForeignKey('tblfragments.fragmentid'))
    location = Column(Text)

    @validates('location')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value
    relationship = Column(Text)

    @validates('relationship')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value
    onornament = Column(Integer)

    @validates('onornament')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value
    #color1 = Column(db.Enum('бял', 'жълт', 'охра', 'червен', 'сив', 'тъмносив', 'кафяв', 'светлокафяв', 'тъмнокафяв', 'черен', '', name='color1_type'))
    #color2 = Column(db.Enum('бял', 'жълт', 'охра', 'червен', 'сив', 'тъмносив', 'кафяв', 'светлокафяв', 'тъмнокафяв', 'черен', '', name='color2_type'))
    encrustcolor1 = Column(String(10))

    @validates('encrustcolor1')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value
    encrustcolor2 = Column(String(10))

    @validates('encrustcolor2')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value
    # ADD NEW FORMS
    primary_ = Column(db.Enum('А', 'В', 'Д', 'И', 'К', 'Н', 'П', 'Р', 'Ф', 'Ц', 'Щ', '', name='primary_type_'))
    secondary = Column(db.Enum('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI',
                               'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', ''))
    tertiary = Column(db.Enum('А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К', 'Л', 'М', 'П', 'А1', 'А2', 'Б1', 'Б2', '', name='tertiary_type_'))
    quarternary = Column(Integer)
    recordenteredon = Column(Date, nullable=False, server_default=text("CURRENT_TIMESTAMP"))

    #tbllayer = relationship('Tblfragment')
    # TODO: fix replationships
    #tblfragment = relationship('Tblfragment', back_populates='tblfragments')

    def __init__(self, fragmentid, location, encrustcolor1,
                 encrustcolor2, primary_, secondary, tertiary, quarternary):
        self.fragmentid = fragmentid
        self.location = location

        # TO REMOVE self.relationship = relationship
        # TO REMOVE self.onornament = onornament

        #self.color1 = color1
        #self.color2 = color2
        self.encrustcolor1 = encrustcolor1
        self.encrustcolor2 = encrustcolor2
        self.primary_ = primary_
        self.secondary = secondary
        self.tertiary = tertiary
        self.quarternary = quarternary

    def __repr__(self):
        return '<ornamentid {}>'.format(self.ornamentid)

    def serialize(self):
        return {
            'ornamentid': self.ornamentid,
            'fragmentid': self.fragmentid,
            'location': self.location,
            #'color1': self.color1,
            #'color2': self.color2,
            'encrustcolor1': self.encrustcolor1,
            'encrustcolor2': self.encrustcolor2,
            'primary_': self.primary_,
            'secondary': self.secondary,
            'tertiary': self.tertiary,
            'quarternary': self.quarternary,
            'recordenteredon': self.recordenteredon

        }

class User(UserMixin, db.Model):
    __tablename__ = 'tblregistered'
    id = Column(Integer, primary_key=True, server_default=text("nextval('tblregistered_id_seq'::regclass)"))
    username = Column(String(25))
    email = Column(String)
    password_hash = Column(db.String)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
