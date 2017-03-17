from django import forms


class Form1(forms.Form):
    recommender_first_name = forms.CharField(max_length = 100, label='First Name')
    recommender_last_name = forms.CharField(max_length=100, label='Second Name')
    recommender_phone = forms.CharField(max_length=13, label='Phone Number')
    recommender_email = forms.EmailField(max_length=80, label='Email')
    recommender_address = forms.CharField(max_length=300, label='Address')
    applicant_first_name = forms.CharField(max_length = 100, label='First Name')
    applicant_second_name = forms.CharField(max_length=100, label='Second Name')
    SEX = (('M', 'Male'),('F', 'Female'))

    applicant_sex = forms.ChoiceField( choices=SEX, label='Gender')
    applicant_phone = forms.CharField(max_length=13, label='Phone Number')
    applicant_bod = forms.DateField(label='Date of Birth')
    applicant_occupation = forms.CharField(max_length=50, label='Occupation')
    applicant_monthly_income =forms.IntegerField(label='Monthly total Income')
    applicant_family_earners = forms.IntegerField(label='Number of earners')

class recommenderForm(forms.Form):
    recommender_first_name = forms.CharField(max_length = 100, label='First Name')
    recommender_last_name = forms.CharField(max_length=100, label='Second Name')
    recommender_phone = forms.CharField(max_length=13, label='Phone Number')
    recommender_email = forms.EmailField(max_length=80, label='Email')
    recommender_address = forms.CharField(widget = forms.Textarea, max_length=300, label='Address')


class applicantForm(forms.Form):
    applicant_first_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'First Name'}), max_length = 100, label='First Name')
    applicant_second_name = forms.CharField(max_length=100, label='Second Name')
    SEX = (('M', 'Male'),('F', 'Female'))

    applicant_sex = forms.ChoiceField( choices=SEX, label='Gender')
    applicant_phone = forms.CharField(max_length=13, label='Phone Number')
    applicant_bod = forms.DateField( widget = forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}), label='Date of Birth')
    applicant_occupation = forms.CharField(max_length=50, label='Occupation')
    applicant_address = forms.CharField(widget = forms.Textarea, max_length=300, label='Address')
    applicant_monthly_income =forms.IntegerField(label='Monthly total Income')
    applicant_family_earners = forms.IntegerField(label='Number of earners')


class DependendForm(forms.Form):
    dependend_name = forms.CharField(max_length=100, label='Name')
    relation = forms.CharField(max_length=100, label='Relation')
    dob = forms.DateField( widget = forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}), label='Date of Birth')
    occupattion = forms.CharField(max_length=100, label='Occupation')
