from django.http import HttpResponseRedirect
from portfolio.forms import SwitchClientForm
import logging

logger = logging.getLogger(__name__)

def switch_client(request):
    if request.method == 'POST':
        form = SwitchClientForm(request.POST)
        if form.is_valid():
            client = form.cleaned_data['client']
            profile = request.user.get_profile()
            profile.client = client
            profile.save()
    return HttpResponseRedirect('/admin/portfolio/')