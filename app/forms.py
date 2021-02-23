from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
class UploadForm(FlaskForm):
    image = FileField(validators=[FileRequired(), FileAllowed(['jpg', 'png'],"Only images are accepted")])
