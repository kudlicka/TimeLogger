from django.db import models


class Department(models.Model):
    title = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    department = models.ForeignKey('Department', models.CASCADE)
    supervisor = models.ForeignKey('self', models.SET_NULL, blank=True, null=True)
    comment = models.TextField(blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Project(models.Model):
    title = models.CharField(max_length=255, unique=True)
    planned_hours = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class TimeEntry(models.Model):
    project = models.ForeignKey('Project', models.CASCADE)
    employee = models.ForeignKey('Employee', models.DO_NOTHING)
    date = models.DateField()
    duration = models.DurationField()
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['-date', 'project__title', 'employee__last_name', 'employee__first_name']
        verbose_name_plural = 'time entries'

    def __str__(self):
        return f"{self.employee} @ {self.project} on {self.date}"
