def get_average_rating(games_obj):
    rating_sum = sum([float(g.rating) for g in games_obj])
    return rating_sum / games_obj.count()