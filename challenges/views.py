from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string


monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Walk for at least 20 minutes everyday!",
    "march": "Learn Python for atleast 30 minutes a day",
    "april": "fast for atleast 2 weeks",
    "may": "fast for atleast 2 weeks",
    "june": "fast for atleast 2 weeks",
    "july": "Learn Python for atleast 30 minutes a day",
    "august": "Learn Python for atleast 30 minutes a day",
    "september": "Learn Python for atleast 30 minutes a day",
    "october": "Learn Python for atleast 30 minutes a day",
    "november": "Eat no meat for the entire month",
    "december": "Eat no meat for the entire month"
}

# Create your views here.


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
          
        return render(request,"challenges/challenge.html",{
            "text" : challenge_text,
            "month_name" : month.capitalize()
        })
    except:
        raise Http404


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        
        return HttpResponseNotFound("<h1>Invalid month</h1>")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge",args=[redirect_month])

    return HttpResponseRedirect(redirect_path)

def home_page(request):
    months = list(monthly_challenges.keys())
    
    return render(request,"challenges/index.html",{
        "months":months
    })
    