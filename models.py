


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


class Tblpok(Base):
    __tablename__ = 'tblpok'

    pokid = Column(Integer, primary_key=True, server_default=text("nextval('tblpok_pokid_seq'::regclass)"))
    locationid = Column(ForeignKey('tbllayers.layerid'))
    type = Column(Text)
    quantity = Column(Integer)
    weight = Column(Numeric(6, 3))

    # TODO: fix replationships
    #tbllayer = relationship('Tbllayer', back_populates='tblpoks')


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
