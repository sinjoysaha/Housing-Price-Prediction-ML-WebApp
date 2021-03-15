from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, IntegerField, SelectField, RadioField
from wtforms.validators import DataRequired, Length

class InputParams(FlaskForm):
    rooms = IntegerField('Rooms',
                    validators=[DataRequired()])

    method = SelectField('Method',
    choices=[('S', 'S'), ('SP', 'SP'),
    ('PI', 'PI'), ('VB','VB'),('SA','SA')])

    ptype = RadioField('Type',
    choices=[('h', 'house,cottage,villa'), ('u', 'unit, duplex'), ('t', 'townhouse')], validators=[DataRequired()])

    # SellerG
    # Date

    postcode = IntegerField('Postcode',
                    validators=[DataRequired()])

    distance = DecimalField('Distance from Central Business District',
                    validators=[DataRequired()])

    region = SelectField('Region',
    choices=[('Northern Metropolitan', 'Northern Metropolitan'),
    ('Western Metropolitan', 'Western Metropolitan'),
    ('Southern Metropolitan', 'Southern Metropolitan'),
    ('Eastern Metropolitan','Eastern Metropolitan'),
    ('South-Eastern Metropolitan','South-Eastern Metropolitan'),
    ('Eastern Victoria','Eastern Victoria'),
    ('Northern Victoria','Northern Victoria'),
    ('Western Victoria','Western Victoria')])

    propertycount = IntegerField('Propertycount',
                    validators=[DataRequired()])

    bedrooms = IntegerField('Bedrooms',
                    validators=[DataRequired()])

    bathrooms = IntegerField('Bathrooms',
                    validators=[DataRequired()])

    cars = IntegerField('Car-Spots',
                    validators=[DataRequired()])

    landsize = DecimalField('Land Size',
                    validators=[DataRequired()])

    buildingarea = DecimalField('Building Area',
                    validators=[DataRequired()])

    yearbuilt = IntegerField('Year Built')

    latitude = DecimalField('Latitude',
                    validators=[DataRequired()])

    longitude = DecimalField('Longitude',
                    validators=[DataRequired()])

    # CouncilArea

# ['Suburb'*, 'Address'*, 'Rooms', 'Type', 'Price', 'Method', 'SellerG'*,
#        'Date'*, 'Distance', 'Postcode', 'Bedroom2', 'Bathroom', 'Car',
#        'Landsize', 'BuildingArea', 'YearBuilt', 'CouncilArea'*, 'Lattitude',
#        'Longtitude', 'Regionname', 'Propertycount']
# Roms: Number of rooms

# Price: Price in dollars

# Method: S - property sold; SP - property sold prior;
# PI - property passed in; PN - sold prior not disclosed;
# SN - sold not disclosed; NB - no bid; VB - vendor bid;
# W - withdrawn prior to auction; SA - sold after auction;
# SS - sold after auction price not disclosed.
# N/A - price or highest bid not available.

# Type: br - bedroom(s); h - house,cottage,villa, semi,terrace; u - unit, duplex; t - townhouse; dev site - development site; o res - other residential.

# SellerG: Real Estate Agent *

# Date: Date sold *

# Distance: Distance from CBD

# Regionname: General Region (West, North West, North, North east …etc)

# Propertycount: Number of properties that exist in the suburb.

# Bedroom2 : Scraped # of Bedrooms (from different source)

# Bathroom: Number of Bathrooms

# Car: Number of carspots

# Landsize: Land Size

# BuildingArea: Building Size

# CouncilArea: Governing council for the area *
