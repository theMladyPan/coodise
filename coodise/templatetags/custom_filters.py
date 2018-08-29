from django import template

register = template.Library()

@register.filter(name="idFriendly")
def idFriendly(value):
    safe=str(value)
    bannedChars=""" .'","""
    for char in bannedChars:
        safe = safe.replace(char,"_")
    return safe
