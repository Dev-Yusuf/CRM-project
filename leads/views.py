from django.shortcuts import redirect, render
from .models import Lead, Agent
from .forms import LeadModelForm


# Create your views here.

def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, 'leads/lead_list.html', context)

def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            
            agent = Agent.objects.first()
            lead = Lead.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                age=form.cleaned_data['age'],
                agent=agent
            )
            return redirect("/leads")

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_detail.html", context)


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "leads/update_lead.html", context)
    
