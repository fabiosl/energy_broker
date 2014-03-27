import random
from energy_app.models import *

def drop_db():
	CloudProvider.objects.all().delete()
	PowerProducer.objects.all().delete()
	PowerChunk.objects.all().delete()
	Query.objects.all().delete()
	Consumer.objects.all().delete()

def _create_google_big_query_providers(scale_factors):
	for scale_factor in scale_factors:
		dataset_size = float( 1024 * scale_factor)
		cloud = CloudProvider(service_name="Google Big Query Dataset: %d scale_factor" % scale_factor, cost_per_processed_gigabyte=0.005, cost_per_uptime=0, dataset_size=dataset_size)
		cloud.save()

def _create_amazon_redshift_providers(scale_factors):
	for scale_factor in scale_factors:
		dataset_size = float( 1024 * scale_factor)
		cloud = CloudProvider(service_name="Amazon Redshift Dataset: %d scale_factor" % scale_factor, cost_per_processed_gigabyte=0, cost_per_uptime=0.215, dataset_size=dataset_size)
		cloud.save()		

def create_cloud_providers():
	scale_factors = [1, 2, 5, 10, 50, 100]
	_create_google_big_query_providers(scale_factors)
	_create_amazon_redshift_providers(scale_factors)


def create_power_producers():
	p1 = PowerProducer(name="Joao", location="Marseille")
	p2 = PowerProducer(name="Maria", location="Aix en Provence")
	p3 = PowerProducer(name="Lorrayne", location="Nimes")
	p4 = PowerProducer(name="Fabio", location="Marseille")
	p5 = PowerProducer(name="Genoveva", location="Grenoble")
	p6 = PowerProducer(name="Martin", location="Paris")
	p7 = PowerProducer(name="Jean Marc", location="Strausburgh")
	for p in [p1,p2,p3,p4,p5,p6,p7]: p.save()

def create_power_chunks(number_of_chunks):
	power_producers = PowerProducer.objects.all()
	cloud_providers = CloudProvider.objects.all()
	
	chunks = []
	for i in range(number_of_chunks):
		amount = random.randint(0,1000)
		cost_per_kilowatt = random.uniform(0.5, 2.0)
		time_to_produce = random.randint(0,120)
		is_green = bool(random.getrandbits(1))
		producer = power_producers[random.randint(0,(len(power_producers) - 1))]
		provider = cloud_providers[random.randint(0,(len(cloud_providers) - 1))]
		
		chunk = PowerChunk(amount=amount, cost_per_kilowatt=cost_per_kilowatt, time_to_produce=time_to_produce, is_green=is_green, power_producer=producer, cloud_hosting_chunk=provider)
		chunks.append(chunk)
	PowerChunk.objects.bulk_create(chunks)



drop_db()
create_cloud_providers()
create_power_producers()
create_power_chunks(100000)
