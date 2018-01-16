from django.db import models

class Pintoo(models.Model):
    pintoo = models.CharField(max_length=128, unique=False)
    def __str__(self):
        return self.pintoo
    

class Commodity(models.Model):
    commodity = models.CharField(max_length=128, unique=False)                                   #文章內容
    pintoo = models.ForeignKey(Pintoo)                                      
    image1 = models.ImageField(null=True, blank=True, upload_to='commodity/')                           #文章圖說
    image2 = models.ImageField(null=True, blank=True, upload_to='commodity/')                        #文章圖說
    def __str__(self):
        return self.commodity