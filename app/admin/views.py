from . import admin
from flask import url_for,render_template,redirect,request
from .forms import InstitutionForm
from ..models import Institution
from app import db
@admin.route('/')
def index():
    institutionForm = InstitutionForm()
    return render_template('admin/new_institution.html',institutionForm=institutionForm)

@admin.route('/new_institution', methods=['GET','POST'])
def new_institution():
    if request.environ['HTTP_REFERER'] is not None:
        institutionForm = InstitutionForm()
        if institutionForm.is_submitted():
            name = institutionForm.name.data
            tag_name = name.replace(' ','_')
            institution =Institution(name=name,tag_name=tag_name)
            db.session.add(institution) 
            db.session.commit()

        return redirect(request.environ['HTTP_REFERER'])