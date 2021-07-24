# coding: utf-8
from sqlalchemy import Boolean, Column, Date, Enum, ForeignKey, Integer, LargeBinary, Numeric, String, Table, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Tbllayer(Base):
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


class Tblfragment(Base):
    __tablename__ = 'tblfragments'

    fragmentid = Column(Integer, primary_key=True, server_default=text("nextval('tblfragments_fragmentid_seq'::regclass)"))
    locationid = Column(ForeignKey('tbllayers.layerid'))
    fragmenttype = Column(Enum('1', '2', name='fragment_type'))
    technology = Column(Enum('1', '2', '2А', '2Б', name='technology_'))
    speed = Column(Enum('1', '2', name='speed_type'))
    baking = Column(Enum('Р', 'Н', name='baking_type'))
    fract = Column(Enum('1', '2', '3', name='fract_type'))
    primarycolor = Column(Enum('бял', 'жълт', 'охра', 'червен', 'сив', 'тъмносив', 'кафяв', 'светлокафяв', 'тъмнокафяв', 'черен', name='primarycolor_type'))
    secondarycolor = Column(Enum('бял', 'жълт', 'охра', 'червен', 'сив', 'тъмносив', 'кафяв', 'светлокафяв', 'тъмнокафяв', 'черен', name='secondarycolor_type'))
    covering = Column(String(20))
    includesconc = Column(Enum('+', '-', name='includesconc_type'))
    includessize = Column(Enum('М', 'С', 'Г', name='includessize_type'))
    includestype = Column(Enum('с', 'т', name='includestype_type'))
    surface = Column(Enum('А', 'Б', 'В', 'В1', 'В2', 'Г', name='surface_type'))
    count = Column(Integer, nullable=False)
    onepot = Column(Boolean)
    piecetype = Column(Enum('устие', 'стена', 'дръжка', 'дъно', 'профил', 'чучур', 'дъно+дръжка', 'профил+дръжка', 'устие+дръжка', 'стена+дръжка', 'псевдочучур', 'плавен прелом', 'биконичност', 'двоен съд', 'цял съд', name='piecetype_type'), nullable=False)
    wallthickness = Column(Enum('М', 'С', 'Г', name='wallthickness_type'))
    handlesize = Column(String(50))
    handletype = Column(String(5))
    dishsize = Column(Enum('М', 'С', 'Г', name='dishsize_type'))
    topsize = Column(Numeric(5, 2))
    necksize = Column(Numeric(5, 2))
    bodysize = Column(Numeric(5, 2))
    bottomsize = Column(Numeric(5, 2))
    dishheight = Column(Numeric(5, 2))
    bottomtype = Column(Enum('А', 'Б', 'В', 'А1', 'А2', 'Б1', 'Б2', 'В1', 'В2', name='bottomtype_type'))
    outline = Column(Enum('1', '2', '3', name='outline_type'))
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


class Tbllayerinclude(Base):
    __tablename__ = 'tbllayerincludes'

    includeid = Column(Integer, primary_key=True, server_default=text("nextval('tbllayerincludes_includeid_seq'::regclass)"))
    locationid = Column(ForeignKey('tbllayers.layerid'))
    includetype = Column(Enum('антропогенен', 'естествен', name='includetype_type'))
    includetext = Column(Text)
    includesize = Column(Enum('малки', 'средни', 'големи', name='includesize_type'))
    includeconc = Column(Text)

    tbllayer = relationship('Tbllayer')


class Tblpok(Base):
    __tablename__ = 'tblpok'

    pokid = Column(Integer, primary_key=True, server_default=text("nextval('tblpok_pokid_seq'::regclass)"))
    locationid = Column(ForeignKey('tbllayers.layerid'))
    type = Column(Text)
    quantity = Column(Integer)
    weight = Column(Numeric(6, 3))

    tbllayer = relationship('Tbllayer')


class Tblornament(Base):
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

    tblfragment = relationship('Tblfragment')
