import part2
from part1 import valor_min_PRESSAO, valor_medio_PRESSAO, valor_max_PRESSAO
from part1 import valor_min_VELOCIDADE, valor_medio_VELOCIDADE, valor_max_VELOCIDADE
from part2 import libera_freio, aperta_freio
from centroide import centroide


#Mostrará todas as saídas:

print('\n')
print('Valores de Pertinência Nebulosos')
print('Pressão no Pedal Baixo (L): {}'.format(valor_min_PRESSAO(part2.pressao_pedal)))
print('Pressão no Pedal Médio (M): {}'.format(valor_medio_PRESSAO(part2.pressao_pedal)))
print('Pressão no Pedal Alto  (H): {}'.format(valor_max_PRESSAO(part2.pressao_pedal)))
print('\n')

print('Velocidade da Roda Devagar (S): {:.3f}'.format(valor_min_VELOCIDADE(part2.velocidade_roda)))
print('Velocidade da Roda Médio   (M): {:.3f}'.format(valor_medio_VELOCIDADE(part2.velocidade_roda)))
print('Velocidade da Roda Rápido  (F): {}'.format(valor_max_VELOCIDADE(part2.velocidade_roda)))

print('\n')
print('Velocidade do Carro Devagar (S): {}'.format(valor_min_VELOCIDADE(part2.velocidade_carro)))
print('Velocidade do Carro Médio   (M): {}'.format(valor_medio_VELOCIDADE(part2.velocidade_carro)))
print('Velocidade do Carro Rápido  (F): {:.3f}'.format(valor_max_VELOCIDADE(part2.velocidade_carro)))

print('\n')
print('Libere o Freio: {:.3f}'.format(libera_freio()))
print('Aperte o freio: {}'.format(aperta_freio()))
print('Pressão no Freio (Centróide): {:.2f}'.format(centroide()))
