from django.shortcuts import render, redirect
from ..forms.user_form import SimpleUserForm

def create_user_view(request):
    if request.method == 'POST':
        form = SimpleUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(f'/recommend/{user.id}/')
    else:
        form = SimpleUserForm()

    return render(request, 'create_user.html', {'form': form})
