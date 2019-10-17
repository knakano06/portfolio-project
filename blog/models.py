from django.db import models

# Create a Blog model
class Blog(models.Model):
    # title
    title = models.CharField(max_length = 255)
    # pub_date
    pub_date = models.DateTimeField()
    # body
    body = models.TextField()
    # image
    image = models.ImageField(upload_to = 'images/')

# Add the Blog app to the settings

# Create a migration

# Migrate

# Add to the admin
