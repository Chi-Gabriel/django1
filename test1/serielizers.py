from rest_framework.serializers import ModelSerializer 

from .models import Table1 

class TableSerielizer ( ModelSerializer ) :
    class Meta : 
        model = Table1 
        fields = '__all__'