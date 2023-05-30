from .models import *



def createTicketId(title):
    if title == 'Software':
        ticketsCount = Ticket.objects.filter(department='Software').count()
        return 'SW-' + str(ticketsCount + 1)
    elif title == 'Project Management':
        ticketsCount = Ticket.objects.filter(department='Project Management').count()
        return 'PM-' + str(ticketsCount + 1)
    elif title == 'Visitor':
        ticketsCount = Ticket.objects.filter(department='Visitor').count()
        return 'VS-' + str(ticketsCount + 1)
