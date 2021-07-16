from django.db import models


class MyModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Create your models here.
class Employer(MyModel):
    class Meta:
        db_table = 'hr_employer'
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return '%s %s' % (type(self), self.id)
