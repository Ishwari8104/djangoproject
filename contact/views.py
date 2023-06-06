'''from django.shortcuts import render

from .forms import ContactForm
# Create your views here.
def index(request):
    form=ContactForm()
    return render(request,'contact/index.html',{
        'form':form
    })'''
    
'''from django.shortcuts import render
from contact.forms import ContactForm

def index(request):
    if request.method == 'POST':
        # Form submission logic
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            # ...
            return render(request, 'index.html', {'form': form, 'success': True})
        else:
            # Form is invalid, render the form with errors
            return render(request, 'index.html', {'form': form})
    else:
        # Render the form
        form = ContactForm()
        return render(request, 'index.html', {'form': form})'''
'''from django.shortcuts import render,redirect
from django.core.mail import send_mail
from contact.forms import ContactForm
from django.template.loader import render_to_string

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            content=form.cleaned_data['content']
            html=render_to_string('contact/emails/contactform.html',{'name':name,'email':email,'content':content}
                
            )
            # Process the form data
            # ...
            send_mail('The contact form subject','This is the message','2021.ishwari.datir@ves.ac.in',['datir.ishwari@gmail.com'],html_message=html)
            return redirect('index')#render(request, 'contact/success.html')  # Render a success page
        else:
            return render(request, 'contact/index.html', {'form': form})
    else:
        form = ContactForm()
        return render(request, 'contact/index.html', {'form': form})'''
'''from django.shortcuts import render, redirect
from django.core.mail import send_mail
from contact.forms import ContactForm

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            
            # Format the email content
            message = f"Name: {name}\nEmail: {email}\nContent: {content}"
            
            send_mail(
                'Contact Form Submission',
                message,
                'datir.ishwari@gmail.com',  # Replace with your email address
                ['datir.ishwari@gmail.com'],  # Replace with the recipient's email address
            )
            
            return redirect('index')
        else:
            return render(request, 'contact/index.html', {'form': form})
    else:
        form = ContactForm()
        return render(request, 'contact/index.html', {'form': form})'''
'''from django.shortcuts import render, redirect
from django.core.mail import send_mail
from contact.forms import ContactForm

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            
            # Format the email content
            message = f"Name: {name}\nEmail: {email}\nContent: {content}"
            
            send_mail(
                'Contact Form Submission',
                message,
                email,  # Use the user's email address as the sender
                ['datir.ishwari@gmail.com'],  # Replace with the recipient's email address
            )
            
            return redirect('index')
        else:
            return render(request, 'contact/index.html', {'form': form})
    else:
        form = ContactForm()
        return render(request, 'contact/index.html', {'form': form})'''
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from contact.forms import ContactForm

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            phone_number = form.cleaned_data['phone_number']
            class_name = form.cleaned_data['class_name']
            dob = form.cleaned_data['dob']
            
            # Format the email content
            message = f"Name: {name}\nEmail: {email}\nContent: {content}\nPhone Number: {phone_number}\nClass: {class_name}\nDate of Birth: {dob}"
            
            send_mail(
                'Contact Form Submission',
                message,
                email,  # Use the user's email address as the sender
                ['datir.ishwari@gmail.com'],  # Replace with the recipient's email address
            )
            
            return redirect('index')
        else:
            return render(request, 'contact/index.html', {'form': form})
    else:
        form = ContactForm()
        return render(request, 'contact/index.html', {'form': form})




