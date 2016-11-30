from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):

    user = models.OneToOneField(User, null=True, unique=True)
    assign = models.OneToManyField(Assignment, null=True)

    website = models.URLField(blank=True)
    score = models.IntegerField(blank=True)

    def __unicode__(self):
        return self.user.username


class Assignment(models.Model):

	assignment_name = models.CharField(max_length=50)
	question = models.CharField(max_length=500)

	max_score = models.IntegerField(default=100)

	def __unicode__(self):ub
		return self.assignment_name


class Submission(models.Model):

	assignment = model.ForeignKey(Assignment)
	user = model.ForeignKey(UserProfile)
	code_link = model.CharField(max_length=200, blank=True)

	timestamp = model.DateTimeField(auto_now_add=True)
	score = models.IntegerField(default=0)

	def __unicode__(self):
		return self.assignment.assignment_name