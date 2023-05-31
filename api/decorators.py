from .models import *
from django.core.mail import send_mail


# decorator to handle ticket creation notification

def ticketcreationalert(viewfunc):
    def wrapper_func(request,pk, *args, **kwargs):
        sender = User.objects.get(pk= pk).first_name
        title = request.data['title']
        recipient_pk = request.data['assignee'] 
        recipient = User.objects.get(pk= recipient_pk)

        send_mail(
            f"You have been assigned a task by {sender} ",
            f"The task is: {title}",
            str(sender),
            [str(recipient)],
            fail_silently= False,

        )
        return viewfunc(request,pk, *args, **kwargs)
    
    return wrapper_func


def ticketupdatealert(viewfunc):
    def wrapper_func(request, pk, *args, **kwargs):
        ticket = Ticket.objects.get(id = pk)
        assignee = ticket.assignee
        status = request.data['status']

        send_mail(
            f"The task : {ticket.title} has been updated ",
            f"It has been moved to : {status}",
            None,
            [str(assignee)],
            fail_silently= False,

        )

        return viewfunc(request, pk, *args, **kwargs)

    return wrapper_func


def commentcreationalert(viewfunc):
    def wrapper_func(request,pk, *args, **kwargs):
        
        sender = User.objects.get(pk= pk).first_name
        description = request.data['description']
        ticket = Ticket.objects.get(id = request.data['ticket']) 
        recipient = ticket.assignee

        send_mail(
            f"{sender} added a comment to the task ",
            f"{description}",
            None,
            [str(recipient)],
            fail_silently= False,

        )

        return viewfunc(request, pk, *args, **kwargs)
    
    return wrapper_func