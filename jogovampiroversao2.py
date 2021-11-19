



# cena1 = salão
# cena2 = quarto
# cena3 = salaMisteriosa
# Vlad = 1
# Lillith = 2
# Bob = 3 

#função inicio do jogo = escolhas de personagens
def main(): 
    escolha_personagem = int (input('Eu gosto de surpresas... escolha 1, 2 ou 3 e descubra quem és '))


    if (escolha_personagem == 1):
        print('Você se chama Vlad, você é um Vampiro misterioso... porem meio tonto...  ')
        cena1_vlad()
    if (escolha_personagem == 2):
        print('Você é Lillith! Uma voz no seu ouvido diz... "Ah sua Vampira linda, que saudade... ')
        cena1_lilith()
    if (escolha_personagem == 3):
        print('Bob... aaah, que coisa estranha... Seu pescoço deve estar dolorido em...  ')
        cena1_Bob()
    else:
        print('Por favor releia o que eu te peço, escolha uma opção válida.')
        main()


 ###########################################################################################


def game_over():
    resposta_jogador =  (input('Você perdeu.\n Deseja jogar novamente [S/N]? ')).upper()
    if (resposta_jogador == 'S'):
        main()
    else: 
        print('Ok, então. Bye bye!')
        


#############################################################################################

def cena1_vlad():
    salao_vlad = int(input('Você se encontra em um mezanino, as paredes são muito altas... \n Tem uma escadaria toda decorada em ouro a sua frente! Você esta olhando para baixo... \n Será que você consegue descer...? \n Por favor digite um número de 1 a 20 '))
    if (salao_vlad <= 15):
        print ('Você pisou em uma armadilha... \n você teve a "grande sorte" de cair em um porão cheio de estacas...\n Tente novamente em outra história, isto é... se tiver coragem kkkk... ')
        game_over()
    if (salao_vlad >= 16 and salao_vlad <= 20):
        print('Você pisou em uma armadilha, mas o seu instinto vampírico falou mais alto! \n Você se  transformou em morcego e desceu até o andar de baixo. Foi por pouco em... \n Tome mais cuidado da próxima vez!')
        cena2_vlad()
    else:
        print('Por favor releia o que eu te peço, escolha uma opção válida ou vai virar churrasquinho. ')
    

def cena2_vlad():
    quarto_vlad = int(input('Você escuta um grito e vai ao quarto para descobrir sua origem... \n Você ainda não adentrou no quarto. \n Você não consegue ver muito bem mesmo ativando sua visão vampírica...\n Na porta você identifica desenhado a giz branco o que se parece com uma operação de matematica incompleta... \n Por um breve momento de loucura, insanidade você acredita que se resolver essa charada você consegue sair dessa ileso! \n Escolha um número de 1 a 20 '))
    if (quarto_vlad <= 15):
        print ('Seria você o Leopoldo Nachbin? kkk Não, com certeza não! Mas Vlad você foi muito esperto nessa...\n Será que na próxima terá a mesma sorte? ')
        cena3_vlad()
    if (quarto_vlad >= 16 and quarto_vlad <= 20):
        print('Tava no caminho certo Vlad, mas você tropeçou e para não bater a cara no chão se apoiou-se em uma estatua de pedra adentro do quarto\n e adivinha? Você ativou a armadilha da fome! Você virou um churrasquinho bem passado!\n Mais cuidado se houver uma próxima vez! ')
        game_over()
    else:
        print('Por favor releia o que eu te peço, escolha uma opção válida.')


def cena3_vlad():
    misterio_vlad = int(input('faça a escolha misterio d20 '))
    if (misterio_vlad <= 15):
        print ('perdeu tudo')
        game_over()
    if (misterio_vlad >= 16 and misterio_vlad <= 20):
        print('vc ganho')
    else:
        print('Por favor releia o que eu te peço, escolha uma opção válida.')


#############################################################################  
# cenas jogadas se for com a personagem Lillith  

def cena1_lilith():
    salao_lilith = int(input('faça a escolha o salão d20 '))
    if (salao_lilith <= 15):
        print ('byebye')
    if (salao_lilith >= 16 and salao_lilith <= 20):
        print('Foi por pouco')
        cena2_lilith()
    else:
        print('Por favor releia o que eu te peço, escolha uma opção válida.')
    

def cena2_lilith():
    quarto_lilith = int(input('faça a escolha quarto d20'))
    if (quarto_lilith <= 15):
        print ('chora bebe')
    if (quarto_lilith >= 16 and quarto_lilith <= 20):
        print('ta quase la em')
        cena3_lilith()
    else:
        print('Por favor releia o que eu te peço, escolha uma opção válida.')


def cena3_lilith():
    misterio_lilith = int(input('faça a escolha misterio d20 '))
    if (misterio_lilith <= 15):
        print ('perdeu tudo')
    if (misterio_lilith >= 16 and misterio_lilith <= 20):
        print('vc ganho')
    else:
        print('Por favor releia o que eu te peço, escolha uma opção válida.')

######################################################################################################
# cenas jogadas caso seja com o personagem Bob

def cena1_Bob():
    salao_Bob = int(input('faça a escolha o salão d20 '))
    if (salao_Bob <= 15):
        print ('byebye')
    if (salao_Bob >= 16 and salao_Bob <= 20):
        print('Foi por pouco')
        cena2_Bob()
    else:
        print('Por favor releia o que eu te peço, escolha uma opção válida.')
    

def cena2_Bob():
    quarto_Bob = int(input('faça a escolha quarto d20'))
    if (quarto_Bob <= 15):
        print ('chora bebe')
    if (quarto_Bob >= 16 and quarto_Bob <= 20):
        print('ta quase la em')
        cena3_Bob()
    else:
        print('Por favor releia o que eu te peço, escolha uma opção válida.')


def cena3_Bob():
    misterio_Bob = int(input('faça a escolha misterio d20 '))
    if (misterio_Bob <= 15):
        print ('perdeu tudo')
    if (misterio_Bob >= 16 and misterio_Bob <= 20):
        print('vc ganho')
    else:
        print('Por favor releia o que eu te peço, escolha uma opção válida .')


main()


