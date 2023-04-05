from django.template.defaulttags import register


@register.filter
def get_dict_item(target_dict, coluna):
    registros = target_dict.__dict__
    if coluna in registros.keys():
        valor = registros[coluna]
    else:
        valor = target_dict.__getattribute__(coluna).__str__()
    return valor
