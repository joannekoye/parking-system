from . import admin
from flask import url_for,render_template,redirect,request
from .forms import InstitutionForm
from ..models import Institution,Lot,Insights
from app import db
@admin.route('/')
def index():
    institutionForm = InstitutionForm()
    institutions = Institution.get_all()
    return render_template('admin/dashboard.html',institutionForm=institutionForm,institutions=institutions)

@admin.route('/new_institution')
def new_institution():
    institutionForm = InstitutionForm()
    return render_template('admin/new_institution.html',institutionForm=institutionForm)

@admin.route('/insights/institution_<int:institution_id>')
def insights(institution_id):
    insights = Insights.get_from_institution(institution_id)
    return render_template('admin/insights.html', insights=insights)


@admin.route('/new_institution', methods=['GET','POST'])
def new_institution_func():
    if request.environ['HTTP_REFERER'] is not None:
        institutionForm = InstitutionForm()
        if institutionForm.is_submitted():
            name = institutionForm.name.data
            active = institutionForm.active.data
            quantity = int(institutionForm.lot_numbers.data)
            tag_name = name.replace(' ','_')
            institution =Institution(name=name,tag_name=tag_name,active=active,quantity=quantity)
            db.session.add(institution) 
            db.session.commit()
            Lot.create_lots(tag_name,quantity)

        return redirect(request.environ['HTTP_REFERER'])