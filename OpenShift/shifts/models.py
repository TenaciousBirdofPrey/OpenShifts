from django.db import models

# Create your models here.

class open_shift(models.Model):
	date = models.DateField(null=True,verbose_name ='shift date')
	start = models.CharField(max_length = 10,verbose_name ='start time')
	end = models.CharField(max_length = 10,verbose_name ='end time')
	description = models.CharField(max_length = 200, verbose_name =' description')
	attire = models.CharField(max_length = 200, verbose_name ='attire')
	is_filled = models.BooleanField(default = False)
	is_sent = models.BooleanField(default = False)
	filled_by = models.CharField(max_length = 200, null = True, blank = True, verbose_name ='filled by')
		
	class Meta:
	    permissions = (
	            ("can_add_date", "Can add date"),
	        )