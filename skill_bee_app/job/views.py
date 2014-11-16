from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User

from auth_op.models import ClientUser, StudentUser

def view_students(request):
  context = RequestContext(request)
  
  render_page = 'error.html'
  render_dict = {}

  if request.method == 'GET':
    if request.user.is_authenticated():
      try:
        client_id = ClientUser.objects.get(user_id=request.user.id)
        cat = 'APP' # this is for testing
        
        render_page = 'cat_list.html'
        if(cat != 'APP' and cat != 'SUP' and cat != 'SOC'):
          render_dict['error_message'] = 'Category key is not valid.'
          except

        if(cat == 'APP'):
          student_id_list = StudentUser.objects.get(app_bool=True)
        if(cat == 'SUP'):
          1
        if(cat == 'SOC'):
          1
        curr_student = {}
        curr_student['name']
        curr_student['major']
        curr_student['gpa']
        curr_student['request_url']
      except:
        render_dict['error_message'] = "User does not have a CLIENT account."
    else:
      render_dict['error_message'] = "User is not authenticated."
  else:
    render_dict['error_message'] = "Incorrect request type."

  return render_to_response(render_page, render_dict, context)
