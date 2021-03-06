from flask_wtf import Form
from wtforms.fields import StringField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Length

from app import db
from app.models import DefaultChecklistItem, Document


class DefaultChecklistItemForm(Form):
    title = StringField(validators=[InputRequired(), Length(1, 64)])
    description = TextAreaField(validators=[InputRequired()])
    submit = SubmitField()

class MultipleFileUploadField(StringField):
    pass

class UploadDocumentForm(Form):
    file_urls = MultipleFileUploadField(
            'Select & Upload File')
    submit = SubmitField('Upload Document')