from django.db import models

class Blogs(models.Model):
    title=models.CharField(max_length=100)
    description =models.TextField()
    published_date=models.DateField()
    auther=models.CharField(max_length=20)

    # auther=models.ForeignKey(Auther,on_delete=models.PROTECT,blank=True,null=True)

    def __str__(self):
        return self.title
