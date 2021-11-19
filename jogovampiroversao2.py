# Abaixo esta o import time para criar um suspense na cena 3 do personagem Bob.
import time
# Variáveis iniciais
escolha_jogador = ''
personagem_jogador = ''
#função inicio do jogo = escolhas de personagens
def main():     
    print('____________________________________________________\n')
    print('                                                      ')
    print('     ▀█████████▄     ▄████████     ███                       ')
    print('       ███    ███   ███    ███ ▀█████████▄                   ')
    print('       ███    ███   ███    ███    ▀███▀▀██                   ')
    print('      ▄███▄▄▄██▀    ███    ███     ███   ▀       ')
    print('     ▀▀███▀▀▀██▄  ▀███████████     ███    ')
    print('       ███    ██▄   ███    ███     ███  ')
    print('       ███    ███   ███    ███     ███    ')
    print('     ▄█████████▀    ███    █▀     ▄████▀     ')
    print('                                                      ')
    print('   ▄██████▄     ▄████████   ▄▄▄▄███▄▄▄▄      ▄████████ ')
    print('  ███    ███   ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███ ')
    print('  ███    █▀    ███    ███ ███   ███   ███   ███    █▀  ')
    print(' ▄███          ███    ███ ███   ███   ███  ▄███▄▄▄    ')
    print('▀▀███ ████▄  ▀███████████ ███   ███   ███ ▀▀███▀▀▀    ')
    print('  ███    ███   ███    ███ ███   ███   ███   ███    █▄ ')
    print('  ███    ███   ███    ███ ███   ███   ███   ███    ███ ')
    print('  ████████▀    ███    █▀   ▀█   ███   █▀    ██████████ ')
    print('                                                      ')
    print('____________________________________________________\n\n')
    escolha_personagem = int (input('Eu gosto de surpresas... escolha 1, 2 ou 3 e descubra quem és\n\n' ))
    if (escolha_personagem == 1):
        print('Você se chama Vlad, você é um Vampiro misterioso... Você é muito ambicioso...\n')
        cena1_vlad()
    elif (escolha_personagem == 2):
        print('Você está confusa... Tudo que consegue lembrar e que acordou em um lugar estranho.\nVocê está procurando por Vlad! Você grita, grita de novo e nada! Você é Vampira está com uma sede de sangue fresco.\n')
        cena1_lilith()
    elif (escolha_personagem == 3):
        print('Bob... aaah, que coisa estranha... Seu pescoço deve estar dolorido em...\n')
        cena1_Bob()
    else:
        print('Por favor releia o que eu te peço, escolha uma opção válida.\n')
        main()



###########################################################################################
#  função para fim de jogo e deseja tentar novamente?

def game_over():
    resposta_jogador =  (input('Você perdeu.\nDeseja jogar novamente [S/N]? ')).upper()
    if (resposta_jogador == 'S'):
        main()
    else: 
        print('Ok, então. Bye bye!')
        

#############################################################################################        
# função para Vitória do jogo

def trofeu (): 
    jogador_ganhou = (input('Você Ganhou.\nDeseja jogar novamente [S/N]? ')).upper()
    if (jogador_ganhou == 'S'):
        main()
    else: 
        print('Ok, então. Até a próxima!')


############################################################################################
#função tratamento das condições usadas nas cenas


def numero_verificar(entrada):
    if entrada.isnumeric():
        return int(entrada)
    else:
        return 30

#############################################################################################

def cena1_vlad():
    salao_vlad = (input('Você se encontra em um mezanino, as paredes são muito altas...\nTem uma escadaria toda de madeira quebrada a sua frente! Você esta olhando para baixo...\nSerá que você consegue descer...?\n\nPor favor digite um número de 1 a 20\n'))
    salao_vlad = numero_verificar(salao_vlad)
    print('____________________________________________________\n')
    if (salao_vlad <= 15):
        print ('\nVocê pisou em uma armadilha...\nvocê teve a "grande sorte" de cair em um porão cheio de estacas...\nTente novamente em outra história, isto é... se tiver coragem kkkk...\n')
        game_over()
    elif (salao_vlad >= 16 and salao_vlad <= 20):
        print('\nVocê pisou em uma armadilha, o seu instinto vampírico falou mais alto!\nVocê se  transformou em morcego e desceu até o andar de baixo. Foi por pouco em...\n')
        cena2_vlad()
    else:
        print('\nPor favor releia o que eu te peço, escolha uma opção válida ou vai virar churrasquinho.\n')
        cena1_vlad()



def cena2_vlad():
    quarto_vlad = (input('\nVocê escuta um grito e vai ao quarto para descobrir sua origem...\nVocê ainda não adentrou no quarto.\nVocê não consegue ver muito bem mesmo ativando sua visão vampírica...\nNa porta você identifica desenhado a giz branco o que se parece com uma operação de matematica incompleta...\nPor um breve momento de loucura, insanidade você acredita que se resolver essa charada você conseguiria sair dessa ileso!\n\nEscolha um número de 1 a 20\n'))
    quarto_vlad = numero_verificar(quarto_vlad)
    print('____________________________________________________\n')
    if (quarto_vlad <= 15):
        print ('\nSeria você o Leopoldo Nachbin? kkk Não, com certeza não! Mas Vlad você foi muito esperto nessa...\nSerá que na próxima terá a mesma sorte?\n')
        cena3_vlad()
    elif (quarto_vlad >= 16 and quarto_vlad <= 20):
        print('\nTava no caminho certo Vlad, mas você tropeçou e para não bater a cara no chão se apoiou-se em uma estatua de pedra adentro do quarto...\nE adivinha? Você ativou a armadilha da fome! Você virou um churrasquinho bem passado!\nMais cuidado se houver uma próxima vez...\n')
        game_over()
    else:
        print('\nPor favor releia o que eu te peço, escolha uma opção válida.\n')
        cena2_vlad()



def cena3_vlad():
    misterio_vlad = (input('Você conseguiu ativar sua visão vampírica e conseguiu visualizar a parte de dentro da sala!\nNo canto direito você uma passagem estreita. Você chega mais perto e avista um brilho intenso.\nVocê fica se perguntando o que será esta coisa que tem um brilho tão misterioso...\nPor fim você decide verificar o que é!\n\nEscolha um número de 1 a 20!\n'))
    misterio_vlad = numero_verificar(misterio_vlad)
    print('____________________________________________________\n')
    if (misterio_vlad <= 15):
        print ('Você não é um gato, mas a sua curiosidade te fez ativar uma armadilha no meio da passagem!\nVocê tomou um tiro de bala de prata na testa!\n')
        game_over()
    elif (misterio_vlad >= 16 and misterio_vlad <= 20):
        print('Você consegue passar com sucesso para o outro lado e encontra um báu aberto, com moedas de ouro transbordando!\nParabéns você é o Vampíro mais rico do momento!\n')
        trofeu ()
    else:
        print('Por favor releia o que eu te peço, escolha uma opção válida.\n')
        cena3_vlad()


#############################################################################  
# cenas jogadas se for com a personagem Lillith  

def cena1_lilith():
    biblioteca_lilith = (input('Você esta em uma biblioteca.\nParece que ninguem usa este local, pois está todo empoeirado e cheio de teias de aranhas!\nVocê ao andar pelos corredores percebe que cada prateleira tem um número.\n\nEscolha um número de 1 a 20!\n'))
    biblioteca_lilith = numero_verificar(biblioteca_lilith)
    print('____________________________________________________\n')
    if (biblioteca_lilith <= 15):
        print ('Você pega um livro que chamou sua atenção. O livro escolhido era todo entalhado com ouro\ne pedras preciosas, porém não tinha nenehuma descrição na capa.\nAo abrir o livro você descobre que ele é na verdade uma Bíblia sagrada.\nUma luz misteriorsa sai de dentro da Biblia e você é transformado em pó!\n')
        game_over()
    elif (biblioteca_lilith >= 16 and biblioteca_lilith <= 20):
        print('No momento em que você retira o livro da prateleira abre-se uma passagem secreta.\n')
        cena2_lilith()
    else:
        print('Por favor releia o que eu te peço, escolha uma opção válida.\n')
        cena1_lilith()
    

def cena2_lilith():
    sala_secreta_lilith = (input('Ao entrar na passagem secreta, você começa analisar o local.\nTem uma mesa redonda com 20 lugares para se sentar localiazada ao centro da sala.\n\nEscolha um número de 1 a 20!\n'))
    sala_secreta_lilith = numero_verificar(sala_secreta_lilith)
    print('____________________________________________________\n')
    if (sala_secreta_lilith <= 15):
        print ('No momento que você se senta você escuta um barulho vindo de longe.\nQuando você pensa em desviar já era tarde de mais.\nQuando você sentou-se foi ativado uma armadilha e 3 flechas sagradas acertaram você em cheio!.\n')
        game_over()
    elif (sala_secreta_lilith >= 16 and sala_secreta_lilith <= 20):
        print('ta quase la em')
        cena3_lilith()
    else:
        print('Por favor releia o que eu te peço, escolha uma opção válida.\n')
        cena2_lilith()


def cena3_lilith():
    misterio_lilith = (input('Quando você se senta a mesa começa a girar e aos poucos vai se tornando uma escada espiral para o subsolo.\nAlgumas tochas iluminam o seu caminho...\nAo final da escada você econtra um humano desacordado em cima de uma mesa.\nFaminta, você não pensou duas vezes e deu o bote,  mordeu o pescoço do jovem sugando cada gota de sangue.\n\nEscolha um número de 1 a 20!\n'))
    misterio_lilith = numero_verificar(misterio_lilith)
    print('____________________________________________________\n')
    if (misterio_lilith <= 15):
        print ('Achou que ia matar sua fome né? Você tentou! Sua sede de sangue foi tão grande que não percebeu que o rapaz deitado era um Paladino,\n consigo possuia objetos sagrados que te enfraqueceu.\nE pra completar no meio de sua tentativa de saciar sua fome,\nele acordou de seu transe e te apunhalou pelas costas com uma adaga que estava próximo ao seu corpo.\n')
        game_over ()
    elif (misterio_lilith >= 16 and misterio_lilith <= 20):
        print('Com muita cautela você saciou toda sua fome com sucesso.\nDepois você encontrou no bolso da calça do corpo adormecido do rapaz instruções de um tesouro perdido.\nGood luck!\n')
        trofeu ()
    else:
        print('Por favor releia o que eu te peço, escolha uma opção válida.\n')
        cena3_lilith()

######################################################################################################
# cenas jogadas caso seja com o personagem Bob

def cena1_Bob():
    salao_Bob = (input('A vida não é facil né Bob.\nVocê acabo de acordar em um lugar estranho. Você se sente fraco.\nVocê aos poucos vai se levantando...\nQuanto você se levanta você percebe que cai um papel no chão. Quando você pega o papel você encontra a seguinte mensagem:\nVocê agora é um vampíro agora, tera sede de sangue eternamente!\nhaha Lide com isso! Desesperado você corre em buscas de respostas.\nO tempo não está ao seu lado!\n\nEscolha um número de 1 a 20!\n'))
    salao_Bob = numero_verificar(salao_Bob)
    print('____________________________________________________\n')
    if (salao_Bob <= 15):
        print ('Ao passar por uma armadilha você ativa um sensor.\nAs paredes começam a se fechar e você é espremido! Virou Geleia.\n')
        game_over()
    elif (salao_Bob >= 16 and salao_Bob <= 20):
        print('Foi por pouco.\nAo passar por uma armadilha você ativa um sensor.\nAs paredes começam a se fechar mas no último segundo você consegue escapar!\n')
        cena2_Bob()
    else:
        print('Por favor releia o que eu te peço, escolha uma opção válida.\n')
        cena1_Bob()
    

def cena2_Bob():
    quarto_Bob = input('Ao escapar você adentra em um quarto praticamente vazio.\nTodo conteúdo do quarto se resume a uma caixa.\nAo analisar a caixa você descobre que para abrir é necessário resolver uma questão lógica de botões.\n\nEscolha um número de 1 a 20!\n')
    quarto_Bob = numero_verificar(quarto_Bob)
    print('____________________________________________________\n')
    if (quarto_Bob <= 15):
        print ('Você erra a combinação e um gás começa a sair...\nVocê escuta um barulho e antes de conseguir pensaro gás se transformou em chamas devido a uma reação quimica.\nVocê morreu tostado!\n')
        game_over()
    elif (quarto_Bob >= 16 and quarto_Bob <= 20):
        print('Você consegue abrir a caixa.\nDentro dela você encontra dois frascos e um bilhete.\nGosto de jogos Humano, ou devo dizer, Vampíro novato?')
        cena3_Bob()
    else:
        print('Por favor releia o que eu te peço, escolha uma opção válida.\n')


def cena3_Bob():
    misterio_Bob = input('A mensagem continuava dizendo, Em 1 dos Potes tem um antídoto para você voltar a ser humano,\n no outro pode tem um veneno mortal, até mesmo para vampíros.\nBoa sorte kkkk\n\nEscolha 1 ou 2\n')
    misterio_Bob = numero_verificar(misterio_Bob) 
    print('____________________________________________________\n')  
    if (misterio_Bob == 1 ):
        contador = 3
        while contador > 0:
            print(contador)
            time.sleep(1)
            contador -= 1
        print ('Você tomou o veneno mortal! Se lascou!\n')
        game_over()
    elif (misterio_Bob ==2 ):
        contador = 3
        while contador > 0:
            print(contador)
            time.sleep(1)
            contador -= 1
        print('Você conseguiu voltar a ser humano.\n')
        trofeu ()
    else:
        print('Por favor releia o que eu te peço, escolha uma opção válida \n.')


main()


