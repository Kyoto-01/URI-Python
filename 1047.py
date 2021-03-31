# DESCOBRIR INTERVALO DADA A HORA EM h e m DE INÍCIO E DE FIM

hi, mi, hf, mf = input().split()
hi, mi, hf, mf = int(hi), int(mi), int(hf), int(mf)
duracao = 1440

hi_minutos = (hi * 60) + mi
hf_minutos = (hf * 60) + mf

if hi_minutos < hf_minutos:
    duracao = hf_minutos - hi_minutos
elif hi_minutos > hf_minutos:
    duracao = 1440 - hi_minutos + hf_minutos

duracao_h = duracao // 60
duracao_m = duracao % 60

print(f'O JOGO DUROU {duracao_h} HORA(S) E {duracao_m} MINUTO(S)')
