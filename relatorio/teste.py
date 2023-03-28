from relatorio.models import Sistema

sistema = Sistema.query.filter(Sistema.codigo == 1)

print(sistema)