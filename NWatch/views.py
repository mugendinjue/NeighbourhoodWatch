from django.shortcuts import render,redirect
from .forms import RegistrationForm,NeighbourhoodCreationForm,BusinessCreationForm,OccupantForm,HealthContactsForm,SecurityContactsForm,UserPostForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Neighbourhood,Occupant,Admin,Business,Health,Security,Posts,Profile





def signup(request):
  if request.method == 'POST':
    registration_form = RegistrationForm(request.POST)
    if registration_form.is_valid():
      registration_form.save()
      username = registration_form.cleaned_data.get('username')
      messages.success(request,f'Account for {username} created,you can now login')
      return redirect('login')
  else:
    registration_form = RegistrationForm()
  context = {
    'r_form':registration_form,
  }
  return render(request,'auth/signup.html',context)

@login_required
def homepage(request):
  user = request.user
  n_form = NeighbourhoodCreationForm()
  the_admin = User.objects.get(pk = request.user.id)
  neighbourhood_admin = Admin.objects.filter(neighbourhood_admin = the_admin).first()
  my_hood = Occupant.objects.filter(user_id = user.id).first()
  context = {
    'message':'Am ready to design the application now',
    'n_form':n_form,
    'you_admin':neighbourhood_admin,
    'my_hood':my_hood,
  }
  return render(request,'main/homepage.html',context)

@login_required
def profile(request):
  biz_form = BusinessCreationForm()
  occ_form = OccupantForm()
  the_user = request.user
  the_admin = User.objects.filter(username = the_user.username).first()
  if_admin =  Admin.objects.filter(neighbourhood_admin = the_admin).first()
  get_my_hood = Occupant.objects.get(user = the_user)
  get_my_bizz = Business.objects.filter(owner = get_my_hood).all()
  for biz in get_my_bizz:
    print(biz.owner)
  occ = Occupant.objects.all()
  # print(occ)
  context = {
    'biz_form':biz_form,
    'occ_form':occ_form,
    'admin':str(if_admin),
    'the_user':str(the_user),
    'get_my_hood':get_my_hood,
    'get_my_bizz':get_my_bizz,
  }
  return render(request,'main/profile.html',context)


@login_required
def newHood(request,user_id):
  hood_name = request.POST.get('neighbourhood_name')
  hood_location = request.POST.get('neighbourhood_location')
  hood_logo = request.FILES.get('hood_logo')
  print(hood_logo)
  the_admin = User.objects.get(pk = user_id)
  neighbourhood_admin = Admin(neighbourhood_admin = the_admin)
  neighbourhood_admin.save()
  initial_count = 0
  new_hood  = Neighbourhood.objects.filter(neighbourhood_name = hood_name,neighbourhood_location = hood_location).first()
  if new_hood is not None:
    messages.warning(request,f'NeighbourHood with {hood_name} name in {hood_location} location already exist,search to join the neighbourhood')
  else:
    new_neighbourhood = Neighbourhood(neighbourhood_name = hood_name,neighbourhood_location = hood_location,occupants = initial_count ,neighbourhood_admin = neighbourhood_admin)
    new_neighbourhood.save()
  data = {
    'success':'message received'
  }
  return JsonResponse(data)

@login_required
def newbiz(request,user_id):
  biz_name = request.POST.get('name')
  biz_email = request.POST.get('business_email')
  biz_hood = request.POST.get('business_hood')
  occupant = Occupant.objects.filter(user_id = request.user.id).first()
  # the_hood = Neighbourhood.objects.get()
  user = request.user
  # new_occupant = Occupant(user = user,neighbourhood = the_hood)
  # new_occupant.save()
  new_biz = Business(name = biz_name,owner = occupant,neighbourhood = occupant.neighbourhood,business_email = biz_email)
  new_biz.save()
  data = {
    'success':'message received'
  }
  return JsonResponse(data)

@login_required
def hoods(request):
  hoods = Neighbourhood.objects.all()
  user = Occupant.objects.filter(user_id = request.user.id).first()
  context = {
    'hoods':hoods,
    'userN':str(user),
  }
  return render(request,'main/hoods.html',context)

@login_required
def myhood(request):
  user = request.user
  my_hood = Occupant.objects.filter(user_id = user.id).first()
  other_neighbours = Occupant.objects.filter(neighbourhood_id = my_hood.neighbourhood).all()
  health_form = HealthContactsForm()
  security_form = SecurityContactsForm()
  posts_form = UserPostForm()
  hood = Neighbourhood.objects.get(pk = my_hood.neighbourhood.id)
  health_contacts = Health.objects.filter(neighbourhood = hood).all()
  security_contacts = Security.objects.filter(neighbourhood = hood).all()
  hood_story = Posts.objects.filter(neighbourhood = my_hood.neighbourhood)
  print(hood_story)
  context = {
  # 'you_admin':neighbourhood_admin,
  'other_neighbours':other_neighbours,
  'my_hood':my_hood,
  'health_form':health_form,
  'security_form':security_form,
  'health_contacts':health_contacts,
  'security_contacts':security_contacts,
  'post_form':posts_form,
  'hood_story':hood_story,

  }
  return render(request,'main/myhood.html',context)


@login_required
def joinhood(request,hood_id,user_id):
  new_occupant = User.objects.get(pk = user_id)
  the_hood = Neighbourhood.objects.get(pk = hood_id)
  my_hood = Occupant.objects.filter(user_id = request.user.id).first()
  if my_hood is not None:
    mehood = Occupant.objects.filter(user_id = request.user.id).first()
    mehood.delete()
    save_to = Occupant(user = new_occupant,neighbourhood = the_hood)
    save_to.save()
  else:
    save_to = Occupant(user = new_occupant,neighbourhood = the_hood)
    save_to.save()
  return redirect('myhood')

@login_required
def healthContact(request,hood_id):

  Hname = request.POST.get('Health_center_name')
  Healthphone_number = request.POST.get('Health_center_phone_number')
  Healthaddress = request.POST.get('Health_center_address')
  Healthemail = request.POST.get('Health_center_email')
  hood = Neighbourhood.objects.get(pk = hood_id)
  contact = Health(Health_center_name=Hname,Health_center_phone_number=Healthphone_number,Health_center_address = Healthaddress,Health_center_email=Healthemail,neighbourhood=hood)
  contact.save()

  data = {
  'success':'message received'
  }
  return JsonResponse(data)
  
@login_required
def securityContact(request,hood_id):

  Sname = request.POST.get('Police_station_name')
  Policephone_number = request.POST.get('Police_station_phone_number')
  Policeaddress = request.POST.get('Police_station_address')
  Policeemail = request.POST.get('Police_station_email')
  hood = Neighbourhood.objects.get(pk = hood_id)
  contact = Security(Police_station_name=Sname,Police_station_phone_number=Policephone_number,Police_station_address = Policeaddress,Police_station_email=Policeemail,neighbourhood=hood)
  contact.save()

  data = {
  'success':'message received'
  }
  return JsonResponse(data)

@login_required
def newpost(request,hood_id,user_id):

  title = request.POST.get('title')
  story = request.POST.get('story')
  user = User.objects.get(pk = user_id)
  occupant = Occupant.objects.get(user_id = user_id)
  hood = Neighbourhood.objects.get(pk = hood_id)

  new_post = Posts(title = title , story = story ,user = occupant ,neighbourhood = hood)
  new_post.save()

  data = {
  'success':'message received'
  }
  return JsonResponse(data)

@login_required
def search(request):
  if 'search_term' in request.GET and request.GET["search_term"]:
    search_term = request.GET.get('search_term')
    hoods = Neighbourhood.search_neighbourhood_by_name(search_term)
    users = Profile.search_profile(search_term)
    business = Business.search_business_by_name(search_term)
    health_centers = Health.search_health_centers(search_term)
    security_center = Security.search_security_centers(search_term)
    posts = Posts.search_posts(search_term)
    print(search_term,hoods,users,business,health_centers,security_center,posts)
    context = {
    'hoods':hoods,
    'users':users,
    'business':business,
    'health':health_centers,
    'security':security_center,
    'posts':posts
    }
    return render(request,'main/search.html',context)
  else:
    return render(request,'main/search.html')



