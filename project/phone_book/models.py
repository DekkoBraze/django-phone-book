from django.db import models


class Record(models.Model):
    family = models.ForeignKey('Family', on_delete=models.CASCADE, related_name='record')
    name = models.ForeignKey('Name', on_delete=models.CASCADE, related_name='record')
    otchestvo = models.ForeignKey('Otchestvo', on_delete=models.CASCADE, blank=True, related_name='record')
    street = models.ForeignKey('Street', on_delete=models.CASCADE, blank=True, related_name='record')
    house = models.CharField(max_length=10, blank=True)
    korp = models.CharField(max_length=10, blank=True)
    apartments = models.IntegerField(null=True, blank=True)
    mob = models.OneToOneField('Mob', on_delete=models.SET_NULL, related_name='record', null=True)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        if self.family:
            if not self.family.record.all().exists():
                self.family.delete()
        if self.name:
            if not self.name.record.all().exists():
                self.name.delete()
        if self.otchestvo:
            if not self.otchestvo.record.all().exists():
                self.otchestvo.delete()
        if self.street:
            if not self.street.record.all().exists():
                self.street.delete()
        if self.mob:
            self.mob.delete()

    class Meta:
        ordering = ['id']


class Family(models.Model):
    value = models.CharField(max_length=30)

    def __str__(self):
        return self.value

    def delete(self, *args, **kwargs):
        records = self.record.all()
        for record in records:
            record.delete()
        try:
            super().delete(*args, **kwargs)
        except ValueError:
            pass

    class Meta:
        ordering = ['id']


class Name(models.Model):
    value = models.CharField(max_length=20)

    def __str__(self):
        return self.value

    def delete(self, *args, **kwargs):
        records = self.record.all()
        for record in records:
            record.delete()
        try:
            super().delete(*args, **kwargs)
        except ValueError:
            pass

    class Meta:
        ordering = ['id']


class Otchestvo(models.Model):
    value = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.value

    def delete(self, *args, **kwargs):
        records = self.record.all()
        for record in records:
            record.delete()
        try:
            super().delete(*args, **kwargs)
        except ValueError:
            pass

    class Meta:
        ordering = ['id']


class Street(models.Model):
    value = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.value

    def delete(self, *args, **kwargs):
        records = self.record.all()
        for record in records:
            record.delete()
        try:
            super().delete(*args, **kwargs)
        except ValueError:
            pass

    class Meta:
        ordering = ['id']


class Mob(models.Model):
    value = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.value

    def delete(self, *args, **kwargs):
        try:
            self.record.delete()
        except Record.DoesNotExist:
            super().delete(*args, **kwargs)
        #Телефон пытается удалить объект записи, который уже удален в методе delete записи, поэтому прописываем
        except ValueError:
            super().delete(*args, **kwargs)

    class Meta:
        ordering = ['id']
