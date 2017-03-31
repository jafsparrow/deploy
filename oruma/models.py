from django.db import models

# Create your models here.




class Recommender(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length = 12)
    email = models.EmailField(max_length=80)
    address = models.TextField(max_length=300)

    def __str__(self):
        return self.first_name



class Applicant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    SEX = (('M', 'Male'),('F', 'Female'))
    sex = models.CharField(max_length=2, choices=SEX)
    date_of_birth = models.DateField()
    occupation = models.CharField(max_length=50)
    monthly_family_income = models.IntegerField()
    no_earners = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.first_name

class Dependend(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete= models.CASCADE)
    full_name = models.CharField(max_length=100)
    relation = models.CharField(max_length=50, null=True)
    age = models.IntegerField()
    occupation = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.full_name





class Application(models.Model):
    Recommender = models.ForeignKey(Recommender)
    Applicant = models.ForeignKey(Applicant)
    estimated_amount = models.IntegerField(default = 0)
    self_amount = models.IntegerField(default=0)
    ouruma_expected = models.IntegerField(default=0)
    STATUS = (('N','New'),('S','Submited'),('R', 'Review'),('A', 'Accepted'),('RJ','Rejected'))
    status = models.CharField(max_length = 10, choices =STATUS, default='N' )
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now = True)
    app_stage = models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)

    # A profperty to chedk if editable.
    # if status is 'new', 'review' return true.
    def is_app_editable(self):
        if self.status == 'N' or self.status == 'R':
            return True
        else:
            return False


# define a model to track notes associated with application.
class ApplicationNotes(models.Model):
    Application = models.ForeignKey(Application)
    note = models.TextField(null=True)
    created = models.DateField(auto_now=True)

    
class Documents(models.Model):
    application = models.ForeignKey(Application)
    description = models.CharField(max_length=100)
    document = models.FileField(upload_to ='application/files')

    def __str__(self):
        return self.description



class Detail(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    aid_type = models.CharField(max_length=200)
    add_information = models.CharField(max_length=500)


    def __str__(self):
        return self.aid_type
