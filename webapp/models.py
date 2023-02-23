from django.db import models
from django.db.models import TextChoices
from django.utils import timezone

# Create your models here.


class StatusChoice(TextChoices):
    NEW = "NEW", "НОВАЯ"
    IN_PROGRESS = "IN_PROGRESS", "В ПРОЦЕССЕ"
    FINISHED = "FINISHED", "СДЕЛАНО"


class To_do(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        help_text="Заголовок задачи",
        verbose_name="Заголовок",
    )
    description = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        help_text="Кратко опишите задачу",
        verbose_name="Описание",
    )
    text = models.TextField(
        max_length=3000, null=True, blank=True, verbose_name="Текстовое поле"
    )
    status = models.CharField(
        max_length=20,
        choices=StatusChoice.choices,
        default=StatusChoice.NEW,
        help_text="Статус задачи",
        verbose_name="Статус",
    )
    execution_date = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        help_text="Введите в формате ГГГГ-ММ-ДД",
        verbose_name="Дата исполнения",
    )
    is_deleted = models.BooleanField(
        verbose_name="Удалено", null=False, default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата и время обновления"
    )
    deleted_at = models.DateTimeField(
        verbose_name="Дата и время удаления", null=True, default=None
    )

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return f"{self.title} - {self.description} - {self.status} - {self.execution_date}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
