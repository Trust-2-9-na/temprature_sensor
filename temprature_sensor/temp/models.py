from django.db import models


class SensorData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is created
    temperature = models.FloatField()  # Store temperature data as a float

    def __str__(self):
        return f"SensorData at {self.timestamp} - Temp: {self.temperature}°C"


