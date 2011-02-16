from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from subscription.forms import SubscriptionForm
from subscription.models import Subscription


def new(request):
    form = SubscriptionForm()
    context = RequestContext(request, {'form': form})
    return render_to_response('subscription/new.html', context)

def create(request):
    form = SubscriptionForm(request.POST)
    if not form.is_valid():
        context = RequestContext(request, {'form': form})
        return render_to_response('subscription/new.html', context)
    subscription = form.save()
    return HttpResponseRedirect(reverse('subscription:success', args=[ subscription.pk ]))

def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def success(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    context = RequestContext(request, {'subscription': subscription})
    
    send_mail(subject=u'Inscricao no eventex', message=u'Obrigado por se inscrever no eventex!', from_email='contato@eventex.com', recipient_list=[ subscription.email ],)
        
    return render_to_response('subscription/success.html', context)
