Gerador de Senhas Seguras
Gerador de senhas em Python usando o módulo secrets. Permite definir tamanho, quantidade e quais tipos de caracteres usar — maiúsculas, minúsculas, números e especiais.
Funcionalidades

Geração criptograficamente segura com secrets.choice
Garante pelo menos um caractere de cada categoria ativada
Gera várias senhas de uma vez
Código simples e fácil de reutilizar em outros projetos

Como funciona
O script monta a lista de categorias ativas, força um caractere de cada uma, preenche o restante aleatoriamente e embaralha tudo para que a ordem não fique previsível.

Como usar
bashpython3 gerador_senhas.py
Por padrão gera 10 senhas de 16 caracteres com maiúsculas, minúsculas e números.
Para usar em outro arquivo:
pythonfrom gerador_senhas import gerar_senha, gerar_multiplas_senhas

senha = gerar_senha(tamanho=20, usar_especiais=True)
senhas = gerar_multiplas_senhas(quantidade=5, tamanho=12)
Parâmetros de gerar_senha
ParâmetroPadrãoDescriçãotamanho12Tamanho da senhausar_maiusculasTrueInclui letras maiúsculasusar_minusculasTrueInclui letras minúsculasusar_numerosTrueInclui númerosusar_especiaisTrueInclui símbolos especiais
