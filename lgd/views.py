from django.shortcuts import render
from django.utils.translation import ugettext as _
# Create your views here.

def index(request):
    	context = {
		'name': _('K Md Mamunur Rashid')
	}
	return render(request, 'lgd/index.html', context)