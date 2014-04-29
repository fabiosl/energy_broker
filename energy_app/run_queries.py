import random
from energy_app.models import *

def run_queries():
	print "Running queries"
	queries = Query.objects.all()
	chunks = PowerChunk.objects.all()
	for query in queries:
		print query
		for pc in PowerChunk.objects.filter(amount__lte=query.needed_power).order_by('-amount','total_cost'):
			print pc

run_queries()