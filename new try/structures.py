
'''
funcionarios = {
    "João": ["Recepção", "Limpeza de Quartos"],
    "Maria": ["Cozinha", "Serviço de Quarto", "Bar"],
    "Ana": ["Recepção", "Lavanderia"],
    "Carlos": ["Limpeza de Quartos", "Manutenção"],
    "Bruno": ["Cozinha", "Serviço de Quarto"],
    "Paula": ["Recepção", "Limpeza de Quartos", "Bar"],
    "Pedro": ["Manutenção", "Limpeza de Quartos"],
    "Luiza": ["Lavanderia", "Limpeza de Quartos"],
    "Thiago": ["Cozinha", "Bar"],
    "Fernanda": ["Recepção", "Lavanderia", "Serviço de Quarto"],
    "Rafael": ["Cozinha", "Serviço de Quarto", "Bar"],
    "Juliana": ["Recepção", "Limpeza de Quartos"],
    "Caio": ["Manutenção", "Limpeza de Quartos"],
    "Beatriz": ["Recepção", "Limpeza de Quartos", "Serviço de Quarto"],
    "Lucas": ["Manutenção", "Limpeza de Quartos", "Bar"],
    "Bruna": ["Cozinha", "Serviço de Quarto"],
    "Marcelo": ["Recepção", "Limpeza de Quartos", "Lavanderia"],
    "Vanessa": ["Cozinha", "Bar"],
    "Danilo": ["Manutenção", "Limpeza de Quartos"],
    "Renata": ["Recepção", "Serviço de Quarto", "Bar"]
}
'''

'''
{
    'Recepção': ['João', 'Ana', 'Paula', 'Fernanda', 'Juliana', 'Beatriz', 'Marcelo', 'Renata'],
    'Limpeza de Quartos': ['João', 'Carlos', 'Paula', 'Pedro', 'Luiza', 'Juliana', 'Beatriz', 'Lucas', 'Marcelo', 'Danilo'],
    'Cozinha': ['Maria', 'Bruno', 'Thiago', 'Bruna', 'Vanessa'],
    'Serviço de Quarto': ['Maria', 'Bruno', 'Paula', 'Fernanda', 'Rafael', 'Beatriz', 'Renata'],
    'Bar': ['Maria', 'Paula', 'Thiago', 'Rafael', 'Lucas', 'Vanessa'],
    'Lavanderia': ['Ana', 'Luiza', 'Fernanda', 'Marcelo'],
    'Manutenção': ['Carlos', 'Pedro', 'Danilo']
}
'''
'''
variaveis = ["João", "Maria", "Ana", "Carlos", "Bruno", "Paula", "Pedro", "Luiza", "Thiago", "Fernanda", "Rafael", "Juliana", "Caio", "Beatriz", "Lucas", "Bruna", "Marcelo", "Vanessa", "Danilo", "Renata"]
'''
'''
for variavel in variaveis:
    dominios[variavel] = ["Recepção", "Cozinha", "Serviço de Quarto", "Limpeza de Quartos", "Lavanderia", "Manutenção", "Bar"]
'''
'''
dominios = {
    'Recepção-T1': ['Fernanda', 'Ana', 'Renata', 'Paula', 'João', 'Beatriz', 'Juliana', 'Marcelo'],
    'Limpeza de Quartos-T1': ['Carlos', 'Beatriz', 'Pedro', 'Luiza', 'Danilo', 'Paula', 'Lucas', 'João', 'Juliana', 'Marcelo'],
    'Cozinha-T1': ['Maria', 'Bruno', 'Thiago', 'Bruna', 'Vanessa'],
    'Serviço de Quarto-T1': ['Maria', 'Bruno', 'Paula', 'Fernanda', 'Rafael', 'Beatriz', 'Renata'],
    'Bar-T1': ['Maria', 'Paula', 'Thiago', 'Rafael', 'Lucas', 'Vanessa'],
    'Lavanderia-T1': ['Ana', 'Luiza', 'Fernanda', 'Marcelo'],
    'Manutenção-T1': ['Carlos', 'Pedro', 'Danilo'],
    'Recepção-T2': ['Fernanda', 'Ana', 'Renata', 'Paula', 'João', 'Beatriz', 'Juliana', 'Marcelo'],
    'Limpeza de Quartos-T2': ['Carlos', 'Beatriz', 'Pedro', 'Luiza', 'Danilo', 'Paula', 'Lucas', 'João', 'Juliana', 'Marcelo'],
    'Cozinha-T2': ['Maria', 'Bruno', 'Thiago', 'Bruna', 'Vanessa'],
    'Serviço de Quarto-T2': ['Maria', 'Bruno', 'Paula', 'Fernanda', 'Rafael', 'Beatriz', 'Renata'],
    'Bar-T2': ['Maria', 'Paula', 'Thiago', 'Rafael', 'Lucas', 'Vanessa'],
    'Lavanderia-T2': ['Ana', 'Luiza', 'Fernanda', 'Marcelo'],
    'Manutenção-T2': ['Carlos', 'Pedro', 'Danilo'],
    'Recepção-T3': ['Fernanda', 'Ana', 'Renata', 'Paula', 'João', 'Beatriz', 'Juliana', 'Marcelo'],
    'Limpeza de Quartos-T3': ['Carlos', 'Beatriz', 'Pedro', 'Luiza', 'Danilo', 'Paula', 'Lucas', 'João', 'Juliana', 'Marcelo'],
    'Cozinha-T3': ['Maria', 'Bruno', 'Thiago', 'Bruna', 'Vanessa'],
    'Serviço de Quarto-T3': ['Maria', 'Bruno', 'Paula', 'Fernanda', 'Rafael', 'Beatriz', 'Renata'],
    'Bar-T3': ['Maria', 'Paula', 'Thiago', 'Rafael', 'Lucas', 'Vanessa'],
    'Lavanderia-T3': ['Ana', 'Luiza', 'Fernanda', 'Marcelo'],
    'Manutenção-T3': ['Carlos', 'Pedro', 'Danilo']
}
'''
#variaveis = ['Recepção-T1', 'Recepção-T2', 'Recepção-T3', 'Limpeza de Quartos-T1', 'Limpeza de Quartos-T2', 'Limpeza de Quartos-T3', 'Cozinha-T1', 'Cozinha-T2', 'Cozinha-T3', 'Serviço de Quarto-T1', 'Serviço de Quarto-T2', 'Serviço de Quarto-T3', 'Bar-T1', 'Bar-T2', 'Bar-T3', 'Lavanderia-T1', 'Lavanderia-T2', 'Lavanderia-T3', 'Manutenção-T1', 'Manutenção-T2', 'Manutenção-T3']
    

'''
dominios =  {
    'Recepção': ['João', 'Ana', 'Paula', 'Fernanda', 'Juliana', 'Beatriz', 'Marcelo', 'Renata'],
    'Limpeza de Quartos': ['João', 'Carlos', 'Paula', 'Pedro', 'Luiza', 'Juliana', 'Beatriz', 'Lucas', 'Marcelo', 'Danilo'],
    'Cozinha': ['Maria', 'Bruno', 'Thiago', 'Bruna', 'Vanessa'],
    'Serviço de Quarto': ['Maria', 'Bruno', 'Paula', 'Fernanda', 'Rafael', 'Beatriz', 'Renata'],
    'Bar': ['Maria', 'Paula', 'Thiago', 'Rafael', 'Lucas', 'Vanessa'],
    'Lavanderia': ['Ana', 'Luiza', 'Fernanda', 'Marcelo'],
    'Manutenção': ['Carlos', 'Pedro', 'Danilo']
}
'''

#variaveis = ['Recepção-T1', 'Recepção-T2', 'Recepção-T3', 'Limpeza de Quartos-T1', 'Limpeza de Quartos-T2', 'Limpeza de Quartos-T3', 'Cozinha-T1', 'Cozinha-T2', 'Cozinha-T3', 'Serviço de Quarto-T1', 'Serviço de Quarto-T2', 'Serviço de Quarto-T3', 'Bar-T1', 'Bar-T2', 'Bar-T3', 'Lavanderia-T1', 'Lavanderia-T2', 'Lavanderia-T3', 'Manutenção-T1', 'Manutenção-T2', 'Manutenção-T3']
#variaveis = ["Recepção", "Cozinha", "Serviço de Quarto", "Limpeza de Quartos", "Lavanderia", "Manutenção", "Bar"]
    