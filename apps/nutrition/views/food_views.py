from django.shortcuts import render, get_object_or_404, redirect
from ..models import SimpleUser
from ..services.recommendation_service import RecommendationService
from ..services.strategy_factory import StrategyFactory


def recommend_food_view(request, user_id):
    user = get_object_or_404(SimpleUser, id=user_id)

    strategy = StrategyFactory.get_strategy(user)
    service = RecommendationService(strategy)

    foods = service.recommend_food(user)

    return render(request, 'recommendation.html', {
        'user': user,
        'foods': foods
    })