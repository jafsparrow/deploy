from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse

from .forms import Form1,recommenderForm,applicantForm, DependendForm
from .models import Applicant, Recommender, Application, Dependend, Detail
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



def stage_views(request, application_number, stage):
    pass
    '''
    if stage=2:
    if stage=3:
    if stage=4:

    '''
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
    applications = Application.objects.all()
    context ={'applications': applications}

    return render(request, 'oruma/applications.html', context)


def landing_view(request):
    return render(request, 'oruma/landingpage.html',{})
