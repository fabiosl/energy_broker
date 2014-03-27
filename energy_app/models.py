from django.db import models

class CloudProvider(models.Model): # "Cloud SLA's"
	service_name = models.CharField(max_length=60)
	cost_per_processed_gigabyte = models.FloatField(default=0) # in euros
	cost_per_uptime = models.FloatField(default=0) # in euros
	dataset_size = models.FloatField(default=0) # in gigs
	
	def __unicode__(self):
		return self.service_name

class PowerProducer(models.Model):
	name = models.CharField(max_length=40)
	location = models.CharField(max_length=100)
	
	def __unicode__(self):
		return "%s: %s" % (self.name, self.location)

class PowerChunk(models.Model):
	amount = models.IntegerField(default=0) #in watts
	cost_per_kilowatt = models.FloatField(default=0) # in euros
	time_to_produce = models.IntegerField(default=0) # in millis
	is_green = models.BooleanField(default=False)
	power_producer = models.ForeignKey(PowerProducer)
	cloud_hosting_chunk = models.ForeignKey(CloudProvider)

class Query(models.Model): # "Users' SLA's"
	needed_power = models.IntegerField(default=0) # in watts
	max_query_cost = models.IntegerField(default=0) # in euros
	max_power_cost = models.IntegerField(default=0) # price in euros
	only_green_energy = models.BooleanField(default=False) 
	query_timeout = models.IntegerField(default=0) # in millis


class Consumer(models.Model):
	name = models.CharField(max_length=40)
	location = models.CharField(max_length=100)

