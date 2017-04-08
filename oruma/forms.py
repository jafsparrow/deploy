from django import forms

# project related
from .models import Applicant, Recommender, Dependend,Detail, Application

class ApplicantModelForm(forms.ModelForm):
    first_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}), max_length = 100, label='First Name')
    last_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}), max_length=100, label='Second Name')
    SEX = (('M', 'Male'),('F', 'Female'))
    sex = forms.ChoiceField( widget=forms.Select(attrs={'class': 'form-control'}), choices=SEX, label='Gender')
    phone_number = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'}), max_length=13, label='Phone Number')
    date_of_birth = forms.DateField( widget = forms.DateInput(attrs={'placeholder': 'MM/DD/YYYY', 'class': 'form-control'}), label='Date of Birth')
    occupation = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Occupation', 'class': 'form-control'}), max_length=50, label='Occupation')
    address = forms.CharField(widget = forms.Textarea(attrs={'placeholder': 'Address', 'class': 'form-control', 'rows':'3'}), max_length=300, label='Address')
    monthly_family_income =forms.IntegerField(widget = forms.NumberInput(attrs={'placeholder': 'Monthly Income', 'class': 'form-control'}),label='Monthly total Income')
    no_earners = forms.IntegerField(widget = forms.NumberInput(attrs={'placeholder': 'Number of earning members', 'class': 'form-control'}), label='Number of earners')

    class Meta:
        model = Applicant
        fields = '__all__'

class RecommenderModelForm(forms.ModelForm):
    first_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}),max_length = 100, label='First Name')
    last_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Second Name', 'class': 'form-control'}),max_length=100, label='Second Name')
    phone_number = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'}), max_length=13, label='Phone Number')
    email = forms.EmailField(widget = forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),max_length=80, label='Email')
    address = forms.CharField(widget = forms.Textarea(attrs={'placeholder': 'Address', 'class': 'form-control', 'rows':'3'}), max_length=300, label='Address')

    class Meta:
        model = Recommender
        fields= '__all__'


class DependendModelFrom(forms.ModelForm):
    class Meta:
        model = Dependend
        fields = '__all__'

class DetailModelFrom(forms.ModelForm):
    class Meta:
        model = Detail
        fields = '__all__'

class ApplicationModelForm(forms.ModelForm):

    estimated_amount = forms.IntegerField(widget = forms.NumberInput(attrs={'placeholder': 'Enter Estimated Amount', 'class': 'form-control'}),label='Estimated Amount')
    self_amount = forms.IntegerField(widget = forms.NumberInput(attrs={'placeholder': 'Enter Self Contributing Amount', 'class': 'form-control'}),label='Self Contribution')
    ouruma_expected = forms.IntegerField(widget = forms.NumberInput(attrs={'placeholder': 'Enter Oruma Aid amount', 'class': 'form-control'}),label='Oruma Expected')

    class Meta:
        model =  Application
        fields = '__all__'


class recommenderForm(forms.Form):
    recommender_first_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}),max_length = 100, label='First Name')
    recommender_last_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Second Name', 'class': 'form-control'}),max_length=100, label='Second Name')
    recommender_phone = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'}), max_length=13, label='Phone Number')
    recommender_email = forms.EmailField(widget = forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),max_length=80, label='Email')
    recommender_address = forms.CharField(widget = forms.Textarea(attrs={'placeholder': 'Address', 'class': 'form-control', 'rows':'3'}), max_length=300, label='Address')


class applicantForm(forms.Form):
    applicant_first_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}), max_length = 100, label='First Name')
    applicant_second_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Second Name', 'class': 'form-control'}), max_length=100, label='Second Name')
    SEX = (('M', 'Male'),('F', 'Female'))

    applicant_sex = forms.ChoiceField( widget=forms.Select(attrs={'class': 'form-control'}), choices=SEX, label='Gender')
    applicant_phone = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'}), max_length=13, label='Phone Number')
    applicant_bod = forms.DateField( widget = forms.DateInput(attrs={'placeholder': 'MM/DD/YYYY', 'class': 'form-control'}), label='Date of Birth')
    applicant_occupation = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Occupation', 'class': 'form-control'}), max_length=50, label='Occupation')
    applicant_address = forms.CharField(widget = forms.Textarea(attrs={'placeholder': 'Address', 'class': 'form-control', 'rows':'3'}), max_length=300, label='Address')
    applicant_monthly_income =forms.IntegerField(widget = forms.NumberInput(attrs={'placeholder': 'Monthly Income', 'class': 'form-control'}),label='Monthly total Income')
    applicant_family_earners = forms.IntegerField(widget = forms.NumberInput(attrs={'placeholder': 'Monthly Income', 'class': 'form-control'}), label='Number of earners')






class testformapplicant(forms.Form):
    first_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}), max_length = 100, label='First Name')
    last_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Second Name', 'class': 'form-control'}), max_length=100, label='Second Name')
    SEX = (('M', 'Male'),('F', 'Female'))

    sex = forms.ChoiceField( widget=forms.Select(attrs={'class': 'form-control'}), choices=SEX, label='Gender')
    phone_number = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'}), max_length=13, label='Phone Number')
    date_of_birth = forms.DateField( widget = forms.DateInput(attrs={'placeholder': 'MM/DD/YYYY', 'class': 'form-control'}), label='Date of Birth')
    occupation = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Occupation', 'class': 'form-control'}), max_length=50, label='Occupation')
    address = forms.CharField(widget = forms.Textarea(attrs={'placeholder': 'Address', 'class': 'form-control', 'rows':'3'}), max_length=300, label='Address')
    monthly_family_income =forms.IntegerField(widget = forms.NumberInput(attrs={'placeholder': 'Monthly Income', 'class': 'form-control'}),label='Monthly total Income')
    no_earners = forms.IntegerField(widget = forms.NumberInput(attrs={'placeholder': 'Monthly Income', 'class': 'form-control'}), label='Number of earners')


class ArticleForm(forms.Form):
    title = forms.CharField()
    pub_date = forms.DateField()


class DependendForm(forms.Form):
    dependend_name = forms.CharField(max_length=100, label='Name')
    relation = forms.CharField(max_length=100, label='Relation')
    dob = forms.DateField( widget = forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}), label='Date of Birth')
    occupattion = forms.CharField(max_length=100, label='Occupation')
