from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=120, default='Vivek Ray')
    role = models.CharField(max_length=120, default='Aspiring Software Developer')
    tagline = models.CharField(max_length=240, default='Building Modern Web Applications with Django & JavaScript')
    location = models.CharField(max_length=120, default='Madhubani, Bihar, India')
    email = models.EmailField(default='vivekray7970@gmail.com')
    phone = models.CharField(max_length=40, default='+91 7970936214')
    linkedin_url = models.URLField(default='https://linkedin.com/in/vivek-rai-1b06893C')
    github_url = models.URLField(default='https://github.com/vivekrai7970-max')
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=180)
    summary = models.TextField()
    technologies = models.CharField(max_length=220)
    github_url = models.URLField(blank=True, null=True)
    demo_url = models.URLField(blank=True, null=True)
    case_study_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
class Skill(models.Model):
    category = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    proficiency = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.category} - {self.name}"


class Certificate(models.Model):
    title = models.CharField(max_length=160)
    subtitle = models.CharField(max_length=220, blank=True)
    issued_by = models.CharField(max_length=140, blank=True)

    def __str__(self):
        return self.title


class Achievement(models.Model):
    title = models.CharField(max_length=180)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Education(models.Model):
    title = models.CharField(max_length=180)
    institution = models.CharField(max_length=220)
    location = models.CharField(max_length=120, blank=True)
    year_range = models.CharField(max_length=80)
    extra_info = models.CharField(max_length=220, blank=True)

    def __str__(self):
        return self.title

