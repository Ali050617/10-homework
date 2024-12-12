from django.db import models
from django.shortcuts import reverse

class Notes(models.Model):
    note_title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)


    def get_detail_url(self):
        return reverse('notes:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('notes:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('notes:delete', args=[self.pk])

