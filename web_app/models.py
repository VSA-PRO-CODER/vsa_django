import uuid
from django.db import models
from django.utils import timezone
from django.http import HttpResponse
def generate_unique_id():
    random_uuid = uuid.uuid4()
    random_number = int(random_uuid.hex[:8], 16)
    random_number = random_number % 10000000
    unique_id = f'{random_number:08}'
    return unique_id

class Reg_Data(models.Model):
    ID = models.CharField(primary_key=True, default=generate_unique_id, editable=False, max_length=50)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    img = models.ImageField(upload_to='upload/', default='upload/davatar.png')
    def __str__(self):
        return f"{self.name} - {self.email}"


class Salary(models.Model):
    ID = models.CharField(primary_key=True,max_length=36)
    name = models.CharField(max_length=100) 
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    salary_updated_date = models.DateField(default=timezone.now)
    class Meta:
        ordering = ['-salary_updated_date']
    def __str__(self):
        return f"ID: {self.ID}, Salary: {self.salary}, Updated Date: {self.salary_updated_date}"

    def save(self, *args, **kwargs):
        try:
            another_instance = Reg_Data.objects.get(ID=self.ID)
            self.name = another_instance.name
        except Reg_Data.DoesNotExist:
            print("ID does\'t match")
            return HttpResponse('ID does\'t match ')
        
        super().save(*args, **kwargs)
    