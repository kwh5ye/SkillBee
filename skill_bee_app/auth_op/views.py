from auth_op.forms import StudentRegForm, ClientRegForm, UserRegForm

from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

class IndexView(generic.ListView):
    template_name = 'auth_index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        return "12345"

def register_student(request):
    context = RequestContext(request)

    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_reg_form = UserRegForm(data=request.POST)
        student_reg_form = StudentRegForm(data=request.POST)

        # If the two forms are valid...
        if user_reg_form.is_valid() and student_reg_form.is_valid(): 
            # Save the user's form data to the database.
            student = user_reg_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            student.set_password(student.password)
            student.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            student_reg = student_reg_form.save(commit=False)
            student_reg.user = student

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                student_reg.picture = request.FILES['picture']

            # Now we save the StudentUser model instance.
            a = student_reg.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print student_reg_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_reg_form = UserRegForm()
        student_reg_form = StudentRegForm()

    # Render the template depending on the context.
    return render_to_response(
            'register_student.html',
            {'user_reg_form': user_reg_form, 'student_reg_form': student_reg_form, 'registered': registered},
            context)

def register_client(request):
    context = RequestContext(request)

    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_reg_form = UserRegForm(data=request.POST)
        client_reg_form  = ClientRegForm(data=request.POST)

        # If the two forms are valid...
        if user_reg_form.is_valid() and client_reg_form.is_valid(): 
            # Save the user's form data to the database.
            student = user_reg_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            student.set_password(student.password)
            student.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            client_reg = client_reg_form.save(commit=False)
            client_reg.user = student

            # Now we save the StudentUser model instance.
            a = client_reg.save()
            print a

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print client_reg_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_reg_form = UserRegForm()
        client_reg_form = ClientRegForm()

    # Render the template depending on the context.
    return render_to_response(
            'register_client.html',
            {'user_reg_form': user_reg_form, 'client_reg_form': client_reg_form, 'registered': registered},
            context)

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/auth/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('login.html', {}, context)

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/auth/')
