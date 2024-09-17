from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'add_contact.html', {'form': form})

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})

def contact_detail(request, pk):
    contact = Contact.objects.get(pk=pk)
    return render(request, 'contact_detail.html', {'contact': contact})

def edit_contact(request, pk):
    contact = Contact.objects.get(pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'edit_contact.html', {'form': form})

def delete_contact(request, pk):
    contact = Contact.objects.get(pk=pk)
    contact.delete()
    return redirect('home')

def search_contacts(request):
    query = request.GET.get('q')
    results = Contact.objects.filter(first_name__icontains=query) | Contact.objects.filter(email__icontains=query)
    return render(request, 'contacts/search_results.html', {'results': results})
