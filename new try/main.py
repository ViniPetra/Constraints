from satisfacao_restricoes import Restricao, SatisfacaoRestricoes

'''
class apenas_uma_atribuição(Restricao):
    def __init__ (self, variaveis):
        self.variaveis = variaveis

    def esta_satisfeita(self, atribuicao):
        values = []
        for i in atribuicao.values():
          values.append(i)
        if len(atribuicao) == len(set(values)):
            return True
        else: return False
'''

class ate_dois_turnos(Restricao):
    def __init__ (self, variaveis):
        super().__init__(variaveis)
        self.variaveis = variaveis

    def esta_satisfeita(self, atribuicao):
        values = list(atribuicao.values())
        i = 0
        while i != len(values-2):
            if values[i] == values[i+1] and values[i] == values[i+2]:
                return False
        return True

if __name__ == "__main__":
    variaveis = ['Recepção-T1', 'Limpeza de Quartos-T1', 'Cozinha-T1', 'Serviço de Quarto-T1', 'Bar-T1', 'Lavanderia-T1', 'Manutenção-T1', 'Recepção-T2', 'Limpeza de Quartos-T2',  'Cozinha-T2', 'Serviço de Quarto-T2', 'Bar-T2', 'Lavanderia-T2','Manutenção-T2', 'Recepção-T3',  'Limpeza de Quartos-T3', 'Cozinha-T3', 'Serviço de Quarto-T3', 'Bar-T3', 'Lavanderia-T3', 'Manutenção-T3']
    #variaveis = ['Recepção-T1', 'Recepção-T2', 'Recepção-T3', 'Limpeza de Quartos-T1', 'Limpeza de Quartos-T2', 'Limpeza de Quartos-T3', 'Cozinha-T1', 'Cozinha-T2', 'Cozinha-T3', 'Serviço de Quarto-T1', 'Serviço de Quarto-T2', 'Serviço de Quarto-T3', 'Bar-T1', 'Bar-T2', 'Bar-T3', 'Lavanderia-T1', 'Lavanderia-T2', 'Lavanderia-T3', 'Manutenção-T1', 'Manutenção-T2', 'Manutenção-T3']
    #variaveis = ["Recepção", "Cozinha", "Serviço de Quarto", "Limpeza de Quartos", "Lavanderia", "Manutenção", "Bar"]
    
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

    problema = SatisfacaoRestricoes(variaveis, dominios)

    #problema.adicionar_restricao()
    #problema.adicionar_restricao(apenas_uma_atribuição(variaveis=variaveis))
    problema.adicionar_restricao(ate_dois_turnos(variaveis))

    resposta = problema.busca_backtracking()
    if resposta is None:
        print("Nenhuma resposta encontrada")
    else:
        print(resposta) 
