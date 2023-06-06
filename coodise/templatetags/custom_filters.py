from django import template

register = template.Library()


@register.filter(name="idFriendly")
def idFriendly(value):
    """Remove chars not suitable fod id element."""
    safe = str(value)
    bannedChars = """ .'",#&@^<>:;()"""
    for char in bannedChars:
        safe = safe.replace(char, "_")
    return safe


@register.filter(name="htmlFriendly")
def htmlFriendly(value):
    """Replace HTML tags with &; alternatives."""
    safe = str(value)
    safe = safe.replace("<", "&lt;")
    safe = safe.replace(">", "&gt;")
    safe = safe.replace("\t", "    ")
    return safe.replace(" ", "&nbsp;")


@register.filter(name="tabsToSpaces")
def tabsToSpaces(value):
    """Replace HTML tags with &; alternatives."""
    safe = str(value)
    return safe.replace("\t", "    ")
