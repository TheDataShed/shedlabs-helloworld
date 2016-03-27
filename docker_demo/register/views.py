from django.shortcuts import render, get_object_or_404
from .forms import RegisterForm
from django.utils import timezone
from django.shortcuts import redirect
from .models import Attendee
import sendgrid


def send_mail(first_name, last_name, email_address, organisation):

        full_name = first_name + " " + last_name
        subj =  "I'm all ready to go with the DataShed Labs!"
        body = "Attendee details: Name: {0} , Email Address: {1}, Organisation: {2}".format(full_name, email_address, organisation)
        
        client = sendgrid.SendGridClient("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")
        
        message = sendgrid.Mail()

        message.add_to("hello@thedatashed.co.uk")
        message.set_from(email_address)

        message.set_subject(subj)
        message.set_html(body)

        client.send(message)

def attendee_new(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			attendee = form.save(commit=False)
			attendee.signed_up = timezone.now()
			attendee.save()
			send_mail(attendee.first_name,attendee.surname,attendee.email_address, attendee.company)
			return redirect('attendee_detail', pk=attendee.pk)
	else:
		form = RegisterForm()
	return render(request, 'register/attendee_edit.html', {'form': form})

def attendee_detail(request, pk):
    attendee = get_object_or_404(Attendee, pk=pk)
    return render(request, 'register/attendee_detail.html', {'attendee': attendee})

def attendee_list(request):
	attendees = Attendee.objects.filter(signed_up__lte=timezone.now()).order_by('signed_up')
 	return render(request, 'register/attendee_list.html', {'attendees': attendees})
