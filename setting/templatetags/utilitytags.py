from django.template import Library

register = Library()

def toint(value:float) -> int:
    try:
        return int(value)
    except:
        return 0
def tofloat(value:int) -> float:
    try:
        return float(value)
    except:
        return 0

register.filter("toint",toint)
register.filter("tofloat",tofloat)