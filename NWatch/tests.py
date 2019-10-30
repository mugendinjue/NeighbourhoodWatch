from django.test import TestCase
from .models import Neighbourhood,Admin,Business,Occupant
from django.contrib.auth.models import User



class TestNeighbourhoodModel(TestCase):
  '''
  test class for our the neighbour model
  '''
  def setUp(self):
    '''
    the startup class of the class
    '''
    self.new_user = User(username = 'Denis')
    self.new_user.save()
    self.new_admin = Admin(neighbourhood_admin = self.new_user)
    self.new_admin.save()
    self.new_neighbourhood = Neighbourhood(neighbourhood_name = 'blessed-court',neighbourhood_location = 'Syokimau',occupants = '22', founded_on = '2019/20/20',neighbourhood_admin = self.new_admin)

# test for checking the instance of a class
  def test_instance(self):
    self.assertTrue(isinstance(self.new_neighbourhood,Neighbourhood))


# test for creating a new neighbourhood
  def test_create_neighbourhood(self):
    self.new_neighbourhood.create_neighbourhood()
    all_neighbourhoods = Neighbourhood.objects.all()
    self.assertTrue(len(all_neighbourhoods) > 0)

# test for deleting a neighbourhood
  def test_delete_neighbourhood(self):
    self.new_neighbourhood.create_neighbourhood()
    self.new_neighbourhood.delete_neighbourhood()
    all_neighbourhoods = Neighbourhood.objects.all()
    self.assertEqual(len(all_neighbourhoods),0)


# test for searching a neighbourhood by name
  def test_search_neighbourhood_by_name(self):
    self.new_neighbourhood.create_neighbourhood()
    self.new_user = User(username = 'doe')
    self.new_user.save()
    self.new_admin = Admin(neighbourhood_admin = self.new_user)
    self.new_admin.save()
    self.another_neighbourhood = Neighbourhood(neighbourhood_name = 'new_block',neighbourhood_location = 'Dubai',occupants = '2002', founded_on = '2019/10/30',neighbourhood_admin = self.new_admin)
    self.another_neighbourhood.create_neighbourhood()
    search_result = Neighbourhood.search_neighbourhood_by_name('new_block')
    self.assertEqual(len(search_result),1)


# test for searching a neighbourhood by location
  def test_search_neighbourhood_by_location(self):
    self.new_neighbourhood.create_neighbourhood()
    self.new_user = User(username = 'doe')
    self.new_user.save()
    self.new_admin = Admin(neighbourhood_admin = self.new_user)
    self.new_admin.save()
    self.another_neighbourhood = Neighbourhood(neighbourhood_name = 'new_block',neighbourhood_location = 'Dubai',occupants = '2002', founded_on = '2019/10/30',neighbourhood_admin = self.new_admin)
    self.another_neighbourhood.create_neighbourhood()
    search_result = Neighbourhood.search_neighbourhood_by_location('Syokimau')
    self.assertEqual(len(search_result),1)


# test for updating a neighbourhood name
  def test_update_a_neighbourhood(self):
    # self.new_neighbourhood.create_neighbourhood()
    # Neighbourhood.update_neigbourhood_name('new_block','rich_town')
    # search_results = Neighbourhood.search_neighbourhood_by_name('rich_town')
    # self.assertEqual(len(search_results),1)
    pass

# test for updating occupants
  def test_update_an_occupant(self):
    pass




class TestBusinessModels(TestCase):
  '''
  test classs that test the business model and its functions
  '''
  def setUp(self):
    '''
    the functions that runs at the begin of the test
    '''
    self.new_user = User(username = 'Denis')
    self.new_user.save()
    self.new_admin = Admin(neighbourhood_admin = self.new_user)
    self.new_admin.save()
    self.new_neighbourhood = Neighbourhood(neighbourhood_name = 'blessed-court',neighbourhood_location = 'Syokimau',occupants = '22', founded_on = '2019/20/20',neighbourhood_admin = self.new_admin)
    self.new_neighbourhood.create_neighbourhood()
    self.new_occupant = Occupant(user = self.new_user,neighbourhood = self.new_neighbourhood,is_accepted = True)
    self.new_occupant.save()
    self.new_business = Business(name = 'denisWarehouse',owner = self.new_occupant,neighbourhood = self.new_neighbourhood,business_email = 'family@gmail.com' )

# test the instance of the business model
  def test_business_instance(self):
    self.assertTrue(isinstance(self.new_business,Business))

# test for creating a business
  def test_create_a_business(self):
    self.new_business.create_business()
    all_business = Business.objects.all()
    self.assertTrue(len(all_business) > 0)


# test for deleting a business
  def test_delete_a_business(self):
    self.new_business.create_business()
    self.new_business.delete_business()
    all_business = Business.objects.all()
    self.assertEqual(len(all_business),0)


# test for searching for a business
  def test_search_for_business(self):
    self.new_business.create_business()
    self.new_user = User(username = 'doe')
    self.new_user.save()
    self.new_admin = Admin(neighbourhood_admin = self.new_user)
    self.new_admin.save()
    self.new_occupant = Occupant(user = self.new_user,neighbourhood = self.new_neighbourhood,is_accepted = True)
    self.new_occupant.save()
    self.another_business = Business(name = 'denisButchery',owner = self.new_occupant,neighbourhood = self.new_neighbourhood,business_email = 'fam@gmail.com' )
    self.another_business.create_business()
    search_result =Business.search_business_by_name('denisButchery')
    self.assertEqual(len(search_result),1)


#test for updating a business
  def test_update_a_business(self):
    pass