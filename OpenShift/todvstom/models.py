from django.db import models


# Create your models here.

class Rooms(models.Model):
	set_date = models.DateField(null=True,blank = True,verbose_name ='set date')
	symph_a = models.TextField(max_length = 200,blank = True,verbose_name ='Symphony A')
	symph_b = models.TextField(max_length = 200,blank = True,verbose_name ='Symphony b')
	ballroom = models.TextField(max_length = 200,blank = True,verbose_name ='Ballroom')
	mozart = models.TextField(max_length = 200,blank = True,verbose_name ='mozart')
	beethoven = models.TextField(max_length = 200,blank = True,verbose_name ='Beethoven')
	board = models.TextField(max_length = 200,blank = True,verbose_name ='Temple Boardroom')
	handel = models.TextField(max_length = 200,blank = True,verbose_name ='Handel')
	haydn = models.TextField(max_length = 200,blank = True,verbose_name ='Haydn')
	thirty_third = models.TextField(max_length = 200,blank = True,verbose_name ='33rd')
	capitol = models.TextField(max_length = 200,blank = True,verbose_name ='Capitol')
	other = models.TextField(max_length = 200,blank = True, verbose_name ='Other')
		
	
	
	
	