from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Learn python'},
    {'id': 2, 'name': 'Learn c++', }
]


def home(request):
  return render(request, 'base/home.html', {'rooms': rooms})


def room(request, pk):
  for room in rooms:
    print(room)
    if room['id'] == int(pk):
      break
  context = {'room': room}
  return render(request, 'base/room.html', context)
