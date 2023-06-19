from django import forms
from .models import FeedbacksModel, Post

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

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

    class Meta:
        model = Post
        fields = ('question','text')
        labels = {
            'question': ('Тема вопроса'),
            'text': ('Текст вопроса')
        }
        help_texts = {
            'question': ('Выберите тему вопроса'),
            'text': ('Введите текст вопроса')
        }

class ResponseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = FeedbacksModel
        fields = ('response_status',)
        labels = {
            'response_status': ('Текст сообщения кандидату'),
        }

class ComentResponseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Post
        fields = ('response_status',)
        labels = {
            'response_status': ('Текст сообщения кандидату'),
        }