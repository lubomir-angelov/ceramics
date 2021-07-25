# coding: utf-8
from sqlalchemy import Boolean, CHAR, Column, Enum, ForeignKey, Integer, LargeBinary, Numeric, String, Text, text, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from app import db

Base = declarative_base()
metadata = Base.metadata


class Tbllayer(db.Model):
    __tablename__ = 'tbllayers'

    layerid = Column(Integer, primary_key=True, server_default=text("nextval('tbllayers_layerid_seq'::regclass)"))
    layertype = Column(Enum('механичен', 'контекст', name='layer_type'))
    layername = Column(Text)
    site = Column(Text)
    sector = Column(Text)
    square = Column(Text)
    context = Column(Text)
    layer = Column(Text)
    stratum = Column(Text)
    parentid = Column(Integer)
    level = Column(Text)
    structure = Column(Text)
    includes = Column(Text)
    color1 = Column(Enum('бял', 'жълт', 'охра', 'червен', 'сив', 'тъмносив', 'кафяв', 'светлокафяв', 'тъмнокафяв', 'черен', name='color1_type'))
    color2 = Column(Enum('бял', 'жълт', 'охра', 'червен', 'сив', 'тъмносив', 'кафяв', 'светлокафяв', 'тъмнокафяв', 'черен', name='color2_type'))
    photos = Column(LargeBinary)
    drawings = Column(LargeBinary)
    handfragments = Column(Integer)
    wheelfragment = Column(Integer)
    recordenteredby = Column(Text)
    recordenteredon = Column(Date, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    recordcreatedby = Column(Text)
    recordcreatedon = Column(Date)
    description = Column(Text)
    akb_num = Column(Integer)

    # TODO: fix replationships
    #tblfragments = relationship('Tblfragment', back_populates='tbllayers')
    #tbllayerincludes = relationship('Tbllayerinclude', back_populates='tbllayers')
    #tblornaments = relationship('Tblornament', back_populates='tbllayers')
    #tblpoks = relationship('Tblpok', back_populates='tbllayers')

    def __init__(self, layertype, layername, site, sector, square, context, layer, stratum, level,
                 structure, includes, color1, color2, handfragments, wheelfragment, recordenteredby,
                 recordcreatedby, recordcreatedon, description, akb_num):
        self.layertype = layertype
        self.layername = layername
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
        self.handfragments = handfragments
        self.wheelfragment = wheelfragment
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
    locationid = Column(ForeignKey('tbllayers.layerid'))
    fragmenttype = Column(Enum('1', '2', '', name='fragmenttype_type'))
    technology = Column(Enum('1', '2', '2А', '2Б', '', name='technology_type'))
    speed = Column(Enum('1', '2', '', name='speed_type_'))
    baking = Column(Enum('Р', 'Н', '', name='baking_type_'))
    fract = Column(Enum('1', '2', '3', '', name='fract_type_'))
    primarycolor = Column(Enum('бял', 'жълт', 'охра', 'червен', 'сив', 'тъмносив', 'кафяв', 'светлокафяв', 'тъмнокафяв', 'черен', '', name='primarycolor_type_'))
    secondarycolor = Column(Enum('бял', 'жълт', 'охра', 'червен', 'сив', 'тъмносив', 'кафяв', 'светлокафяв', 'тъмнокафяв', 'черен', '', name='secondarycolor_type_'))
    covering = Column(Enum('да', 'не', 'Ф1', 'Ф2', '', name='covering_type_'))
    includesconc = Column(Enum('+', '-', '', name='includesconc_type_'))
    includessize = Column(Enum('М', 'С', 'Г', '', name='includessize_type_'))
    includestype = Column(Enum('с', 'т', '', name='includestype_type_'))
    surface = Column(Enum('А', 'Б', 'В', 'В1', 'В2', 'Г', '', name='surface_type_'))
    count = Column(Integer, nullable=False)
    onepot = Column(Enum('да', 'не', '', name='onepot_type'))
    piecetype = Column(Enum('устие', 'стена', 'дръжка', 'дъно', 'профил', 'чучур', 'дъно+дръжка', 'профил+дръжка', 'устие+дръжка', 'стена+дръжка', 'псевдочучур', 'плавен прелом', 'биконичност', 'двоен съд', 'цял съд', name='piecetype_type'), nullable=False)
    wallthickness = Column(Enum('М', 'С', 'Г', '',  name='wallthickness_type_'))
    handlesize = Column(Enum('М', 'С', 'Г', '', name='handlesize_type'))
    handletype = Column(String(5))
    dishsize = Column(Enum('М', 'С', 'Г', '', name='dishsize_type_'))
    topsize = Column(Numeric(5, 2))
    necksize = Column(Numeric(5, 2))
    bodysize = Column(Numeric(5, 2))
    bottomsize = Column(Numeric(5, 2))
    dishheight = Column(Numeric(5, 2))
    bottomtype = Column(Enum('А', 'Б', 'В', 'А1', 'А2', 'Б1', 'Б2', 'В1', 'В2', '',  name='bottomtype_type_'))
    outline = Column(Enum('1', '2', '3', '', name='outline_typee'))
    category = Column(String(5))
    form = Column(String(5))
    type = Column(Integer)
    subtype = Column(String(1))
    variant = Column(Integer)
    note = Column(Text)
    inventory = Column(Text)
    decoration = Column(Text)
    composition = Column(Text)
    parallels = Column(Text)
    image = Column(LargeBinary)
    recordenteredby = Column(Text)
    recordenteredon = Column(String(50), server_default=text("CURRENT_TIMESTAMP"))

    tbllayer = relationship('Tbllayer')
    # TODO: fix replationships
    #tbllayer = relationship('Tbllayer', back_populates='tblfragments')
    #tblornaments = relationship('Tblornament', back_populates='tblfragment')

    def __init__(self, technology, speed, baking, fract, primarycolor, secondarycolor, covering, includesconc, includessize,
                 includestype, surface, count, onepot, piecetype, wallthickness, handlesize, handletype, dishsize, topsize,
                 necksize, bodysize, bottomsize, dishheight, bottomtype, outline, category, form, type, subtype, variant,
                 note, inventory, decoration, composition, parallels, recordenteredby):
        self.technology = technology
        self.speed = speed
        self.baking = baking
        self.fract = fract
        self.primarycolor = primarycolor
        self.secondarycolor = secondarycolor
        self.covering = covering
        self.includesconc = includesconc
        self.includessize = includessize
        self.includestype = includestype
        self.surface = surface
        self.count = count
        self.onepot = onepot
        self.piecetype = piecetype
        self.wallthickness = wallthickness
        self.handlesize = handlesize
        self.handletype = handletype
        self.dishsize = dishsize
        self.topsize = topsize
        self.necksize = necksize
        self.bodysize = bodysize
        self.bottomsize = bottomsize
        self.dishheight = dishheight
        self.bottomtype = bottomtype
        self.outline = outline
        self.category = category
        self.form = form
        self.type = type
        self.subtype = subtype
        self.variant = variant
        self.note = note
        self.inventory = inventory
        self.decoration = decoration
        self.composition = composition
        self.parallels = parallels
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
    includetype = Column(Enum('антропогенен', 'естествен', name='includetype_type'))
    includetext = Column(Text)
    includesize = Column(Enum('малки', 'средни', 'големи', name='includesize_type'))
    includeconc = Column(Text)

    tbllayer = relationship('Tbllayer')
    # TODO: fix replationships
    #tbllayer = relationship('Tbllayer', back_populates='tbllayerincludes')

    def __init__(self, includetype, includetext, includesize, includeconc):
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
            'includeconc': self.includeconc
        }

class Tblpok(db.Model):
    __tablename__ = 'tblpok'

    pokid = Column(Integer, primary_key=True, server_default=text("nextval('tblpok_pokid_seq'::regclass)"))
    locationid = Column(ForeignKey('tbllayers.layerid'))
    type = Column(Text)
    quantity = Column(Integer)
    weight = Column(Numeric(6, 3))

    tbllayer = relationship('Tbllayer')
    # TODO: fix replationships
    #tbllayer = relationship('Tbllayer', back_populates='tblpoks')

    def __init__(self, type, quantity, weight):
        self.type = type
        self.quantity = quantity
        self.weight = weight

    def __repr__(self):
        return '<pokid {}>'.format(self.pokid)

    def serialize(self):
        return {
            'pokid': self.pokid,
            'locationid': self.locationid,
            'type': self.type,
            'quantity': self.quantity,
            'weight': self.weight
        }


class Tblornament(db.Model):
    __tablename__ = 'tblornaments'

    ornamentid = Column(Integer, primary_key=True, server_default=text("nextval('tblornaments_ornamentid_seq'::regclass)"))
    fragmentid = Column(ForeignKey('tblfragments.fragmentid'))
    location = Column(Text)
    relationship = Column(Text)
    onornament = Column(Integer)
    color1 = Column(Enum('бял', 'жълт', 'охра', 'червен', 'сив', 'тъмносив', 'кафяв', 'светлокафяв', 'тъмнокафяв', 'черен', name='color1_type'))
    color2 = Column(Enum('бял', 'жълт', 'охра', 'червен', 'сив', 'тъмносив', 'кафяв', 'светлокафяв', 'тъмнокафяв', 'черен', name='color2_type'))
    encrustcolor1 = Column(String(10))
    encrustcolor2 = Column(String(10))
    primary_ = Column(String(1))
    secondary = Column(String(5))
    tertiary = Column(String(1))
    quarternary = Column(String(10))

    #tbllayer = relationship('Tblfragment')
    # TODO: fix replationships
    #tblfragment = relationship('Tblfragment', back_populates='tblfragments')

    def __init__(self, location, relationship, onornament, color1, color2, encrustcolor1, encrustcolor2, primary_, secondary,
                 tertiary, quarternary):
        self.location = location
        self.relationship = relationship
        self.onornament = onornament
        self.color1 = color1
        self.color2 = color2
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
            'relationship': self.relationship,
            'onornament': self.onornament,
            'color1': self.color1,
            'color2': self.color2,
            'encrustcolor1': self.encrustcolor1,
            'encrustcolor2': self.encrustcolor2,
            'primary_': self.primary_,
            'secondary': self.secondary,
            'tertiary': self.tertiary,
            'quarternary': self.quarternary,
        }
