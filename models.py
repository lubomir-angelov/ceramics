# coding: utf-8
from sqlalchemy import Boolean, CHAR, Column, Enum, ForeignKey, Integer, LargeBinary, Numeric, String, Text, text
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
    color1 = Column(Text)
    color2 = Column(Text)
    photos = Column(LargeBinary)
    drawings = Column(LargeBinary)
    handfragments = Column(Integer)
    wheelfragment = Column(Integer)
    recordenteredby = Column(Text)
    recordenteredon = Column(String(50))
    recordcreatedby = Column(Text)
    recordcreatedon = Column(String(50))
    description = Column(Text)
    akb_num = Column(Integer)

    # based on the assumption the relationship is one-to-many
    # if one-to-one change is needed in the declaration
    # TODO: fix replationships
    #tblfragments = relationship('Tblfragment', back_populates='tbllayers')
    #tbllayerincludes = relationship('Tbllayerinclude', back_populates='tbllayers')
    #tblornaments = relationship('Tblornament', back_populates='tbllayers')
    #tblpoks = relationship('Tblpok', back_populates='tbllayers')

    # TODO: change all vars to columns needed for input
    # Note: do not include photos and drawings
    def __init__(self, layertype, layername, site, sector, square, context, layer, stratum, level,
                 structure, includes, color1, color2, handfragments, wheelfragment, recordenteredby
                 , recordcreatedby, recordcreatedon, description, akb_num):
        self.layertype = layertype
        self.layername = layername
        self.site = site
        self.sector = sector
        self.square = square
        self.context = context
        self.layer = layer
        self.stratum = stratum
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


    # TODO: change all vars to columns needed for input
    # Note: do not include photos and drawings
    def __repr__(self):
        return '<layerid {}>'.format(self.layerid)

    # TODO: change all vars to columns needed for input
    # Note: do not include photos and drawings
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


class Tblfragment(Base):
    __tablename__ = 'tblfragments'

    fragmentid = Column(Integer, primary_key=True, server_default=text("nextval('tblfragments_fragmentid_seq'::regclass)"))
    locationid = Column(ForeignKey('tbllayers.layerid'))
    fragmenttype = Column(String(50))
    technology = Column(String(50))
    speed = Column(Text)
    baking = Column(CHAR(50))
    fract = Column(String(50))
    primarycolor = Column(String(50))
    secondarycolor = Column(String(50))
    covering = Column(String(20))
    includesconc = Column(String(1))
    includessize = Column(String(1))
    includestype = Column(String(50))
    surface = Column(String(2))
    count = Column(Integer)
    onepot = Column(Boolean)
    piecetype = Column(String(10))
    wallthickness = Column(String(10))
    handlesize = Column(String(50))
    handletype = Column(String(50))
    dishsize = Column(String(1))
    topsize = Column(Numeric(5, 2))
    necksize = Column(Numeric(5, 2))
    bodysize = Column(Numeric(5, 2))
    bottomsize = Column(Numeric(5, 2))
    dishheight = Column(Numeric(5, 2))
    bottomtype = Column(String(2))
    outline = Column(String(50))
    category = Column(String(5))
    form = Column(String(5))
    type = Column(String(10))
    subtype = Column(String(50))
    variant = Column(Text)
    note = Column(Text)
    inventory = Column(Text)
    decoration = Column(Text)
    composition = Column(Text)
    parallels = Column(Text)
    image = Column(LargeBinary)
    recordenteredby = Column(Text)
    recordenteredon = Column(String(50))

    # TODO: fix replationships
    #tbllayer = relationship('Tbllayer', back_populates='tblfragments')
    #tblornaments = relationship('Tblornament', back_populates='tblfragment')

    # TODO: change all vars to columns needed for input
    # Note: do not include photos and drawings
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




    # TODO: change all vars to columns needed for input
    # Note: do not include photos and drawings
    def __repr__(self):
        return '<fragmentid {}>'.format(self.fragmentid)

    # TODO: change all vars to columns needed for input
    # Note: do not include photos and drawings
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
            'recordenteredon': self.recordenteredon,




        }


class Tbllayerinclude(Base):
    __tablename__ = 'tbllayerincludes'

    includeid = Column(Integer, primary_key=True, server_default=text("nextval('tbllayerincludes_includeid_seq'::regclass)"))
    locationid = Column(ForeignKey('tbllayers.layerid'))
    includetype = Column(Text)
    includetext = Column(Text)
    includesize = Column(Text)
    includeconc = Column(Text)

    # TODO: fix replationships
    #tbllayer = relationship('Tbllayer', back_populates='tbllayerincludes')

    # TODO: change all vars to columns needed for input
    # Note: do not include photos and drawings
    def __init__(self, includetype, includetext, includesize, includeconc):
        self.includetype = includetype
        self.includetext = includetext
        self.includesize = includesize
        self.includeconc = includeconc

    # TODO: change all vars to columns needed for input
    # Note: do not include photos and drawings
    def __repr__(self):
        return '<includeid {}>'.format(self.includeid)

    # TODO: change all vars to columns needed for input
    # Note: do not include photos and drawings
    def serialize(self):
        return {
            'includeid': self.includeid,
            'locationid': self.locationid,
            'includetype': self.includetype,
            'includetext': self.includetext,
            'includesize': self.includesize,
            'includeconc': self.includeconc
        }


class Tblpok(Base):
    __tablename__ = 'tblpok'

    pokid = Column(Integer, primary_key=True, server_default=text("nextval('tblpok_pokid_seq'::regclass)"))
    locationid = Column(ForeignKey('tbllayers.layerid'))
    type = Column(Text)
    quantity = Column(Integer)
    weight = Column(Numeric(6, 3))

    # TODO: fix replationships
    #tbllayer = relationship('Tbllayer', back_populates='tblpoks')

    # TODO: change all vars to columns needed for input
    # Note: do not include photos and drawings
    def __init__(self, type, quantity, weight):
        self.type = type
        self.quantity = quantity
        self.weight = weight

    # TODO: change all vars to columns needed for input
    # Note: do not include photos and drawings
    def __repr__(self):
        return '<pokid {}>'.format(self.pokid)

    # TODO: change all vars to columns needed for input
    # Note: do not include photos and drawings
    def serialize(self):
        return {
            'pokid': self.pokid,
            'locationid': self.locationid,
            'type': self.type,
            'quantity': self.quantity,
            'weight': self.weight
        }


class Tblornament(Base):
    __tablename__ = 'tblornaments'

    ornamentid = Column(Integer, primary_key=True, server_default=text("nextval('tblornaments_ornamentid_seq'::regclass)"))
    fragmentid = Column(ForeignKey('tblfragments.fragmentid'))
    location = Column(Text)
    relationship = Column(Text)
    onornament = Column(Integer)
    color1 = Column(String(10))
    color2 = Column(String(10))
    encrustcolor1 = Column(String(10))
    encrustcolor2 = Column(String(10))
    primary_ = Column(String(10))
    secondary = Column(String(10))
    tertiary = Column(String(10))
    quarternary = Column(String(10))

    # TODO: fix replationships
    #tblfragment = relationship('Tblfragment', back_populates='tblfragments')

    # TODO: change all vars to columns needed for input
    # Note: do not include photos and drawings
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

    # TODO: change all vars to columns needed for input
    # Note: do not include photos and drawings
    def __repr__(self):
        return '<ornamentid {}>'.format(self.ornamentid)

    # TODO: change all vars to columns needed for input
    # Note: do not include photos and drawings
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
