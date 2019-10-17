from django.db import models

# this is a Blog model
class Blog(models.Model):
    # title
    title = models.CharField(max_length = 255)
    # pub_date
    pub_date = models.DateTimeField()
    # body
    body = models.TextField()
    # image
    image = models.ImageField(upload_to = 'images/')

    # function that will allow the admin page to display each blog title
    def __str__(self):
        return self.title

    # function that will return certain portion of the body
    def summary(self):
        return self.body[:100]+"..."

    # customize publishing dates
    def pub_date_neat(self):
        return self.pub_date.strftime('%B %e, %Y')
