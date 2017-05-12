from django.db import models


# Create your models here.

field = """
TIME:
AV:

"""

class Room(models.Model):
	set_date = models.DateField(unique = True,null=True,blank = True,verbose_name ='set date')
	symph_a = models.TextField(max_length = 200,blank = True,verbose_name ='Symphony A',default=field)
	symph_b = models.TextField(max_length = 200,blank = True,verbose_name ='Symphony b',default=field)
	ballroom = models.TextField(max_length = 200,blank = True,verbose_name ='Ballroom',default=field)
	mozart = models.TextField(max_length = 200,blank = True,verbose_name ='mozart',default=field)
	beethoven = models.TextField(max_length = 200,blank = True,verbose_name ='Beethoven',default=field)
	board = models.TextField(max_length = 200,blank = True,verbose_name ='Temple Boardroom',default=field)
	handel = models.TextField(max_length = 200,blank = True,verbose_name ='Handel',default=field)
	haydn = models.TextField(max_length = 200,blank = True,verbose_name ='Haydn',default=field)
	thirty_third = models.TextField(max_length = 200,blank = True,verbose_name ='33rd',default=field)
	capitol = models.TextField(max_length = 200,blank = True,verbose_name ='Capitol',default=field)
	other = models.TextField(max_length = 200,blank = True, verbose_name ='Other',default=field)
		
	
	
	
	