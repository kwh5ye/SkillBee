from django.db import models

class Job(models.Model):
    NOT_ACCEPTED = 'NA'
    IN_PROGRESS = 'IP'
    COMPLETED = 'CP'
    PROG_STATE = (
                   (NOT_ACCEPTED, 'Not accepted'),
                   (IN_PROGRESS, 'In progress'),
                   (COMPLETED, 'Completed'),
                 )

    WEB_MOBILE = 'APP'
    TECH_SUPPORT = 'SUP'
    SOCIAL_MEDIA = 'SOC'
    CATEGORIES = (
                   (WEB_MOBILE, 'Web and Mobile Apps'),
                   (TECH_SUPPORT, 'Tech Support'),
                   (SOCIAL_MEDIA, 'Social Media'),
                 )

    description = models.TextField()
    category = models.CharField(max_length=3, choices=CATEGORIES)
    progress = models.CharField(max_length=2, choices=PROG_STATE, default=NOT_ACCEPTED)
    student_id = models.IntegerField()
    client_id = models.IntegerField()

    def __unicode__(self):
      return str(self.description)
