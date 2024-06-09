from django.shortcuts import render, redirect
from .utils import *

def home(request):
    return render(request, 'system-html/index.html')

def search(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        player_id = convert_nickname_id(nickname)
        
        if player_id:
            return redirect('search_results', player_id=player_id)
        else:
            return render(request, 'system-html/search.html', {'error': 'The player could not be found.'})
    
    return render(request, 'system-html/search.html')

def search_results(request, player_id):
    user_data = get_data(player_id)
    
    if user_data:
        context = {
            'nickname': user_data['name'],
            'description': user_data.get('description', 'No description available'),
            'display_name': user_data['displayName'],
            'created': user_data['created'],
            'is_banned': user_data['isBanned'],
            'id': user_data['id'],
            'avatar_url': user_data['avatar_url']
        }
    else:
        context = {'error': 'Could not get player information.'}
    
    return render(request, 'system-results/results.html', context)
