from django.db import models
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.title[:25]

    def summary(self):
        if len(self.body) > 50:
            return self.body[:50]+'...'
        return self.body

    def public_date_format(self):
        return self.pub_date.strftime('%m-%d-%Y')
