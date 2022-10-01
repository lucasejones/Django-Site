from django.db import models

# Create your models here.

'''
Comprehension Notes:
Each model has a number of variables.
	- Each variable represents a db field. 
Each field is represented by an instance of a Field class.
The variable names, (the content of which holdseach field instance) will be the column names in the db.
You can create an optional name as the first argument, as shown below in Question.pub_date: "date published".
''' 

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)


