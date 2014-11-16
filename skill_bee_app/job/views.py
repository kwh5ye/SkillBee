from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User

from auth_op.models import ClientUser, StudentUser

def view_students(request, cat):
  context = RequestContext(request)
  
  render_page = 'error.html'
  render_dict = {}

  if request.method == 'GET':
    if request.user.is_authenticated():
      try:
        client_id = ClientUser.objects.get(user_id=request.user.id)
         
        if(cat != 'APP' and cat != 'SUP' and cat != 'SOC'):
          render_dict['error_message'] = 'Category key is not valid: <' + cat + '.'
        else:
          render_page = 'cat_list.html'
          if(cat == 'APP'):
            student_id_list = StudentUser.objects.filter(app_bool=True)
          if(cat == 'SUP'):
            student_id_list = StudentUser.objects.filter(sup_bool=True)
          if(cat == 'SOC'):
            student_id_list = StudentUser.objects.filter(soc_bool=True)

          student_list = {}
          for student in student_id_list:
            curr_student = {}
            curr_user = User.objects.get(id=student.user_id)        

            curr_student['name'] = curr_user.first_name + " " + curr_user.last_name
            curr_student['major'] = student.major
            curr_student['gpa'] = student.gpa
            student_list['student_id'] = curr_student
          
          render_dict['students'] = student_list
          render_dict['cat'] = cat
      except:
        render_dict['error_message'] = "User does not have a CLIENT account."
    else:
      render_dict['error_message'] = "User is not authenticated."
  else:
    render_dict['error_message'] = "Incorrect request type."

  return render_to_response(render_page, render_dict, context)
