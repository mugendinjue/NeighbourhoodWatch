from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import date


class Admin(models.Model):
  neighbourhood_admin = models.ForeignKey(User,on_delete=models.CASCADE,related_name='neighbourhood_admin')

  def __str__(self):
    return "%s " % self.neighbourhood_admin

class Neighbourhood(models.Model):
  neighbourhood_name = models.CharField(max_length=100)
  neighbourhood_location = models.CharField(max_length=100)
  occupants = models.IntegerField(blank=True)
  founded_on = models.DateField(auto_now_add=True)
  neighbourhood_admin = models.ForeignKey(Admin,on_delete=models.CASCADE,related_name='admin')
  hood_logo = models.ImageField(default='hood.jpg',upload_to='hoods/')


  # create a new user function
  def create_neighbourhood(self):
    self.save()


  # delete a neighbourhood function
  def delete_neighbourhood(self):
    self.delete()


  # search a neighbourhood by name
  @classmethod
  def search_neighbourhood_by_name(cls,name):
    search_result = cls.objects.filter(neighbourhood_name__icontains = name)
    return search_result

  # search a neighbourhood by location
  @classmethod
  def search_neighbourhood_by_location(cls,location):
    search_result = cls.objects.filter(neighbourhood_location__icontains = location)
    return search_result

  # update the neighbourhood name
  @classmethod
  def update_neigbourhood_name(cls,neighbourhood_update,name):
    update_name = cls.objects.filter(neighbourhood_name = neighbourhood_update).update(neighbourhood_name = name)

  def __str__(self):
    return "%s " % self.neighbourhood_name

# the model class that will register the users
class Occupant(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='the_users')
  neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,related_name='your_neighbourhood')
  is_accepted = models.BooleanField(blank=True,default=False)


  def __str__(self):
    return "%s" % self.user



# the business model
class Business(models.Model):
  name = models.CharField(max_length=100,help_text='Your business name')
  owner = models.ForeignKey(Occupant,on_delete=models.CASCADE,related_name='business_owners')
  neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,related_name='business_neighbourhood')
  business_email = models.EmailField(blank=True,default='business@gmail.com')
  business_hood = models.BooleanField(default=True,help_text='Is your business in the same neighbourhood you are in')



  # function that creates a new business
  def create_business(self):
    self.save()


  # function that deletes a business
  def delete_business(self):
    self.delete()


  # function that searches a business by its name
  @classmethod
  def search_business_by_name(cls,name):
    search_result = cls.objects.filter(name = name).all()
    return search_result

  def __str__(self):
    return "%s " % self.name


# the profile for the users models
class Profile(models.Model):
  profile_pic = models.ImageField(default='default.jpg',upload_to='profile/')
  bio = models.TextField()
  user = models.OneToOneField(User,on_delete = models.CASCADE)
  phone_number = models.IntegerField(default='0700000000',blank=True)
  plot_number = models.CharField(max_length=20)
  occupation = models.CharField(max_length=50,blank=True)


# the receiver that will create the profile for the users on registration
  @receiver(post_save , sender = User)
  def create_profile(instance,sender,created,**kwargs):
    if created:
      Profile.objects.create(user = instance)

  @receiver(post_save,sender = User)
  def save_profile(sender,instance,**kwargs):
    instance.profile.save()


  @classmethod
  def search_profile(cls,username):
    search_result = cls.objects.filter(user__username__icontains = username).all()
    return search_result


  def __str__(self):
    return "%s " % self.user


# the model for contact information
class Health(models.Model):
  Health_center_name = models.CharField(max_length=50)
  Health_center_phone_number = models.IntegerField()
  Health_center_address = models.CharField(max_length=50,blank=True)
  Health_center_email = models.EmailField(blank=True)
  neighbourhood = models.OneToOneField(Neighbourhood,on_delete=models.CASCADE,related_name='health_details')


# the receiver that will create the health model for the neighbourhood on creaation
  @receiver(post_save,sender=Neighbourhood)
  def create_health(instance,sender,created,**kwargs):
    if created:
      Health.objects.create(neighbourhood = instance)

  @receiver(post_save,sender=Neighbourhood)
  def save_health(sender,instance,**kwargs):
    instance.health.save()



  @classmethod
  def search_health_centers(cls,search_term):
    search_result = cls.objects.filter(Health_center_name__icontains = search_term)
    return search_result



  def __str__(self):
    return "%s " % self.Health_center_name


# the security department
class Security(models.Model):
  Police_station_name = models.CharField(max_length=50)
  Police_station_phone_number = models.IntegerField()
  Police_station_address = models.CharField(max_length=50,blank=True)
  Police_station_email = models.EmailField(blank=True)
  neighbourhood = models.OneToOneField(Neighbourhood,on_delete=models.CASCADE,related_name='security_details')


# the receiver that will create the security model for the neighbourhood on creaation
  @receiver(post_save,sender=Neighbourhood)
  def create_security(instance,sender,created,**kwargs):
    if created:
      Security.objects.create(neighbourhood = instance)

  @receiver(post_save,sender=Neighbourhood)
  def save_security(sender,instance,**kwargs):
    instance.security.save()



  @classmethod
  def search_security_centers(cls,search_term):
    search_result = cls.objects.filter(Police_station_name__icontains = search_term)
    return search_result


  def __str__(self):
    return "%s " % self.Police_station_name


class Posts(models.Model):
  '''
  This class will contain the raising issues in the neighborhood (posts and info)
  '''
  title = models.CharField(max_length=30)
  story = models.TextField()
  user = models.ForeignKey(Occupant,on_delete=models.CASCADE)
  neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
  posted_on = models.DateTimeField(auto_now_add=True,null=True)


  # search method for posts
  @classmethod
  def search_posts(cls,search_term):
    search_result = cls.objects.filter(title__icontains = search_term)
    return search_result



  def __str__(self):
    return f'{self.title} story from {self.neighbourhood.neighbourhood_name} neighbourhood'
