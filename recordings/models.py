from django.db import models

# Create your models here.

class Record(models.Model):
	subjects = [
		('physics','Physics'),
		('math','Maths'),
		('C','C Programming'),
		('IIT','IIT'),
		('DL','Digital Logic'),
	]
	subject = models.CharField(max_length=50,choices=subjects)
	date = models.CharField(max_length=20,default="")
	link = models.CharField(max_length=500)
	content = models.TextField(max_length=500)

	def __str__(self):
		return self.subject + " | " + self.content[:50]+"..."
