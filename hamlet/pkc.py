# BenderInvestimentos 2023© todos os direitos reservados

# Este é o código do Procedural-key Criptography
# Ele utiliza da biblioteca random para gerar um caminho de encriptação procedural
# A partir de duas chaves, uma maior e outra menor (HIGH-KEY e LOW-KEY)

class PKC:  # define a instâcia da classe
    def __init__(self, h_key, l_key=0): # a H-KEY é de um tipo str para ser utilizada no metodo seed
        self.l_key = l_key
        self.h_key = h_key
    
    def seed_gen(self): # Aqui é a base da criptografia
        from random import seed
        from random import shuffle
        from string import printable
        seed(self.h_key)    # ele usa a H-KEY para definir uma seed para toda thread do código
                            # assim, sempre que você usar a seed definida,
                            # vai obter o mesmo resultado pelos metodos da biblioteca random
        self.e_path = list(printable[:-5]+'áéóíúÁÉÓÍÚàèòìùÀÒÈÌÙôêâîûÔÂÎÛÊãõÃÕ')  
                                            # aqui ele pega todos os caracteres printavéis do python e 
        shuffle(self.e_path)                # cria uma lista embaralhando ele
                                            # basicamente o que fazemos a seguir é só uma simples
                                            # cifra de césar utilizando a L-KEY como parametro

    def __str__(self):  # função só para printar os argumentos usados
        return f"high-key: [{self.h_key}]\nlow-key: [{self.l_key}]\nencription path: [{self.e_path}]"
    
    def change_l(self,nl):  # caso queira mudar a L-KEY durante a execução
        self.l_key = nl
    
    def PKC_it(self, m, mode='pkc'):  # função principal para a encriptação e decriptação
        enc = ''                      # ele recebe uma mensagem e um modo para (en/de)criptação
        for l in range(len(m)):       # indo de letra em letra
            for p in range(len(self.e_path)):   # ele acha a posição dela na lista de caracteres embaralhados o e_path
                if m[l] == self.e_path[p]:      # achando a o indice da letra por exemplo M = 45
                    if mode == 'pkc':
                        cod = p + l + self.l_key + len(m)   # aqui vai a cifra de césar
                                                            # o funcionamento é interessante, já que não é só a L-KEY que afeta
                                                            # ele soma a posição da letra na mensagem, o tamanho da mensagem,
                                                            # a L-KEY e por último o indice da letra no e_path
                                                # então, se a mensagem a ser criptografada fosse AMOR e L-KEY = 2
                                                # a letra M iria avançar 2 + 4 + 2 + indice dela no e_path 
                                                # sendo trocada por exemplo, por &
                        while cod > len(self.e_path) - 1:   # o e_path tem 100 caracteres
                            cod -= len(self.e_path)         # por isso essa soma as vezes pode ultrapassar o indice máximo
                        enc += self.e_path[cod]             # assim o código estabiliza essa soma e acha o indice certo pra ela
                        break
                    elif mode == 'unpkc':                   
                        cod = p - l - self.l_key - len(m)   # a única diferença para a decriptação
                        while cod < 0:                      # é que em vez de somar, diminui
                            cod += len(self.e_path)
                        enc += self.e_path[cod]
                        break
        return enc  # no fim, ele retorna a mensagem (en/de)criptada
    
    # algumas ressalvas
    # mesmo que alguém ache ter a HIGH-KEY, se ela não descobrir a LOW-KEY
    # pode se levar a crer que a H-KEY está errada, assim dando uma segurança a mais a mensagem

    # a chance de alguém ter o mesmo encription path que você é de 1/(100!)%, então não se preocupe
    # guarde bem a HIGH-KEY, embora tenha a LOW-KEY, como já disse, ela só é um pequeno metodo de segurança
