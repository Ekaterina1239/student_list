from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    course = models.CharField(max_length=250)
    average_mark =models.PositiveIntegerField()
    instrument = models.CharField(max_length=50)
    payment =models.BooleanField(blank=False)
    slug = models.SlugField(unique=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(f'{self.name}-{self.surname}-{self.course}')
        super(Student, self).save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f'{self.name}-{self.surname}-{self.course}'
