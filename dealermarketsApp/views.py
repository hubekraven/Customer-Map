from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .forms import DealerSelectForm

from .models import Dealer, Client

# define the index view. Make a request on the Dealer model dealers and return the list of all the dealers
# in the dealer view
class IndexView(generic.ListView):  
    template_name = 'dealermarkets/index.html'
    context_object_name = 'dealers_list'
	
    def get_queryset(self):
        """ define the index view.Return the list of all the dealers in the dealer view """
        form = DealerSelectForm()
        return Dealer.objects.order_by('pk')
#def index(request):
##dealers_list= Dealer.objects.order_by('pk')
#dealers_list = Dealer.objects.all()
#context = { 
#	'dealers_list': dealers_list
#}
#return render(request,'dealermarkets/index.html', context)

#define a delear market. Make a request with the selected option on the Client model and 
# return of the list of all the clients of a dealer
class ResultsView(generic.DetailView):
    model = Dealer
    template_name = 'dealermarkets/result.html'
    
	#y:
	#clients = Client.objects.filter(dealer_id = id_dealer)
	#context = { 
	#	'clients_list': clients_list
	#}
	#cept Dealer.DoesNotExist:
	#raise Http404("Ooops! this dealer does not exist")
	#turn render(request, 'dealermarkets/result.html', context )
	