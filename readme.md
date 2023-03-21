### Descrição do problema

Suponha que o hotel precisa alocar seus funcionários em diferentes turnos para garantir que todas as tarefas sejam executadas adequadamente durante o dia. Existem várias tarefas que precisam ser realizadas, incluindo recepção, limpeza de quartos, manutenção, cozinha, entre outras.

Existem 20 funcionários disponíveis, cada um com habilidades específicas em uma ou mais tarefas, e o hotel precisa decidir qual funcionário atribuir a cada turno de trabalho. Cada turno tem uma duração fixa de 8 horas e o hotel está aberto 24 horas por dia.

As restrições a serem satisfeitas incluem:
1.  Cada turno deve ter pelo menos um funcionário alocado.
2.  Cada funcionário pode trabalhar em no máximo dois turnos consecutivos.
3.  Cada funcionário só pode ser alocado para um turno que corresponda às suas habilidades.
4.  O número de funcionários alocados para cada turno deve ser suficiente para concluir todas as tarefas necessárias.

Funcionário | Tarefa
----|----
João | Recepção, Limpeza de Quartos
Maria | Cozinha, Serviço de Quarto, Bar
Ana | Recepção, Lavanderia
Carlos | Limpeza de Quartos, Manutenção
Bruno | Cozinha, Serviço de Quarto
Paula | Recepção, Limpeza de Quartos, Bar
Pedro | Manutenção, Limpeza de Quartos
Luiza | Lavanderia, Limpeza de Quartos
Thiago | Cozinha, Bar
Fernanda | Recepção, Lavanderia, Serviço de Quarto
Rafael | Cozinha, Serviço de Quarto, Bar
Juliana | Recepção, Limpeza de Quartos
Caio | Manutenção, Limpeza de Quartos
Beatriz | Recepção, Limpeza de Quartos, Serviço de Quarto
Lucas | Manutenção, Limpeza de Quartos, Bar
Bruna | Cozinha, Serviço de Quarto
Marcelo | Recepção, Limpeza de Quartos, Lavanderia
Vanessa | Cozinha, Bar
Danilo | Manutenção, Limpeza de Quartos
Renata | Recepção, Serviço de Quarto, Bar

As habilidades são:
Bar, Limpeza de Quartos, Cozinha, Lavanderia, Manutenção e Serviço de Quarto.

O objetivo é encontrar uma alocação de funcionários que atenda a todas as restrições e minimize o número total de funcionários necessários para cobrir todos os turnos.

### Modelagem

Este é um problema de Satisfação de restrições
Para resolução desse problema, é necessário tomar algumas decisões para modelar o problema. 

O hotel funciona 24 horas por dia e cada turno dura 8 horas. Uma vez que o hotel não fecha, não importa qual turno no dia o funcionário vai assumir, apenas se satisfaz à restrição o mesmo não está em dois turnos seguidos

Como temos 3 informações (Funcionário, Habilidade e Turno), temos que abstrair o problema de forma que duas dessas informações representem uma coisa só. Para este problema, foi assumido que Habilidade e Turno serão mesclados pois assim será possível definir **Habilidade/Turno** como **Variável** e **Funcionário** como **Domínio**. Para esclarecer melhor, uma (habilidade em um turno) assumirá o valor de um funcionário, contanto que o mesmo tenha a habilidade. 

As variáveis deste problema foram definidas como o nome da função + T(um número de turno).

Para os domínios, foi criado um dicionário com o nome de cada habilidade/Turno e os funcionários que as possuem.

Foram implementadas duas restrições. Uma valida de o funcionário está alocado em até dois turnos consecutivos e a outra valida se o mesmo funcionário não está alocado em mais de uma função no mesmo turno.

## Conclusão

Este código chegou na resposta:

|            Funções      |   T1     |   T2     |  T3     |
|------------------------|:--------|:--------|:--------|
| Recepção               | Fernanda | Fernanda | Ana     |
| Limpeza de Quartos     | Carlos   | Carlos   | Beatriz |
| Cozinha                | Maria    | Maria    | Bruno   |
| Serviço de Quarto      | Bruno    | Paula    | Maria   |
| Bar                    | Paula    | Thiago   | Paula   |
| Lavanderia             | Ana      | Ana      | Luiza   |
| Manutenção             | Pedro    | Pedro    | Carlos  |

