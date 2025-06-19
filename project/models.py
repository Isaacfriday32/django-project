from django.db import models

# Create your models here.

class ProjectFormat(models.Model):
    title = models.CharField(max_length=2025)
    description = models.TextField()
    tech_stack= models.TextField()
    programmer = models.CharField()
    image = models.ImageField(default="default_image.png")      
    date = models.DateTimeField(auto_now_add=True)
    project_link = models.URLField(blank=True, null=True)


    def _str_(self):
        return self.ti
    
                                           