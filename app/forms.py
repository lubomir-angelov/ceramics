from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from enum import Enum
from markupsafe import escape
from app.models import User

from app.models import Tblpok, Tbllayer, Tbllayerinclude, Tblornament, Tblfragment


# helper for choices
# does not work https://stackoverflow.com/questions/43160780/python-flask-wtform-selectfield-with-enum-values-not-a-valid-choice-upon-valid
# first answer does not work: https://stackoverflow.com/questions/44078845/using-wtforms-with-enum/49376245
# used answer 3 from Constantinos
class FormEnum(Enum):
    @classmethod
    def choices(cls):
        return [(choice, choice.name) for choice in cls]

    @classmethod
    def coerce(cls, item):
        return cls(int(item)) if not isinstance(item, cls) else item

    def __str__(self):
        return str(self.value)


# color1 and color2 enum
class Color(FormEnum):
    WHITE = 'бял'
    YELLOW = 'жълт'
    OCHER = 'охра'
    RED = 'червен'
    GRAY = 'сив'
    DARK_GRAY = 'тъмносив'
    BROWN = 'кафяв'
    PALE_BROWN = 'светлокафяв'
    DARK_BROWN = 'тъмнокафяв'
    BLACK = 'черен'
    NONE = ''

class Color2(FormEnum):
    NONE = ''
    WHITE = 'бял'
    YELLOW = 'жълт'
    OCHER = 'охра'
    RED = 'червен'
    GRAY = 'сив'
    DARK_GRAY = 'тъмносив'
    BROWN = 'кафяв'
    PALE_BROWN = 'светлокафяв'
    DARK_BROWN = 'тъмнокафяв'
    BLACK = 'черен'


class Technology(Enum):
    ONE = '1'
    TWO = '2'
    TWO_A = '2А'
    TWO_B = '2Б'
    NO_TECHNOLOGY = ''

    def __str__(self):
        return self.name  # value string

    def __html__(self):
        return self.value  # label string


class Baking(FormEnum):
    EVEN = 'Р'
    UNEVEN = 'Н'
    NO_BAKING = ''


class Fracture(FormEnum):
    MONOLAYER = '1'
    TWO_LAYER = '2'
    THREE_LAYER = '3'
    NO_LAYER = ''

class Outline(FormEnum):
    NO_LAYER = ''
    MONOLAYER = '1'
    TWO_LAYER = '2'
    THREE_LAYER = '3'


class Covering(FormEnum):
    YES = 'да'
    NO = 'не'
    BLACK_FIRNIS = 'Ф1'
    BROWN_FIRNIS = 'Ф2'
    COV_B = 'Б'
    COV_G = 'Г'
    NO_COVERING = ''

class IncludesConcentration(FormEnum):
    HIGH = '+'
    LOW = '-'
    NO_INCLUDES = ''


class SizeShort(FormEnum):
    MEDIUM = 'С'
    SMALL = 'М'
    LARGE = 'Г'
    NONE = ''


class SizeShort2(FormEnum):
    SMALL = 'М'
    MEDIUM = 'С'
    LARGE = 'Г'
    NONE = ''


class SizeLong(FormEnum):
    NONE = ''
    SMALL = 'малки'
    MEDIUM = 'средни'
    LARGE = 'големи'


class IncludesType(FormEnum):
    MICA = 'с'
    TALC = 'т'
    NO_TYPE = ''


class Surface(FormEnum):
    POLISHED = 'А'
    POLISHED_WITHOUT_SHINE = 'Б'
    ROUGH = 'В'
    EVEN_POOR_POLISHED = 'В1'
    EVEN_UNPOLISHED = 'В2'
    UNEVEN = 'Г'
    NO_SURFACE = ''


class OneDish(FormEnum):
    NO = 'не'
    YES = 'да'

class PieceType(FormEnum):
    RIM = 'устие'
    WALL = 'стена'
    HANDLE = 'дръжка'
    BOTTOM = 'дъно'
    PROFILE = 'профил'
    SPOUT = 'чучур'
    BOTTOM_WITH_HANDLE = 'дъно+дръжка'
    PROFILE_WITH_HANDLE = 'профил+дръжка'
    RIM_WITH_HANDLE = 'устие+дръжка'
    WALL_WITH_HANDLE = 'стена+дръжка'
    PSEUDO_SPOUT = 'псевдочучур'
    SMOOTH_FRACTURE = 'плавен прелом'
    BICONICAL ='биконичност'
    DOUBLE_DISH = 'двоен съд'
    WHOLE_DISH = 'цял съд'


class BottomType(FormEnum):
    NO_BOTTOM = ''
    THICK = 'А'
    LOW_CHAIR = 'Б'
    HIGH_CHAIR = 'В'
    CONCAVE_PROFILED = 'А1'
    THICK_PROFILED = 'А2'
    CONCAVE_UNPROFILED = 'Б1'
    THICK_UNPROFILED = 'Б2'
    HIGH_HOLLOW_CHAIR = 'В1'
    LOW_CHAIR_HAND = 'В2'


class IncludeType(FormEnum):
    ANTHROPOGENIC = 'антропогенен'
    NATURAL = 'естествен'
    NO_INCLUDE_TYPE = ''


class Primary_(FormEnum):
    Type_A_ornament = 'А'
    Type_B_ornament = 'В'
    Type_D_ornament = 'Д'
    Type_I_ornament = 'И'
    Type_K_ornament = 'К'
    Type_N_ornament = 'Н'
    Type_P_ornament = 'П'
    Type_R_ornament = 'Р'
    Type_F_ornament = 'Ф'
    Type_C_ornament = 'Ц'
    Type_TS_ornament = 'Щ'
    Empty_type = ''

class Secondary(FormEnum):
    Type_one = 'I'
    Type_two = 'II'
    Type_three = 'III'
    Type_four = 'IV'
    Type_five = 'V'
    Type_six = 'VI'
    Type_seven = 'VII'
    Type_eight = 'VIII'
    Type_nine = 'IX'
    Type_ten = 'X'
    Type_eleven = 'XI'
    Type_twelve = 'XII'
    Type_thirteen = 'XIII'
    Type_fourteen = 'XIV'
    Type_fiveteen = 'XV'
    Type_sixteen = 'XVI'
    Type_seventeen = 'XVII'
    Type_empty = ''


class Tertiary(FormEnum):
    Type_A = 'А'
    Type_B = 'Б'
    Type_V = 'В'
    Type_G = 'Г'
    Type_D = 'Д'
    Type_E = 'Е'
    Type_J = 'Ж'
    Type_Z = 'З'
    Type_I = 'И'
    Type_K = 'К'
    Type_L = 'Л'
    Type_M = 'М'
    Type_P = 'П'
    Type_A1 = 'А1'
    Type_A2 = 'А2'
    Type_B1 = 'Б1'
    Type_B2 = 'Б2'
    Empty_type = ''

#includeconc = Column(db.Enum('ниска', 'средна', 'висока', '', name='includeconc_type'))
class Includeconc(FormEnum):
    Empty_conc = ''
    Low_conc = 'ниска'
    Medium_conc = 'средна'
    High_conc = 'висока'

class AddLayerForm(FlaskForm):
    site = StringField('Обект', validators=[DataRequired()])
    sector = StringField('Сектор')
    square = StringField('Квадрат')
    context = StringField('Контекст')
    layer = StringField('Пласт')
    stratum = StringField('Стратиграфия')
    level = StringField('Ниво')
    structure = StringField('Структура')
    includes = StringField('Примеси')
    color1 = SelectField('Цвят1', choices=[choice.value for choice in Color2])
    color2 = SelectField('Цвят2', choices=[choice.value for choice in Color2])
    recordenteredby = StringField('Въведен от', validators=[DataRequired()])
    recordcreatedby = StringField('Създаден от', validators=[DataRequired()])
    recordcreatedon = DateField('Създаден на', validators=[DataRequired()])
    description = StringField('Описание')
    akb_num = IntegerField('АКБ Номер', default=0)

    def save_entry(self, entry):
        self.populate_obj(entry)
        return entry


class AddFragmentForm(FlaskForm):
    #locationid = IntegerField('ID пласт', validators=[DataRequired()])
    technology = SelectField('Технология',  choices=[choice.value for choice in Technology])
    #speed = SelectField('Скорост', choices=[choice.value for choice in Speed])
    baking = SelectField('Изпичане', choices=[choice.value for choice in Baking])
    fract = SelectField('Лом', choices=[choice.value for choice in Fracture])
    includessize = SelectField('Размер примеси', choices=[choice.value for choice in SizeShort2])
    includesconc = SelectField('Концентрация примеси', choices=[choice.value for choice in IncludesConcentration])
    surface = SelectField('Повърхност', choices=[choice.value for choice in Surface])
    covering = SelectField('Покритие', choices=[choice.value for choice in Covering])
    primarycolor = SelectField('Основен цвят', choices=[choice.value for choice in Color])
    secondarycolor = SelectField('Вторичен цвят', choices=[choice.value for choice in Color2])
    category = StringField('Категория')
    form = StringField('Форма')
    type = IntegerField('Тип', default=0)
    subtype = StringField('Подтип')
    variant = IntegerField('Вариант', default=0)
    piecetype = SelectField('Фрагмент от', choices=[choice.value for choice in PieceType])
    wallthickness = SelectField('Дебелина на стената', choices=[choice.value for choice in SizeShort])
    dishsize = SelectField('Размер на съда', choices=[choice.value for choice in SizeShort])
    handletype = StringField('Тип дръжка')
    #handlesize = SelectField('Размер на дръжката', choices=[choice.value for choice in SizeShort])
    bottomtype = SelectField('Тип дъно', choices=[choice.value for choice in BottomType])
    outline = SelectField('Силует', choices=[choice.value for choice in Outline])
    #includestype = SelectField('Тип примеси', choices=[choice.value for choice in IncludesType])
    count = IntegerField('Брой', validators=[DataRequired()])
    onepot = SelectField('Цял съд', choices=[choice.value for choice in OneDish])
    note = StringField('Бележка')
    inventory = StringField('Инвентарен номер')
    recordenteredby = StringField('Въведен от', validators=[DataRequired()])
    #topsize = DecimalField('Размер на устие', places=2, default=0.0)
    #necksize = DecimalField('Размер на шия', places=2, default=0.0)
    #bodysize = DecimalField('Размер на тяло', places=2, default=0.0)
    #bottomsize = DecimalField('Размер на дъно', places=2, default=0.0)
    #dishheight = DecimalField('Височина на съд', places=2, default=0.0)
    #decoration = StringField('Декорация')
    #composition = StringField('Композиция')
    #parallels = StringField('Паралели')

    def save_entry(self, entry):
        self.populate_obj(entry)
        return entry


class AddLayerIncludeForm(FlaskForm):
    locationid = IntegerField('ID пласт', validators=[DataRequired()])
    includetype = SelectField('Тип примеси', choices=[choice.value for choice in IncludeType])
    includetext = StringField('Вид примеси')
    includesize = SelectField('Размер на примеси', choices=[choice.value for choice in SizeLong])
    includeconc = SelectField('Концентрация на примеси', choices=[choice.value for choice in Includeconc])

    def save_entry(self, entry):
        self.populate_obj(entry)
        return entry


class AddOrnamentForm(FlaskForm):
    fragmentid = IntegerField('ID фрагмент', validators=[DataRequired()])
    location = StringField('Положение')
    #color1 = SelectField('Цвят1', choices=[choice.value for choice in Color])
    #color2 = SelectField('Цвят2', choices=[choice.value for choice in Color])
    encrustcolor1 = StringField('Инкрустация цвят1')
    encrustcolor2 = StringField('Инкрустация цвят2')
    primary_ = SelectField('Украса', choices=[choice.value for choice in Primary_])
    secondary = SelectField('Орнамент', choices=[choice.value for choice in Secondary])
    tertiary = SelectField('Комбинация', choices=[choice.value for choice in Tertiary])
    quarternary = IntegerField('Мотив', default=0)

    def save_entry(self, entry):
        self.populate_obj(entry)
        return entry


class AddPokForm(FlaskForm):
    locationid = IntegerField('ID пласт', validators=[DataRequired()])
    type = StringField('Тип')
    quantity = IntegerField('Количество (бр.)', default=0)
    weight = DecimalField('Килограми ПОК', places=3, default=0.0)
    sok_weight = DecimalField('Килограми СОК', places=3, default=0.0)

    def save_entry(self, entry):
        self.populate_obj(entry)
        return entry


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

