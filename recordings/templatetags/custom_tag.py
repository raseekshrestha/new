from django import template
import random

register = template.Library()



@register.simple_tag
def kounter():
	with open('counter.txt','r') as f:
		num = int(f.read().strip())
		
	with open('counter.txt','w') as f:
		num += 1
		f.write(str(num))

	return num

@register.simple_tag
def kounterReset():
	with open('counter.txt','w') as f:
		f.write('0')
	return ''



	



    