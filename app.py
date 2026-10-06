def validar_aluno(aluno):
    """Verifica se os dados do aluno estão corretos antes de processar."""
    erros = []
    
    # Valida as notas (devem estar entre 0.0 e 10.0)
    notas = aluno.get("notas", [])
    for nota in notas:
        if not (0.0 <= nota <= 10.0):
            erros.append(f"Nota inválida encontrada ({nota}).")
            break  # Um erro já invalida o cálculo seguro
            
    # Valida a frequência (deve estar entre 0% e 100%, ou seja, 0.0 e 1.0)
    frequencia = aluno.get("frequencia", 0.0)
    if not (0.0 <= frequencia <= 1.0):
        erros.append(f"Frequência inválida ({frequencia * 100}%).")
        
    return erros


def calcular_media(notas):
    """Calcula a média de uma lista de notas."""
    return sum(notas) / len(notas) if notas else 0.0


def determinar_status(media, frequencia):
    """Retorna a situação do aluno com base na média e frequência."""
    if frequencia < 0.75:
        return "REPROVADO POR FREQUÊNCIA"
    elif media >= 7.0:
        return "APROVADO"
    elif media >= 5.0:
        return "RECUPERAÇÃO"
    else:
        return "REPROVADO POR NOTA"


def gerar_relatorio_turma(turma):
    """Exibe o relatório e sinaliza dados pendentes ou incorretos."""
    print(f"\n{'NOME':<15} | {'MÉDIA':<6} | {'FREQ.':<6} | SITUAÇÃO / AVISOS")
    print("-" * 65)
    
    for aluno in turma:
        nome = aluno.get("nome", "Sem Nome")
        erros = validar_aluno(aluno)
        
        # Se houver inconsistências nos dados, exibe o aviso
        if erros:
            aviso = " [ERRO DE DADOS: " + ", ".join(erros) + "]"
            print(f"{nome:<15} | {'N/A':<6} | {'N/A':<6} | ⚠️ AÇÃO NECESSÁRIA{aviso}")
        else:
            media = calcular_media(aluno["notas"])
            status = determinar_status(media, aluno["frequencia"])
            freq_percentual = aluno["frequencia"] * 100
            
            print(f"{nome:<15} | {media:<6.1f} | {freq_percentual:>4.0f}% | {status}")


# --- Teste com Dados Válidos e Incorretos ---
turma = [
    {"nome": "Ana", "notas": [8.5, 7.0, 9.0], "frequencia": 0.90},
    {"nome": "Bruno", "notas": [-5.0, 12.0, 6.0], "frequencia": 0.80},  # Nota inválida
    {"nome": "Carla", "notas": [9.0, 8.5], "frequencia": 1.50},         # Frequência inválida
    {"nome": "Diego", "notas": [3.0, 2.0, 4.0], "frequencia": 0.85},     # Dados ok
]

gerar_relatorio_turma(turma)