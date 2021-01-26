from unittest import TestCase
from .bibliotheque import fonction2,moyenne,ecart_type
class MoyenneTestCase(TestCase):

  def test_exemple(self): #Votre test a vous.
    assert fonction2() == 2

  def test_moyenne_111(self):
    assert moyenne([1,1,1]) == 1
  
  def test_ecart_111(self):
    assert ecart_type([1,1,1]) == 0 
