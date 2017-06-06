# compactador_de_arquivos
### __Projeto PEE - Script criado em Linux/Python 2.7.__
####__Programa recebe como input um determinado arquivo e retorna como output um arquivo csv contendo informações sobre a compactação do arquivo de input__

### __Sobre o codigo:__
Instruções:
Para que o código funcione é preciso alterar em sua fonte os caminhos a serem utilizados durante sua execução.

Arquivos:
-Trocar o caminho especificado no "dictarquivo" dos scripts(rar.py, targz.py, zip.py), para o caminho onde está localizado o arquivo a ser compactado

CSV:
-Trocar o caminho especificado na função "open()" dos scripts "rar.py", "targz.py", "zip.py", para o caminho onde o arquivo csv será criado.
-Trocar o caminho especificado na função "csv_creator()" do script "get_file_csv.py", para o caminho onde o arquivo csv será criado.
 
### __O CSV gerado pelo script contem:__

-User-time

-System-time

-Elapsed-time

-CPU%

-Compacted-file-size
