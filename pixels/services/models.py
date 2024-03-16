# models.py
from django.db import models
from django.contrib.auth.models import User
from traitlets import default

class FoodPrediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    foods = models.CharField(max_length=255)
    result = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        app_label = 'services'
class DiabetesPrediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pregnancies = models.FloatField(verbose_name='Pregnancies', default=0)
    glucose = models.FloatField(verbose_name='Glucose', default=0)
    blood_pressure = models.FloatField(verbose_name='Blood Pressure', default=0)
    skin_thickness = models.FloatField(verbose_name='Skin Thickness', default=0)
    insulin = models.FloatField(verbose_name='Insulin', default=0)
    bmi = models.FloatField(verbose_name='BMI', default=0)
    diabetes_pedigree_function = models.FloatField(verbose_name='Diabetes Pedigree Function', default=0)
    age = models.FloatField(verbose_name='Age', default=0)
    result = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        app_label = 'services'
class HeartDiseasePrediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    sex = models.CharField(max_length=6)  # Assuming 'male' or 'female'
    chestpain = models.IntegerField()
    blood_pressure = models.IntegerField()
    cholesterol = models.IntegerField()
    fasting_blood_sugar = models.IntegerField()
    ekg_results = models.IntegerField()
    max_heart_rate = models.IntegerField()
    exercise_induced_angina = models.IntegerField()
    st_depression = models.FloatField()
    st_slope = models.IntegerField()
    num_vessels = models.IntegerField()
    thallium = models.IntegerField()
    result = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        app_label = 'services'
class SleepCyclePrediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start = models.FloatField(verbose_name='Start', default=0.0)
    end = models.FloatField(verbose_name='End', default=0.0)
    regularity = models.FloatField(verbose_name='Regularity', default=0.0)
    steps = models.FloatField(verbose_name='Steps', default=0.0)
    movements_per_hour = models.FloatField(verbose_name='Movements per hour', default=0.0)
    time_in_bed_seconds = models.FloatField(verbose_name='Time in bed (seconds)', default=0.0)
    time_asleep_seconds = models.FloatField(verbose_name='Time asleep (seconds)', default=0.0)
    time_before_sleep_seconds = models.FloatField(verbose_name='Time before sleep (seconds)', default=0.0)
    window_start = models.FloatField(verbose_name='Window start', default=0.0)
    window_stop = models.FloatField(verbose_name='Window stop', default=0.0)
    snore_time = models.FloatField(verbose_name='Snore time', default=0.0)

    result = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Sleep Cycle - ID: {self.id}"
    class Meta:
        app_label = 'services'