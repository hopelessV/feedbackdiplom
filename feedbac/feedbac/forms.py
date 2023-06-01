from django import forms
from startform.models import asd

class feedback(forms.ModelForm):
    def __init__(self, args, **kwargs):
        super().__init__(args, **kwargs)

    class Meta:
        model = asd # модель формы
        fields = ('vacation', 'name', 'middlename', 'surrname', 'number', 'emails', 'pasport_series', 'pasport_number', 'url_linc', 'description')
        labels = {
            'vacation': ('Выберите вакансию'),
            'name': ('Имя'),
            'middlename': ('Фамилия'),
            'surrname': ('Отчество'),
            'number': ('Номер телефона'),
            'emails': ('Почта для связи'),
            'pasport_series': ('Серия паспорта'),
            'pasport_number': ('Номер паспорта'),            
            'url_linc': ('Ссылка на облачное хранилище где расоложен документ об окончании обучения на выбранную вами специальность'),
            'description': ('Почему именно эта вакансия'),
        }
        help_texts = {
            'name': ('Влад'),
            'middlename': ('Кощеев'),
            'surrname': ('Дмитриевич'),
            'number': ('89194697098'),
            'emails': ('loading11210@mail.ru'),
            'pasport_series': ('2314'),
            'pasport_number': ('086253'),
            'url_linc': ('https://drive.google.com/file/d/1OlV3q4mQF11l9jTty3fgviwbiwL967Du/view?usp=sharing'),
        }    