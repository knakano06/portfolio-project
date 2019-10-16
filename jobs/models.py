from django.db import models

class Job(models.Model):
    # refer to documentation for model field

    # image for each job description on my webpage
    # everytime someone uploads an image, save it to the images folder
    image = models.ImageField(upload_to = 'images/')

    # summary for each job
    # set a capacity for the size of the summary text box
    summary = models.CharField(max_length = 200)
    
