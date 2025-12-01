import secrets
import string

def gerar_senha(
    tamanho=12,
    usar_maiusculas=True,
    usar_minusculas=True,
    usar_numeros=True,
    usar_especiais=True,
):
    categorias = []
    
    if usar_maiusculas:
        categorias.append(string.ascii_uppercase)
    if usar_minusculas:
        categorias.append(string.ascii_lowercase)
    if usar_numeros:
        categorias.append(string.digits)
    if usar_especiais:
        categorias.append(string.punctuation)
    
    if not categorias:
        raise ValueError("Nenhum tipo de caractere selecionado!")

    # 1) Garante pelo menos um de cada categoria
    senha = [secrets.choice(cat) for cat in categorias]

    # 2) Preenche o resto com todos os caracteres possíveis
    todos_caracteres = "".join(categorias)
    restante = tamanho - len(senha)
    senha.extend(secrets.choice(todos_caracteres) for _ in range(restante))

    # 3) Embaralha para evitar padrão previsível
    secrets.SystemRandom().shuffle(senha)

    return "".join(senha)


def gerar_multiplas_senhas(
    quantidade=5,
    tamanho=12,
    usar_maiusculas=True,
    usar_minusculas=True,
    usar_numeros=True,
    usar_especiais=True,
):
    return [
        gerar_senha(tamanho, usar_maiusculas, usar_minusculas, usar_numeros, usar_especiais)
        for _ in range(quantidade)
    ]


if __name__ == "__main__":
    senhas = gerar_multiplas_senhas(
        quantidade=10,
        tamanho=16,
        usar_maiusculas=True,
        usar_minusculas=True,
        usar_numeros=True,
        usar_especiais=False
    )

    for s in senhas:
        print(s)
