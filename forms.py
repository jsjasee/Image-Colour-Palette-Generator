from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, SubmitField, FileField, IntegerField
from wtforms.validators import DataRequired, URL, InputRequired, ValidationError, NumberRange
from wtforms.fields import DateField

class ImageForm(FlaskForm):
    file = FileField('Upload the image file', validators=[DataRequired(), FileAllowed(['jpg', 'jpeg', 'png'],
                                                                                      'Only image files allowed!')])

    # maybe implement feature to get image from url?
    number_of_colours = IntegerField("How many colours would you like to extract? Max: 100",
                                     validators=[DataRequired(), NumberRange(max=100, min=1)],
                                     )
    submit = SubmitField("EXTRACTTT!")