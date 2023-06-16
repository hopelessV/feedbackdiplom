from django import forms
from .models import FeedbacksModel

class feedback(forms.ModelForm):
    def __init__(self, args, **kwargs):
        super().__init__(args, **kwargs)

    class Meta:
        model = FeedbacksModel # модель формы
        fields = ('vacation', 'name', 'middlename', 'surrname', 'date_ofbirth', 'residential_address', 'criminal_record', 'number', 'emails', 'description')
        labels = {
            'vacation': ('Выберите вакансию'),
            'name': ('Имя'),
            'middlename': ('Фамилия'),
            'surrname': ('Отчество'),
            'number': ('Номер телефона'),
            'emails': ('Почта для связи'),
            'date_ofbirth': ('Дата рождения'),
            'residential_address': ('Адрес проживания'),            
            'criminal_record': ('Наличие судимости'),
            'description': ('Почему именно эта вакансия'),
        }
    
    