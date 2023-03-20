from satisfacao_restricoes import Restricao, SatisfacaoRestricoes

def funcoes_atendidas(atribuicao_turno, funcoes, habilidades_funcionarios):
    funcoes_presentes = set()
    for funcionario in atribuicao_turno:
        funcoes_presentes.update(habilidades_funcionarios[funcionario])
    return set(funcoes).issubset(funcoes_presentes)

class RestricaoTarefas(Restricao):
    def __init__(self, turno, funcoes):
        super().__init__([turno])
        self.turno = turno
        self.funcoes = funcoes

    def esta_satisfeita(self, atribuicao, habilidades_funcionarios):
        if self.turno not in atribuicao:
            return True
        atribuicao_turno = atribuicao[self.turno]
        return funcoes_atendidas(atribuicao_turno, self.funcoes, habilidades_funcionarios) and not trabalhando_turnos_consecutivos(atribuicao_turno)

def trabalhando_turnos_consecutivos(funcionario, atribuicao):
    turnos_funcionario = [turno for turno, funcionarios in atribuicao.items() if funcionario in funcionarios]
    turnos_funcionario.sort()
    for i in range(len(turnos_funcionario) - 1):
        if turnos_funcionario[i + 1] - turnos_funcionario[i] == 1:
            return True
    return False


class RestricaoTarefas(Restricao):
    def __init__(self, turno, tarefas):
        super().__init__([turno])
        self.turno = turno
        self.tarefas = tarefas

    def esta_satisfeita(self, atribuicao):
        if self.turno not in atribuicao:
            return True
        funcionarios_turno = atribuicao[self.turno]
        tarefas_turno = set()
        for funcionario in funcionarios_turno:
            tarefas_turno.update(habilidades_funcionarios[funcionario])
            if trabalhando_turnos_consecutivos(funcionario, atribuicao):
                return False
        return set(self.tarefas).issubset(tarefas_turno)

# Restrição 1: Cada turno deve ter pelo menos um funcionário alocado.
class Restricao1(Restricao):
    def __init__(self, variaveis):
        self.variaveis = variaveis

    def esta_satisfeita(self, atribuicao):
        for variavel in self.variaveis:
            if atribuicao.get(variavel) is None:
                return False
        return True

# Restrição 2: Cada funcionário pode trabalhar em no máximo dois turnos consecutivos.
class Restricao2(Restricao):
    def __init__(self, variavel1, variavel2):
        super().__init__([variavel1, variavel2])
        self.variavel1 = variavel1
        self.variavel2 = variavel2

    def esta_satisfeita(self, atribuicao):
        if self.variavel1 not in atribuicao or self.variavel2 not in atribuicao:
            return True
        return atribuicao[self.variavel1] != atribuicao[self.variavel2]

# Restrição 3: Cada funcionário só pode ser alocado para um turno que corresponda às suas habilidades.
class Restricao3(Restricao):
    def __init__(self, variavel, valor):
        super().__init__([variavel])
        self.variavel = variavel
        self.valor = valor

    def esta_satisfeita(self, atribuicao):
        if self.variavel not in atribuicao:
            return True
        return atribuicao[self.variavel] == self.valor

# Restrição 4: O número de funcionários alocados para cada turno deve ser suficiente para concluir todas as tarefas necessárias.
class Restricao4(Restricao):
    def __init__(self, variaveis, tarefas):
        self.variaveis = variaveis
        self.tarefas = tarefas

    def esta_satisfeita(self, atribuicao):
        funcionarios = [atribuicao[v] for v in self.variaveis if atribuicao.get(v) is not None]
        return len(funcionarios) >= len(self.tarefas)

class RestricaoHabilidades(Restricao):
    def __init__(self, funcionario, habilidades):
        super().__init__([funcionario])
        self.funcionario = funcionario
        self.habilidades = habilidades

    def esta_satisfeita(self, atribuicao):
        if self.funcionario not in atribuicao:
            return True
        return atribuicao[self.funcionario] in self.habilidades

if __name__ == "__main__":
    variaveis = ["João", "Maria", "Ana", "Carlos", "Bruno", "Paula", "Pedro", "Luiza", "Thiago", "Fernanda", "Rafael", "Juliana", "Caio", "Beatriz", "Lucas", "Bruna", "Marcelo", "Vanessa", "Danilo", "Renata"]
    dominios = {}
    # Dica: o domínio pode ser String, inteiro, Dicionário ou objetos
    for variavel in variaveis:
        dominios[variavel] = ["Recepção", "Cozinha", "Serviço de Quarto", "Limpeza de Quartos", "Lavanderia", "Manutenção", "Bar"]
    
    problema = SatisfacaoRestricoes(variaveis, dominios)


    # Restrição 1: Cada turno deve ter pelo menos um funcionário alocado.
    turno1 = ["João", "Ana", "Paula", "Fernanda", "Juliana", "Beatriz", "Marcelo", "Renata"]
    problema.adicionar_restricao(Restricao1(turno1))

    turno2 = ["Maria", "Bruno", "Thiago", "Lucas", "Bruna", "Vanessa"]
    problema.adicionar_restricao(Restricao1(turno2))

    turno3 = ["João", "Carlos", "Pedro", "Luiza", "Caio", "Danilo"]
    problema.adicionar_restricao(Restricao1(turno3))

    # Restrição 2: Cada funcionário pode trabalhar em no máximo dois turnos consecutivos.
    for i in range(len(variaveis)-2):
        problema.adicionar_restricao(Restricao2(variaveis[i], variaveis[i+1]))
        problema.adicionar_restricao(Restricao2(variaveis[i], variaveis[i+2]))

    # Restrição 3: Cada funcionário só pode ser alocado para um turno que corresponda às suas habilidades.
    for v in variaveis:
        habilidades = dominios[v]
        problema.adicionar_restricao(Restricao3(v, habilidades))

    # Restrição 4: O número de funcionários alocados para cada turno deve ser suficiente para concluir todas as tarefas necessárias.
    tarefas_turno1 = ["Recepção", "Limpeza de Quartos", "Lavanderia"]
    problema.adicionar_restricao(Restricao4(turno1, tarefas_turno1))

    tarefas_turno2 = ["Cozinha", "Serviço de Quarto", "Bar"]
    problema.adicionar_restricao(Restricao4(turno2, tarefas_turno2))

    tarefas_turno3 = ["Limpeza de Quartos", "Manutenção"]
    problema.adicionar_restricao(Restricao4(turno3, tarefas_turno3))

    habilidades_funcionarios = {
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

    for funcionario, habilidades in habilidades_funcionarios.items():
        problema.adicionar_restricao(RestricaoHabilidades(funcionario, habilidades))

    #problema.adicionar_restricao()

    resposta = problema.busca_backtracking()
    if resposta is None:
        print("Nenhuma resposta encontrada")
    else:
        print(resposta) 

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