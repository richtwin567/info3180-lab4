from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from flask_uploads import UploadSet, IMAGES

images_only = UploadSet("images", IMAGES)

class UploadForm(FlaskForm):
    image = FileField(validators=[FileRequired(), FileAllowed(images_only,"Only images are accepted")])
    