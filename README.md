# Sistema de Validação e Relatório Acadêmico

Este script em Python valida dados acadêmicos de alunos, calcula médias e exibe um relatório formatado sobre a situação de cada um.

## 🚀 Funcionalidades

* **Validação de Dados:** Verifica se as notas estão no intervalo de $0.0$ a $10.0$ e se a frequência está entre $0.0$ e $1.0$ ($0\%$ a $100\%$).

* **Cálculo de Média:** Média aritmética simples das notas fornecidas.

* **Regras de Negócio:**

  * **Aprovado:** Frequência $\ge 75\%$ e Média $\ge 7.0$

  * **Recuperação:** Frequência $\ge 75\%$ e $5.0 \le \text{Média} < 7.0$

  * **Reprovado por Nota:** Frequência $\ge 75\%$ e Média $< 5.0$

  * **Reprovado por Frequência:** Frequência $< 75\%$

* **Relatório no Terminal:** Exibe os resultados e aponta falhas nos dados de forma alinhada.

## 📋 Pré-requisitos

* Python 3.x

## 🔧 Como Executar

```
python main.py

```

## 📊 Exemplo de Saída

```
NOME            | MÉDIA  | FREQ.  | SITUAÇÃO / AVISOS

```

Ana             | 8.2    |   90% | APROVADO 
Bruno           | N/A    | N/A    | ⚠️ AÇÃO NECESSÁRIA \[Nota inválida (-5.0)\]