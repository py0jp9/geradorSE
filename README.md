Gerador de Senhas Seguras

Este projeto é um gerador de senhas seguras feito em Python usando o módulo "secrets", ideal para criação de senhas realmente aleatórias e confiáveis. O código permite configurar tamanho, quantidade e tipos de caracteres que serão utilizados.

Funcionalidades

Gera senhas aleatórias usando o módulo "secrets"

Permite escolher:

Letras maiúsculas

Letras minúsculas

Números

Caracteres especiais

Garante pelo menos um caractere de cada categoria selecionada

Pode gerar várias senhas ao mesmo tempo

Código simples e fácil de reutilizar

Como funciona

O script monta uma lista de categorias de caracteres permitidos.
Depois, ele coloca pelo menos um caractere de cada categoria e preenche o restante da senha com caracteres aleatórios.
Por fim, embaralha para que a ordem não fique previsível.

Instalação

Para usar o projeto, basta clonar o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git

cd seu-repositorio

Como usar

Para rodar o script principal:

python3 gerador_senhas.py

O código irá gerar 10 senhas de 16 caracteres usando letras maiúsculas, minúsculas e números.

Para usar dentro de outro arquivo Python:

from gerador_senhas import gerar_senha, gerar_multiplas_senhas

Uma senha

senha = gerar_senha(tamanho=20, usar_especiais=True)
print(senha)

Várias senhas

senhas = gerar_multiplas_senhas(quantidade=5, tamanho=12)
for s in senhas:
print(s)

Parâmetros

Função gerar_senha(tamanho=12, usar_maiusculas=True, usar_minusculas=True, usar_numeros=True, usar_especiais=True)

tamanho: tamanho da senha
usar_maiusculas: inclui letras maiúsculas
usar_minusculas: inclui letras minúsculas
usar_numeros: inclui números
usar_especiais: inclui símbolos especiais

Segurança

Utiliza secrets.choice, ideal para segurança criptográfica

Embaralha os caracteres antes de retornar a senha

Sempre inclui ao menos um caractere de cada tipo selecionado
