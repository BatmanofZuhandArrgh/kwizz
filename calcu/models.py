from django.db import models

class InputFirstNum(models.Model):
    num0 = models.IntegerField(default=0)

    def get_num(self):
        return self.num0
    
    def __str__(self) -> str:
        return str(self.num0)

class InputOperation(models.Model):
    BASIC_OPS = [
        ('ADD', '+'),
        ('SUB', '-'),
        ('MUL', 'x'),
    ]
    
    op = models.CharField(
        max_length=3,
        choices=BASIC_OPS,
        default='ADD'
    )
    def get_op(self):
        return self.op

class InputSecondNum(models.Model):
    num1 = models.IntegerField(default=0)
    def get_num(self):
        return self.num0
