from django import template

register = template.Library()


@register.filter
def stars_rating(rating):
    return range(1, rating + 1)
