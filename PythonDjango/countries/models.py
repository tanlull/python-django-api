from django.db import models

# Create your models here.
class Countries(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,blank=False,default='')
    capital = models.CharField(max_length=50,blank=False,default='')
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('id',)

# class Countries(models.Model):
#     c_id = models.IntegerField(primary_key=True)
#     name=models.CharField(max_length=50,blank=False,default='')
#     capital = models.CharField(max_length=50,blank=False,default='')

#     def __str__(self):
#         return self.name

#     class Meta:
#         db_table = u'countries'


# class Countries(models.Model):
#     job_id = models.CharField(max_length=10, primary_key=True)
#     job_title = models.CharField(max_length=35)
#     min_salary = models.IntegerField(null=True, blank=True)
#     max_salary = models.IntegerField(null=True, blank=True)


# class Meta:
#     db_table = u'countries'

# def __str__(self):
#     return self.job_title