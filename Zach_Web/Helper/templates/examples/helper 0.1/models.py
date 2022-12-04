# отсюда в DB передаются данные при помощи makemigrations
class ToDo(models.Model):
    title = models.CharField('Task', max_length=500)
    is_complete = models.BooleanField('Done', default=False)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title


class Task(models.Model):
    task_name = models.CharField(default='No name', max_length=500)
    task_link = models.URLField(max_length=2000)
    start_time = models.TimeField(default='12:00:00')

    sunday = models.BooleanField(default=False)
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name