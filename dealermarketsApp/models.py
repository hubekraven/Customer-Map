from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# models that olds information for a Dealer and returns the dealer label.
@python_2_unicode_compatible
class Dealer(models.Model):
    dealer_label = models.CharField(max_length = 50)
    dealer_url = models.CharField(max_length = 200)
    dealer_addresse = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.dealer_label
    
#models that olds information for a client and returns the client first and last name
@python_2_unicode_compatible
class Client (models.Model):
    dealer_id = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    client_firstName = models.CharField(max_length = 50)
    client_lastName = models.CharField(max_length = 50)
    client_address =models.CharField(max_length = 100)
    client_PostCod = models.CharField(max_length = 7)
    client_email = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.client_firstName + ' '+ self.client_lastName

