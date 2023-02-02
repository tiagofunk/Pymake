# Pymake

Ferramenta em python que se assemelha a ferramenta [make](https://www.gnu.org/software/make/) para a compilação de projeto C/C++ de várias pastas e arquivos.

Ele tem a intenção de permitir a compilação sem complexidade de comandos do make.

# Como usar

Abra o arquivo pymake.py e edite as seguinte variaveis:
- ```FILES_DIR```: indica a raiz do projeto.
- ```COMPILER```: indica o compilador que você quer usar.
- ```ARGUMENTS```: são os argumentos padrão para compilar cada arquivo.
- ```PROGRAM_NAME```: nome do executável que vai ser gerado.
- ```files_arguments_exceptions```: indica quais arquivos tem argumentos especiais (eles são adicionados aos argumentos padrão). Se nao tiver nenhum, deixar vazio.

O arquivo ```pygame.py``` deste repositório já contém uma configuração de exemplo para compilar os arquivos C++ na pasta ```src``` .

Depois é só executar o arquivo ```pymake.py``` e ele vai gerar o arquivo executável na raiz do projeto.
