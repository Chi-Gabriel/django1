from rest_framework.decorators import api_view 
from rest_framework.response import Response
from .serielizers import TableSerielizer 
from .models import Table1

@api_view(['GET'])
def getRoutes ( request ):
    print('uytn')
    routes = [
        {
            'Endpoint' : '/first',
            'method' : 'Get',
            'body' : None ,
            'description' : 'returns an array of notes'
        }
    ]
     
    return Response( routes  )

@api_view(['GET'])
def getTable ( request ):
    tables = Table1.objects.all( )
    serielizer = TableSerielizer( tables  , many = True )
    return Response( serielizer.data)

@api_view(['GET'])
def getRecord ( request , pk ):
    record = Table1.objects.get( id = pk )
    serielizer = TableSerielizer( record  , many = False )
    return Response( serielizer.data)

@api_view ( ['POST']) 
def createRecord ( request ) :
    data = request.data 
    rec = Table1.objects.create ( body = data['body'])
    ser = TableSerielizer ( rec , many = False )
    return Response ( ser.data )

@api_view( ['PUT'])
def updateRecord ( request , pk ) :
    data = request.data 
    rec = Table1.objects.get ( id = pk )
    ser = TableSerielizer ( rec  , data = data )
    if ( ser.is_valid( )): 
        ser.save ( )
    return Response ( ser.data )

@api_view(['DELETE']) 
def deleteRecord ( request , pk ):
    rec = Table1.objects.get ( id = pk )
    rec.delete( )
    return Response ( 'Deleted sucessfully')