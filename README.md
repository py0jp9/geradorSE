Gerador de Senhas Seguras
Um gerador de senhas feito em Python usando o módulo secrets. Dá pra escolher o tamanho, quantas senhas gerar e quais tipos de caractere usar — maiúsculas, minúsculas, números e especiais.
Funcionalidades

Geração segura com secrets.choice
Garante pelo menos um caractere de cada tipo ativado
Gera várias senhas de uma vez
Fácil de reutilizar em outros projetos

Como funciona
O script pega os tipos de caractere que você ativou, garante um de cada, completa o restante aleatoriamente e embaralha tudo pra não ficar com padrão nenhum.
Como usar
bashpython3 gerador_senhas.py
Por padrão gera 10 senhas de 16 caracteres com maiúsculas, minúsculas e números.
Pra usar em outro arquivo:
pythonfrom gerador_senhas import gerar_senha, gerar_multiplas_senhas

senha = gerar_senha(tamanho=20, usar_especiais=True)
senhas = gerar_multiplas_senhas(quantidade=5, tamanho=12)
Parâmetros
ParâmetroPadrãoO que faztamanho12Tamanho da senhausar_maiusculasTrueInclui letras maiúsculasusar_minusculasTrueInclui letras minúsculasusar_numerosTrueInclui númerosusar_especiaisTrueInclui símbolos especiais
