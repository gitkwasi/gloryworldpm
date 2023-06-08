from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import *
from .utils import *
from .serializers import *
from .decorators import ticketcreationalert, commentcreationalert, ticketupdatealert
# Create your views here.


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        
        token['email'] = user.email
        token['first'] = user.first_name
        token['last'] = user.last_name
        token['id'] = user.id
        token['department'] = user.department
        token['email'] = user.email
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



@api_view(['GET'])
def getTickets(request):
    data = Ticket.objects.all()
    serializer = TicketSerializer( data, many=True)
    
    return Response(serializer.data, status= status.HTTP_200_OK)



@api_view(['GET'])
def getUsers(request):

    data =  User.objects.all()

    serializer = UserSerializer(data, many=True)

    return Response( serializer.data, status = status.HTTP_200_OK)


@api_view(['POST'])
@ticketcreationalert
def createTicket(request, pk):
    context = {'pk':pk}
    print(request.data)
    serializer = TicketSerializer(data = request.data, many= False, context=context)

    if serializer.is_valid():
        serializer.save()
        print(serializer.data)
        return Response( serializer.data, status =status.HTTP_201_CREATED)
    
    return Response(status= status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
@ticketupdatealert
def updateTicket(request, pk):
    try:
        ticket = Ticket.objects.get(id = pk)
    except Ticket.DoesNotExist:
        return Response({'message':'Task does not exist'}, status=status.HTTP_404_NOT_FOUND)

    print(request.data)
    serializer = TicketSerializer(ticket, data = request.data, partial =True)

    if serializer.is_valid():
        serializer.save()
        print(serializer.data)
        return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
    print(serializer.errors)
    



@api_view(['GET'])
def taskDetail(request, pk):
    
    try:

        ticket = Ticket.objects.get(id = pk)
    except Ticket.DoesNotExist:
        return Response({'message':'Task does not exist'}, status=status.HTTP_404_NOT_FOUND)

    serializer = TicketSerializer(ticket, many =False)

    return Response(serializer.data, status = status.HTTP_200_OK)



@api_view(['POST'])
@commentcreationalert
def createComment(request, pk):
    print(request.data)
    context = {"pk":pk}

    serializer = CommentSerializer(data = request.data, many= False, context= context)

    if serializer.is_valid():
        
        serializer.save()
        print(serializer.data)
        return Response(serializer.data, status =status.HTTP_201_CREATED )
    print(serializer.errors)
    return Response(status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getComments(request,pk):
    
    ticket = Ticket.objects.get(id= pk)
    comments = ticket.comments_set.all()


    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data, status = status.HTTP_200_OK )