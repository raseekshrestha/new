from django.shortcuts import render
from .models import Record
from django.http import HttpResponse
# Create your views here.

def getSubjectValues(subjectCode,query=''):
	# subjectCode follows order as in Records.subjects
	# physics is at 0 the index, math in index 1  ans so on..
	return {
		'subject':Record.subjects[subjectCode][1],
		'records': Record.objects.filter(subject=Record.subjects[subjectCode][0],
			content__contains=query),
		'searchedTerm':query
	}



def index(requests):
	return render(requests,'index.html')


def physics(requests):
	subjectCode = 0
	if requests.method == 'GET':
		query = requests.GET.get('search','')
		values =  getSubjectValues(subjectCode,query)
	else:
		values = getSubjectValues(subjectCode)
	return render(requests,'subjects.html',values)

def maths(requests):
	subjectCode = 1
	if requests.method == 'GET':
		query = requests.GET.get('search','')
		values =  getSubjectValues(subjectCode,query)
	else:
		values = getSubjectValues(subjectCode)
	return render(requests,'subjects.html',values)

def c(requests):
	subjectCode = 2
	if requests.method == 'GET':
		query = requests.GET.get('search','')
		values =  getSubjectValues(subjectCode,query)
	else:
		values = getSubjectValues(subjectCode)
	return render(requests,'subjects.html',values)

def iit(requests):
	subjectCode = 3
	if requests.method == 'GET':
		query = requests.GET.get('search','')
		values =  getSubjectValues(subjectCode,query)
	else:
		values = getSubjectValues(subjectCode)
	return render(requests,'subjects.html',values)

def digitalLogic(requests):
	subjectCode = 4
	if requests.method == 'GET':
		query = requests.GET.get('search','')
		values =  getSubjectValues(subjectCode,query)
	else:
		values = getSubjectValues(subjectCode)
	return render(requests,'subjects.html',values)


