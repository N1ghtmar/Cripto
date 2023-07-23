from pkc import PKC # importa a classe PKC

arquivo = 'hamlet.txt' # coloque o arquivo a ser decriptografado aqui

texto = open(arquivo, 'r') # copia as linhas do texto
linhas = texto.readlines()

cripto = PKC('hamlet') # cria a instância de PKC com a HIGH-KEY = 'hamlet'
cripto.seed_gen() # gera o encription path

f=[]
for linha in linhas:    # criptografa linha por linha
    f.append(f"{cripto.PKC_it(linha[:-1],'unpkc')}\n")  # ele desconsidera o último caractere que seria \n

with open(arquivo,'w',encoding='utf-8') as r:
    r.writelines(f)

# confira se a mensagem foi decriptada corretamente