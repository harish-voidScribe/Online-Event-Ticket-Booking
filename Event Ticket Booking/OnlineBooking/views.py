from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Ticket

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    tickets = Ticket.objects.filter(event=event)
    return render(request, 'events/event_detail.html', {'event': event, 'tickets': tickets})

def payment(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)

    if request.method == 'POST':
        # Handle form submission logic for payment processing (implement security measures!)
        quantity = int(request.POST.get('quantity', 1))
        total_amount = ticket.price * quantity

        # Consider using a success message or redirecting to a confirmation page after successful payment

        return render(request, 'events/payment.html', {'ticket': ticket, 'total_amount': total_amount, 'quantity': quantity})

    return render(request, 'events/payment.html', {'ticket': ticket})
