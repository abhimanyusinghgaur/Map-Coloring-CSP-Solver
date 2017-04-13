import time
from django.http import HttpResponse
from django.shortcuts import render
from .utils import username, availableColors, availableAlgorithms
from .csp import *

# Create your views here.
def index(request):
	context={
		'username': username,
		'colors': availableColors,
		'algorithms': availableAlgorithms
	}
	return render(request, 'MapColoring/index.html', context);

def process_csp_and_color_map(request):
	colors = str(request.POST.get('colors'));
	countries = str(request.POST.get('countries'));
	neighbours = str(request.POST.get('neighbours'));
	algorithm = int(request.POST.get('algorithm'));
	assert colors and countries and neighbours and (algorithm>=0 and algorithm <=3), 'Please provide proper parameters.';
	
	csp = MapColoringCSP(list(colors),neighbours);

	result = None;
	start = time.time();
	if algorithm == 0:
		result = backtracking_search(csp);
	elif algorithm == 1:
		result = backtracking_search(csp, inference=forward_checking);
	elif algorithm == 2:
		result = backtracking_search(csp, inference=mac);
	else :
		result = min_conflicts(csp);
	end = time.time();

	if result is not None:
		for x in countries.split(','):
			if x in result:
				result[x] = availableColors[result[x]].colorCode;
			else :
				result[x] = '';

	context={
		'result': result,
		'chosenColors': {availableColors[key].name:availableColors[key].colorCode for key in list(colors)},
		'algorithm': availableAlgorithms[algorithm],
		'runTime': end-start,
	};
	return render(request, 'MapColoring/result.html', context);