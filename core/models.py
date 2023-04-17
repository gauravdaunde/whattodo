from django.db import models

# TODO
STANDARD_CHAR_SIZE = 256

LOW_PRIORITY_CODE = 0
MEDIUM_PRIORITY_CODE = 1
HIGH_PRIORITY_CODE = 2
LOW_PRIORITY_NAME = 'low'
MEDIUM_PRIORITY_NAME = 'medium'
HIGH_PRIORITY_NAME = 'high'
PRIORITY_NAME_TO_CODE_MAP = {
    LOW_PRIORITY_NAME: LOW_PRIORITY_CODE,
    MEDIUM_PRIORITY_NAME: MEDIUM_PRIORITY_CODE,
    HIGH_PRIORITY_NAME: HIGH_PRIORITY_CODE
}
PRIORITY_CODE_TO_NAME_MAP = {
    code: name for name, code in PRIORITY_NAME_TO_CODE_MAP.items()
}
CHOICES = (
    (LOW_PRIORITY_CODE, LOW_PRIORITY_NAME),
    (MEDIUM_PRIORITY_CODE, MEDIUM_PRIORITY_NAME),
    (HIGH_PRIORITY_CODE, HIGH_PRIORITY_NAME)
)


class TimeStampMixin(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class ToDo(TimeStampMixin):
    title = models.CharField(max_length=STANDARD_CHAR_SIZE)
    priority_code = models.IntegerField(default=LOW_PRIORITY_CODE)
    for_date = models.DateField()
    is_completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('for_date', 'title', 'priority_code')

    @property
    def priority(self):
        return PRIORITY_CODE_TO_NAME_MAP[self.priority_code]

    def __str__(self):
        return f'{self.title.title()}'

    def __repr__(self):
        return str(self)
