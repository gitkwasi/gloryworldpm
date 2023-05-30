from rest_framework import serializers
from .models import *


class UserListingField(serializers.RelatedField):
    
    def to_representation(self, value):
        return value.first_name




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['id','department','first_name','last_name']

    
class TicketSerializer(serializers.ModelSerializer):
    
    reporter = UserListingField(many = False, read_only = True)
    
    class Meta:
        model = Ticket
        fields = '__all__'

    def create(self, validated_data):
        reporter = self.context['pk']
        user = User.objects.get(id= reporter)

        ticket = Ticket.objects.create(reporter =user,  **validated_data)
        return ticket



    



class CommentSerializer(serializers.ModelSerializer):
    user = UserListingField(many = False, read_only = True)
    
    class Meta:
        model = Comments
        fields ="__all__"

    def create(self, validated_data):    

        user = User.objects.get(id = self.context["pk"])   
        comment = Comments.objects.create(user= user, **validated_data)

        return comment