from django.db import models

# Create your models here.
class Image(models.Model):
    tag = models.CharField(max_length = 100)
    image_url = models.ImageField(upload_to = 'pics/', default = 'pics/none/no-img.jpg')
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.image_url
    def image_tags(self):
        return  self.tag