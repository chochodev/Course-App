from django.db import models
from django.utils.text import slugify

# Create your models here.
class CourseHead(models.Model):
    id = models.IntegerField(primary_key=True, null=False, blank=False, unique=True)
    name = models.CharField(max_length=50, unique=True, null=True, blank=True)
    description = models.CharField(max_length=1000, null=False, blank=False)
    main_price = models.IntegerField(null=True)
    frac_price = models.IntegerField(null=True)
    image = models.ImageField(default='peep-3.jpg', null=False)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name[0:20]}"

class CourseSection(models.Model):
    section_number = models.IntegerField(primary_key=True, null=False, blank=False)
    section_name = models.CharField(max_length=1000, null=False, blank=False)
    course_head = models.ForeignKey(CourseHead, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f"ID: {self.section_number} - {self.section_name[0:35]}"

    class Meta:
        ordering = ['section_number']

class CourseContent(models.Model):
    content_number = models.IntegerField(null=False, blank=False)
    content_name = models.CharField(max_length=200, null=False, blank=False)
    video_file = models.FileField(default='coursevideo.mp4', upload_to='videos/', null=False)
    course_section = models.ForeignKey(CourseSection, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f"ID: {self.content_number} - {self.content_name[0:35]}"
    
    class Meta:
        ordering = ['course_section', 'content_number']
        # unique_together = ('content_number', 'course_section')

