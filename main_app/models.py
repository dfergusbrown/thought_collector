from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name
    

class Thought(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    date_time = models.DateTimeField()
    tags = models.ManyToManyField(Tag)
    
    EMOTION_CHOICES = {
        "HAPPINESS": "Happiness",
        "SADNESS": "Sadness",
        "JOY": "Joy",
        "FEAR": "Fear",
        "ANGER": "Anger",
        "DISGUST": "Disgust",
    }
    emotion = models.CharField(
        choices=EMOTION_CHOICES
    )
    def __str__(self):
        return self.name


class Recurrence(models.Model):
    date = models.DateField()
    change = models.CharField(max_length=50)

    thought = models.ForeignKey(Thought, on_delete=models.CASCADE)

    def __str__(self):
        return f"A recurrence took place on {self.date}"
    
