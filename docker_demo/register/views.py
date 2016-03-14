from django.shortcuts import render, get_object_or_404
from .forms import RegisterForm
from django.utils import timezone
from django.shortcuts import redirect
from .models import Attendee

def attendee_new(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			attendee = form.save(commit=False)
			attendee.signed_up = timezone.now()
			attendee.save()
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
