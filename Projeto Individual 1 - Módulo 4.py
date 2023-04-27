"""[M4] Projeto Individual 1.ipynb

Aquivo original localizado em https://colab.research.google.com/drive/1mFGP0FHfaQgOELY90s0pBHNfVIHPGyp-?usp=sharing

##################################################################
#  SENAC/RESILIA - Formação em Análise de Dados (FAD)            #
#  Projeto Individual 1 - Módulo 4 - Relatórios Semanais         #
#  !/usr/bin/env python3                                         #
#  -*- coding: utf-8 -*-                                         #
#  Criado por: Douglas Klem Portugal do Amaral                   #
#  Data de criação: 26/04/2023                                   #
#  versão = '3.11(64-bits)'                                      #
##################################################################
#
## Contexto
#
Uma determinada loja deseja produzir relatórios semanais com ganhos e despesas. O gerente da loja te contratou para gerar um relatório de uma semana 
para mostrar ao dono da loja como a análise dos dados pode ser útil para eles. Para isso, ele te enviou uma tabela de exemplo das despesas de uma semana:

|Dia        |Limpeza  |Comida  |Transporte  |Outros |
| --------- | ------- |------- |----------- |------ |
|Segunda    |100      |221.60  |150         |0      |
|Terça      |0        |375.31  |100         |0	    |
|Quarta     |100      |412.00  |125         |2310   |
|Quinta     |0        |495.20  |300         |500    |
|Sexta      |100      |411.53  |275         |0	    |
|Sábado     |100      |245.00  |525         |0	    |
|Domingo    |0        |164.00  |75          |820    |

Além disso, ele informou que os ganhos não estão nessa planilha, mas que ele possui a seguinte lista: 2200, 2420.50, 3391, 5322, 4898.50, 4200, 3893
respectivos aos dias da semana. Ele te deixou bem livre para incluir no relatório as estatísticas que desejar, mas ele deseja que o relatório contenha
outros dados que veremos a seguir:

## Dados para o Relatório

Gerar um relatório de uma semana para mostrar ao dono da loja como a análise dos dados pode ser útil e incluir outros itens:

* A subtração de impostos dos ganhos diários, que nesta semana foi de 7%;
* A soma total dos ganhos;
* A média semanal dos ganhos;
* A soma total das despesas por categoria;
* A média semanal de todas as despesas;
* O lucro diário para informar qual dia foi mais lucrativo e o lucro total da semana;
* Uma organização com textos explicando o que foi feito para obter os valores e os resultados bem apresentados.

## Plano de Ação

1. Criação de um *dataframe* para a tabela de despesas fornecida pelo gerente;
2. Adição da coluna com os valores de ganhos fornecidos;
3. Adição de colunas com dados estratégicos;
4. Adição de colunas com informações detalhadas de acordo com a seção *Dados para o Relatório*;
5. *Insight* dos resultados finais.
"""

#realizando a importação da biblioteca necessária à execução do projeto (Pandas)
import pandas as pd

#[1]
#criação do dataframe inicial
despesas = {'Dia': ['Segunda', 'Terça', 'Quarta', 'Quinta','Sexta','Sábado','Domingo'],
            'Limpeza': [100,0,100,0,100,100,0],
            'Comida': [221.60,375.31,412.00,495.20,411.53,245.00,164.00],
            'Transporte': [150,100,125,300,275,525,75],
            'Outros': [0,0,2310,500,0,0,820]}            
desp = pd.DataFrame(despesas, index = [1,2,3,4,5,6,7])
print(desp)

#[2]
#adição da coluna 'Ganhos' ao dataframe anterior; cada linha dessa coluna informa o ganho bruto do dia em questão
desp['Ganhos']=[2200, 2420.50, 3391, 5322, 4898.50, 4200, 3893]
print(desp)

"""[3] Adição de dados estratégicos:
- Seguro Locação;
- Softwares e Sistemas;
- Taxas Bancárias;
- Folha de Pagamento dos Colaboradores;
- Aluguel do Imóvel;
- Contas de Água, Energia e Telefone/Internet.

NOTA: no registro de dados para o cálculo de lucros e despesas de uma empresa, as adições acima são normalmente realizadas de forma mensal; no entanto,
para fins de comparação com a tabela de gastos contida no projeto, foram utilizados valores fictícios diários para a semana em questão.

[Referências: ](https://)https://www.serasa.com.br/limpa-nome-online/blog/despesas-fixas-entenda-o-que-sao/
"""

#[3] adição de novas colunas ao dataframe anterior
#Seguro Locação (valor do seguro estimado em cima do valor do aluguel)
desp['Seg_Loc']=[50,50.5,50,50,60,55,55.5] 
#Softwares e Sistemas (assinatura mensal estimada em torno de $500,00)
desp['Soft_Sys']=[16,16,16.5,16,17,16.5,18]
#Taxas Bancárias (taxa mensal estimada em torno de 29,90/mês)
desp['Banco_Tax']=[0.9,1.2,1,1,1,0.9,1]
#Folha de Pagamento dos Colaboradores (salário estimado em $1500,00 por colaborador)
desp['Colab']=[150,155,150,150,160,155,170]
#Aluguel do Imóvel (estimativa em um imóvel com valorização aproximada de $200000,00 com aluguel de 1% mensal em cima desse valor)
desp['Alug']=[50,50.5,50,50,60,55,55.5]
#Contas de Água, Energia e Telefone/Internet (valores estimados em planos oferecidos para uma locação suburbana no centro comercial)
desp['Água']=[5,3.9,3.4,5,5,5.5,5.5]
desp['Energia']=[60,60,66.6,65,60,66,65]
desp['Comunic']=[5,5.5,4.5,4,4,5.5,5]
#
print(desp)

#[4]
#adição de outros dados detalhados requeridos pelo gerente:
#subtração de impostos dos ganhos diários (7% nessa semana)
desp['Ganhos_Imp_Descont'] = desp['Ganhos']-0.07*(desp['Ganhos'])
print(desp)

#soma total dos ganhos
print('*'*90)
total_ganhos=desp['Ganhos'].sum() #soma considerando os ganhos brutos
print(f'A soma total dos ganhos brutos durante a semana é de ${"{:.2f}".format(total_ganhos)}.')
total_ganhos_imp=desp['Ganhos_Imp_Descont'].sum() #soma considerando os ganhos descontados de impostos
print(f'A soma total dos ganhos com desconto de impostos durante a semana é de ${"{:.2f}".format(total_ganhos_imp)}.')
print('*'*90)

#média semanal dos ganhos
print('*'*90)
media_ganhos=desp['Ganhos'].mean() #média considerando os ganhos brutos
print(f'A média semanal dos ganhos brutos é de ${"{:.2f}".format(media_ganhos)}.')
media_ganhos_imp=desp['Ganhos_Imp_Descont'].mean() #média considerando os ganhos descontados de impostos
print(f'A média semanal dos ganhos com desconto de impostos é de ${"{:.2f}".format(media_ganhos_imp)}.')
print('*'*90)

#soma total das despesas por categoria
print('*'*90)
#despesas no escopo do projeto
total_limpeza=desp['Limpeza'].sum() #custo total de limpeza na semana
total_aliment=desp['Comida'].sum() #custo total de alimentação na semana
total_transp=desp['Transporte'].sum() #custo total com transportes na semana
total_outros=desp['Outros'].sum() #custo total catalogado em 'outros' na semana
#despesas estratégicas
total_segloc=desp['Seg_Loc'].sum() #custo total com seguro locação na semana
total_softsys=desp['Soft_Sys'].sum() #custo total com o sistema da loja na semana
total_bancotax=desp['Banco_Tax'].sum() #custo total para manutenção da conta bancária PJ na semana
total_colab=desp['Colab'].sum() #custo total para a renda dos colaboradores na semana
total_alug=desp['Alug'].sum() #custo total para locação do imóvel na semana
total_agua=desp['Água'].sum() #custo total com a conta de água na semana
total_energia=desp['Energia'].sum() #custo total com a conta de energia na semana
total_comunic=desp['Comunic'].sum() #custo total com os planos de internet e telefonia na semana
#
print(f'Dentre as despesas registradas, houveram os seguintes gastos totais para a semana:')
print(f'${total_limpeza} com limpeza,')
print(f'${total_aliment} com alimentação,')
print(f'${total_transp} com transporte,')
print(f'${total_outros} com outras despesas,')
#
print(f'${total_segloc} com seguro-locação,')
print(f'${total_softsys} com o sistema da loja,')
print(f'${total_bancotax} com a manutenção da conta bancária,')
print(f'${total_colab} para a renda dos colaboradores,')
print(f'${total_alug} com a locação do imóvel,')
print(f'${total_agua} com a conta de água,')
print(f'${total_energia} com a conta de energia,')
print(f'${total_comunic} com os planos de telefonia e internet.')
print('*'*90)

#média semanal de todas as despesas
print('*'*90)
media_desp=(desp['Limpeza'].mean())+(desp['Comida'].mean())+(desp['Transporte'].mean())+(desp['Outros'].mean()+
            desp['Seg_Loc'].mean())+(desp['Soft_Sys'].mean())+(desp['Banco_Tax'].mean())+(desp['Colab'].mean()+
            desp['Alug'].mean())+(desp['Água'].mean())+(desp['Energia'].mean())+(desp['Comunic'].mean())
print(f'A média semanal de todas as despesas ficou em torno de ${"{:.2f}".format(media_desp)}.')
print('*'*90)

#lucro diário para informar qual dia foi mais lucrativo e o lucro total da semana
#(a fórmula para calcular é: lucro real = ganho bruto – custos)
#(bônus: informar, também, o dia menos lucrativo da semana)
print('*'*90)
lucro_diario=desp['Ganhos_Imp_Descont']-(desp['Limpeza']+desp['Comida']+desp['Transporte']+desp['Outros']+
            desp['Seg_Loc']+desp['Soft_Sys']+desp['Banco_Tax']+desp['Colab']+desp['Alug']+desp['Água']+desp['Energia']+desp['Comunic'])
desp['Lucro_Diário'] = lucro_diario #adiciona uma coluna de lucros diários ao dataframe
#forma final do dataframe para o relatório
print(desp)
#variáveis de lucro máximo, mínimo e total durante a semana, respectivamente
print('*'*90)
lucro_max=desp['Lucro_Diário'].max()
lucro_min=desp['Lucro_Diário'].min()
lucro_total=desp['Lucro_Diário'].sum()
#método idxmax e idxmin para poder relacionar os valores de lucro com os dias da semana e usá-los no display
idmax = desp['Lucro_Diário'].idxmax()
idmin = desp['Lucro_Diário'].idxmin()
diamaxluc=desp.loc[idmax,'Dia']
diaminluc=desp.loc[idmin,'Dia']
print(f'Durante a semana, o dia mais lucrativo foi {diamaxluc}, enquanto que o menos')
print(f'lucrativo foi {diaminluc}; houve um lucro total de ${"{:.2f}".format(lucro_total)}.')
print('*'*90)

"""## *Insights* Finais

> Com a prospecção dos dados anteriores, pode-se perceber a importância de uma análise de dados bem executada para a gestão de custos dentro de uma empresa.

> As consultas dentro do *dataframe* permitem, por exemplo, visualizar potenciais FUROS DE DESPESAS ou planejar investimentos para um mês SEM ESTOURAR O ORÇAMENTO disponível ou prazos de execução de tarefas. Vejamos os exemplos abaixo:

* EXEMPLO 1: "Na posição de gerente, preciso saber se os lucros semanais estão bem encaminhados para atingir a meta do mês através do método 50-30-20, onde:
>- 50% é para despesas fixas;
>- 30% é para despesas flexíveis;
>- 20% são para reservas de emergência ou fundos de investimento."

No escopo apresentado, é possível fazer uma projeção a partir dos lucros semanais:
"""

#lucro total da semana, considerando todas as despesas registradas
print('*'*90)
print(f'Lucro da Semana: ${"{:.2f}".format(lucro_total)}.')
#definindo uma função onde é fornecido o valor estimado para as reservas financeiras da loja
#para uma projeção final de mês onde o total bruto adquirido seria de 250000.00, pelo método anteriormente descrito:
def meta(valormeta=50000.00):
  if (4*lucro_total)<valormeta:
    return f"A META DO MÊS NÃO FOI ATINGIDA! Faltam ${valormeta-(4*lucro_total)} para atingir nosso objetivo."
  return f"A META DO MÊS FOI ATINGIDA! Teremos um lucro de ${((4*lucro_total)-valormeta).round(2)} acima do estipulado. Parabéns!"
print(f'Lucro estimado do Mês: ${4*lucro_total}.')
print(meta(valormeta))
print('*'*90)

""" * EXEMPLO 2: "Tendo conhecimento do dia da semana onde houve o menor lucro registrado, preciso destacar esses dados para procurar algum ponto fora da tangente."
"""

#acesso dos dados referentes à quarta-feira através do índice
print('*'*30)
display(desp.iloc[2])
print('*'*30)

"""Acima, fica visível que no mesmo dia em que houveram despesas elevadas catalogadas em 'Outros', o lucro diário foi negativo. Isso permite iniciar planos de ação para, por exemplo, ampliar as categorias de despesas afim de ter um maior controle dos gastos arbitrários (esse 'outros' foi quebra/roubo de insumo? Ou foi outra coisa?).

* EXEMPLO 3: "Será que os ganhos brutos dessa quarta-feira estavam dentro do esperado e o fator determinante para o lucro negativo foi somente devido às despesas de caráter mais nebuloso?"
"""

#comparações entre valores:
print('*'*90)
print('GANHO BRUTO:',desp['Ganhos'][3]) #ganho bruto de quarta-feira
print('MÉDIA DOS GANHOS:',(desp['Ganhos'].mean().round(2))) #média de ganhos na semana
print('MEDIANA DOS GANHOS:',(desp['Ganhos'].median())) #valor mediano entre os ganhos da semana
print('*'*90)
print(desp.loc[(desp['Ganhos']>3000)&(desp['Lucro_Diário']>0)]) #ganhos brutos superiores a 3000.00 
print('*'*90)                                                   #onde não houveram lucros negativos

"""Com as impressões acima, temos condições de extrair as informações necessárias e observar que apesar de estar num valor levemente abaixo das médias de ganho bruto, o valor de quarta-feira não foi determinante para o lucro indesejado. Assim, é possível direcionarmos os esforços para tratar desses ruídos no planejamento de gastos de forma mais efetiva e precisa.

---
"""
