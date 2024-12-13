from django.db import models

class Table1 ( models.Model ):
    body = models.TextField ( )
    updated = models.DateTimeField( auto_now=True)
    created = models.DateTimeField( auto_now_add=  True )
    
    def __str__(self) -> str:
        return self.body[0:50]
    class Meta : 
        ordering = ['-updated']