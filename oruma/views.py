from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.forms.models import model_to_dict
from django.forms import formset_factory
from django.forms import modelformset_factory
import datetime
from django.urls import reverse
from django import forms
from django.contrib.auth.decorators import login_required

from .forms import (recommenderForm,applicantForm, DependendForm,
                        testformapplicant,
                        ArticleForm,
                        ApplicantModelForm,
                        RecommenderModelForm,
                        DependendModelFrom,
                        ApplicationModelForm)
from .models import Applicant, Recommender, Application, Dependend, Detail, Documents

# class bases views
from django.views import View

# Test views
class applicanttest_create_view(View):
    def get(self, request):
        return HttpResponse("hello I am from class based view")

@login_required
def applicant_create_view(request):
    if request.method == 'POST':
        form = ApplicantModelForm(request.POST)
        if form.is_valid:
            form.save()
        return HttpResponse('New applicant is saved')
    else:
        form = ApplicantModelForm()
    context = {'form': form }
    return render(request, 'oruma/applicantform.html', context)

from django.contrib import messages
def applicant_update_view(request, applicant_id):
    redirect_to = request.GET['next']
    print(redirect_to)
    applicant  = get_object_or_404(Applicant, id=applicant_id)
    if request.method == 'POST':

        # supply the class instance and the post data.
        form = ApplicantModelForm(request.POST, instance=applicant)
        if form.is_valid:
            form.save()
            messages.success(request, 'Applicant details have been updated..!')
        #return HttpResponse('create new recommender')
        return HttpResponseRedirect(redirect_to)

    else:
        form = ApplicantModelForm(instance=applicant)
    context = {'form': form}
    return render (request, 'oruma/applicantform.html', context)


def recommender_create_view(request):
    redirect_to = request.GET['next']
    if request.method == 'POST':
        form = RecommenderModelForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Recommender details have been updated..!')
            return HttpResponse('create new recommender')
        return HttpResponseRedirect(redirect_to)
    else:
        form = RecommenderModelForm()
    context = { 'form' : form }
    return render(request, 'oruma/applicantform.html', context)



def recommender_update_view(request, recommender_id):
    recommender = get_object_or_404(Recommender, id=recommender_id)
    if request.method == 'POST':
        form = RecommenderModelForm(request.POST, instance=recommender)
        if form.is_valid:
            form.save()
            #return HttpResponse('Updated the recommender')
            return reverse(request.next)
    else:
        form = RecommenderModelForm(instance=recommender)
    context = { 'form' : form }
    return render(request, 'oruma/applicantform.html', context)


@login_required
def application_step_1(request):
    if request.method == 'POST':
        applicant=ApplicantModelForm(request.POST or None, prefix='applicant')
        recommender=RecommenderModelForm(request.POST or None, prefix='recommender')
        user_entered_app_number = request.POST['application_user_number']
        if recommender.is_valid() and applicant.is_valid():
            # save applicant
            recommender_obj=  recommender.save()
            applicant_obj= applicant.save()
            # Create New Application.
            application = Application(Recommender=recommender_obj, Applicant=applicant_obj, application_number = user_entered_app_number)
            application.save()

            if application:
                return HttpResponseRedirect(reverse('application_step_2', kwargs = {'application_number': application.id}))
                #return render(request, 'oruma/stage2.html', {'application': application.id })
        else:
            print("Form date is not valid and failed at form.isvalid method")
    # for GET render This.
    else:
        recommender=RecommenderModelForm(prefix='recommender')
        applicant=ApplicantModelForm(prefix='applicant')

    context = { 'applicantForm': applicant,
                'recommender': recommender,
                }
    return render(request, 'oruma/stage1.html', context)


@login_required
def application_step_2(request, application_number):
    #check if there is next save the next from get request.
    #redirect_to = request.GET.get(next, None)
    #print(redirect_to)
    application = get_object_or_404(Application, id=application_number)
    applicant = application.Applicant
    #Dependend_form = DependendForm()
    #DependendFormSet = formset_factory(Dependend_form) #, extra=5)
    #formset = DependendFormSet()
    query = Dependend.objects.filter(applicant = applicant)
    widget_dict = {
                'full_name': forms.TextInput(attrs={'placeholder': 'Dependend Name', 'class': 'form-control'}),
                'relation' : forms.TextInput(attrs={'placeholder': 'Relation', 'class': 'form-control'}),
                'age' : forms.NumberInput(attrs={'placeholder': 'Age', 'class': 'form-control'}),
                'occupation' : forms.TextInput(attrs={'placeholder': 'Occupation', 'class': 'form-control'})

                }
    DependendFormSet = modelformset_factory(Dependend, exclude=('applicant',), widgets = widget_dict, extra=4, max_num=8)#fields='__all__') #

    if request.method == 'POST':
        formset = DependendFormSet(request.POST)
        if formset.is_valid:
            instances = formset.save(commit=False)
            for instance in instances:
                instance.applicant = applicant
                instance.save()
            return HttpResponseRedirect(reverse('application_step_3', kwargs = {'application_number': application_number}))
            #if redirect_to is None or redirect_to == '':

            #else:
                #print('running from blank')
                #return HttpResponseRedirect(redirect_to)
    else:
        formset = DependendFormSet(queryset=query)

    context = { 'formset': formset }
    return render(request, 'oruma/stage2.html', context)


@login_required
def application_step_3(request, application_number):
    application = get_object_or_404(Application, id=application_number)
    query = Detail.objects.filter(application = application)
    SEX = (('M', 'Male'),('F', 'Female'))
    widget_dict = {
                'aid_type': forms.TextInput(attrs={'class': 'form-control'}),
                'add_information' : forms.Textarea(attrs={'placeholder': 'Add Extra infromation', 'rows':'3', 'class': 'form-control'}),
                }
    DetailFormSet = modelformset_factory(Detail, exclude=('application',), widgets = widget_dict, extra=4, max_num=8)#fields='__all__') #
    if request.method == 'POST':
        application_form = ApplicationModelForm(request.POST)
        formset = DetailFormSet(request.POST)
        print(application_form)
        if application_form.is_valid():
            print('app form is valid')
        if formset.is_valid():
            print('formset is also valid')
        if formset.is_valid() and application_form.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.application = application
                instance.save()

            app = application_form.save()
            return HttpResponseRedirect(reverse('application_step_4', kwargs = {'application_number': application_number}))
    else:
        application_form = ApplicationModelForm(instance=application)
        formset = DetailFormSet(queryset=query)

    context = { 'formset': formset , 'appform': application_form,}
    return render(request, 'oruma/stage3.html', context)


@login_required
def application_step_4(request, application_number):
    application = get_object_or_404(Application, id=application_number)
    query = Documents.objects.filter(application = application)
    widget_dict = {
                'description': forms.TextInput(attrs={'placeholder': 'File Name', 'class': 'form-control'}),
                #'Document': forms.FileField(attrs={'class': 'btn btn-default'}),
                }
    DocumentFormSet = modelformset_factory(Documents, fields=('description','document'), widgets=widget_dict, extra=2, max_num=3)#fields='__all__') #
    if request.method == 'POST':
        formset = DocumentFormSet(request.POST, request.FILES)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.application=application
                instance.save()
            return HttpResponseRedirect(reverse('application_step_5', kwargs = {'application_number': application_number}))
    else:
        formset = DocumentFormSet(queryset=query)

    context = { 'formset': formset }
    return render(request, 'oruma/stage4.html', context)


@login_required
def application_step_5(request, application_number):
    application = get_object_or_404(Application, id=application_number)
    recommender = application.Recommender
    applicant = application.Applicant
    dependends = Dependend.objects.filter(applicant=applicant)
    details = Detail.objects.filter(application=application)
    docs = Documents.objects.filter(application=application)
    context ={ 'recommender': recommender,
                    'applicant': applicant,
                    'application': application,
                    'details':details,
                    'dependends': dependends,
                    'docs': docs

                }
    return render(request, 'oruma/stage5.html', context)


# Create your views here.
def form1view(request):
    #form = Form1()
    if request.method == 'POST':
        applicant=applicantForm(request.POST or None)
        recommender=recommenderForm(request.POST or None)
        if recommender.is_valid() and applicant.is_valid():
            # save applicant
            applicant_object = Applicant(first_name=applicant.cleaned_data['applicant_first_name'],
                                    last_name = applicant.cleaned_data['applicant_second_name'],
                                    phone_number = applicant.cleaned_data['applicant_phone'],
                                    sex= applicant.cleaned_data['applicant_sex'],
                                    date_of_birth =applicant.cleaned_data['applicant_bod'],
                                    occupation = applicant.cleaned_data['applicant_occupation'],
                                    monthly_family_income = applicant.cleaned_data['applicant_monthly_income'],
                                    no_earners = applicant.cleaned_data['applicant_family_earners'],
                                    address = applicant.cleaned_data['applicant_address']
                                    )
            applicant_object.save()
            # save recommender
            recommnder_object = Recommender(first_name = recommender.cleaned_data['recommender_first_name'],
                                        last_name = recommender.cleaned_data['recommender_last_name'],
                                        phone_number = recommender.cleaned_data['recommender_phone'],
                                        email = recommender.cleaned_data['recommender_email'],
                                        address = recommender.cleaned_data['recommender_address'],
                                        )
            recommnder_object.save()
            # Create New Application.
            application = Application(Recommender=recommnder_object, Applicant=applicant_object)
            application.save()

            if application:
                print(application.id)
                return HttpResponseRedirect(reverse('stage_2_view', kwargs = {'application_number': application.id}))
                #return render(request, 'oruma/stage2.html', {'application': application.id })
        else:
            print("Form date is not valid and failed at form.isvalid method")
    # for GET render This.
    else:
        recommender=recommenderForm()
        applicant=applicantForm()

    context = {#'form': form,
                'applicantForm': applicant,
                'recommender': recommender,

                }
    return render(request, 'oruma/stage1.html', context)




def applicantion_user_edit(request, application_number):
    application = Application.objects.get(pk=application_number)
    applicant = application.Applicant

    ArticleFormSet = formset_factory(ArticleForm, extra=5)
    #formset = ArticleFormSet()

    formset = ArticleFormSet(initial=[
        {'title': 'Django is now open source',
        'pub_date': datetime.date.today(),}
            ])

    #initial={'q': q}
    # pass intitial values as dictionaries.
    form = testformapplicant(model_to_dict(applicant))
    context = {'form': form, 'formset': formset }
    return render(request, 'oruma/test.html', context)


def stage_2_view(request, application_number):
    #if POST
    if request.method == 'POST':
        counter = 0
        application = Application.objects.get(pk=application_number)#get(id=application_number)[0]
        applicant = application.Applicant
        if request.POST['1_name']:
            depended1 = Dependend(applicant = applicant,
                                    full_name = request.POST['1_name'],
                                    relation = request.POST['1_relation'],
                                    age = request.POST['1_age'],
                                    occupation = request.POST['1_occupation']
                                )
            depended1.save()

        if request.POST['2_name']:
            depended2 = Dependend(applicant = applicant,
                                    full_name = request.POST['2_name'],
                                    relation = request.POST['2_relation'],
                                    age = request.POST['2_age'],
                                    occupation = request.POST['2_occupation']
                                )
            depended2.save()
        if request.POST['3_name']:
            depended3 = Dependend(applicant = applicant,
                                    full_name = request.POST['3_name'],
                                    relation = request.POST['3_relation'],
                                    age = request.POST['3_age'],
                                    occupation = request.POST['3_occupation']
                                )
            depended3.save()
        if request.POST['4_name']:
            depended4 = Dependend(applicant = applicant,
                                    full_name = request.POST['4_name'],
                                    relation = request.POST['4_relation'],
                                    age = request.POST['4_age'],
                                    occupation = request.POST['4_occupation']
                                )
            depended4.save()

        return HttpResponseRedirect(reverse('stage_3_view', kwargs = {'application_number': application_number, 'stage_number':3}))


    return render(request, 'oruma/stage2.html', {'application_number': application_number} )

def stage_3_view(request, application_number, stage_number):
    #return HttpResponse("helloworld")
    if request.method=="POST":
        application = Application.objects.get(pk=application_number)#get(id=application_number)[0]
        if request.POST['aid_1_details']:
            aid_detail = Detail(application=application, aid_type=request.POST['aid_1'], add_information=request.POST['aid_1_details'])
            aid_detail.save()
        if request.POST['aid_2_details']:
            aid_detail = Detail(application=application, aid_type=request.POST['aid_2'], add_information=request.POST['aid_2_details'])
            aid_detail.save()
        if request.POST['aid_3_details']:
            aid_detail = Detail(application=application, aid_type=request.POST['aid_3'], add_information=request.POST['aid_3_details'])
            aid_detail.save()
        if request.POST['aid_4_details']:
            aid_detail = Detail(application=application, aid_type=request.POST['aid_4'], add_information=request.POST['aid_4_details'])
            aid_detail.save()
        if request.POST['aid_5_details']:
            aid_detail = Detail(application=application, aid_type=request.POST['aid_5'], add_information=request.POST['aid_5_details'])
            aid_detail.save()
        if request.POST['aid_6_details']:
            aid_detail = Detail(application=application, aid_type=request.POST['aid_6'], add_information=request.POST['aid_6_details'])
            aid_detail.save()

        # change the application related entries.
        application.estimated_amount = request.POST['estimated_amount']
        application.self_amount = request.POST['self_amount']
        application.ouruma_expected = request.POST['ouruma_expected']
        application.status = "S"
        application.save()

        return HttpResponseRedirect(reverse('application_summary', kwargs = {'application_number': application_number}))

    return render(request, 'oruma/stage3.html', {})



def application_summary(request, application_number):

    #get the appplication
    application = Application.objects.get(pk=application_number)#get(id=application_number)[0]
    # get recommenderForm
    recommender = application.Recommender
    # get applicantForm
    applicant = application.Applicant
    # get dependen.
    dependends = Dependend.objects.filter(applicant=applicant)
    # get all the aids
    details = Detail.objects.filter(application=application)

    context ={ 'recommender': recommender,
                'applicant': applicant,
                'application': application,
                'dependends': dependends,
                'details':details

            }
    return render(request, 'oruma/Summary.html', context)



def applications(request):
    # get the queryset based on logged in users or user's unit.
    # if the user is staff, then return all.
    applications = Application.objects.all()
    context ={'applications': applications}

    return render(request, 'oruma/applications.html', context)


def landing_view(request):
    return render(request, 'oruma/landingpage.html',{})
