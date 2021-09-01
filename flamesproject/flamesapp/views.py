from django.shortcuts import render
from flamesapp.forms import flames
# Create your views here.
def first(request):
    form = flames()
    if request.method == "POST":
        form = flames(request.POST)
        if form.is_valid():
            name1 = form.cleaned_data['your_name']
            name2 = form.cleaned_data['your_partner']

            namestr = name1 + name2
        for c in namestr:
            if namestr.count(c) != 1:
            # counting common letters
                namestr = namestr.replace(c,"")
        number = len(namestr) % 6
        # number to move through FLAMES
        rel = ""
        if number == 1:
            rel += "Friends"
        elif number == 2:
            rel += "Love"
        elif number == 3:
            rel += "Affection"
        elif number == 4:
            rel += "Marriage"
        elif number == 5:
            rel += "Enemy"
        elif number == 0:
            rel += "Siblings"
        else:
            pass
        if rel == "Friends":
            return render(request,'friends.html',{'relation':rel})
        elif rel == "Love":
            return render(request,'love.html',{'relation':rel})
        elif rel == "Affection":
            return render(request,'affection.html',{'relation':rel})
        elif rel == "Marriage":
            return render(request,'marriage.html',{'relation':rel})
        elif rel == "Enemy":
            return render(request,'enemy.html',{'relation':rel})
        elif rel == "Siblings":
            return render(request,'siblings.html',{'relation':rel})
        
    return render(request,'index.html',{'form':form})