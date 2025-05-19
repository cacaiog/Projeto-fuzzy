
import pandas as pd
from part1 import valor_min_PRESSAO, valor_medio_PRESSAO, valor_max_PRESSAO
from part1 import valor_min_VELOCIDADE, valor_medio_VELOCIDADE, valor_max_VELOCIDADE
from part2 import regra_1, regra_2, regra_3, regra_4, aperta_freio, libera_freio
from centroide import centroide
import part2
import os


# Caminho absoluto do CSV com base na localização do script
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'base_frenagem.csv')

# Leitura do arquivo CSV com caminho seguro
df = pd.read_csv(csv_path)

# Itera sobre cada linha da base
for index, row in df.iterrows():
    part2.pressao_pedal = float(row['pressao_pedal'])
    part2.velocidade_roda = float(row['velocidade_roda'])
    part2.velocidade_carro = float(row['velocidade_carro'])

    # Mostra os resultados fuzzy para cada linha
    print(f"\n📊 Registro {index + 1}")
    print(f"Pressão no pedal: {part2.pressao_pedal}")
    print(f"Velocidade da roda: {part2.velocidade_roda}")
    print(f"Velocidade do carro: {part2.velocidade_carro}")
    print(f"Pertinência pressão baixa: {valor_min_PRESSAO(part2.pressao_pedal):.2f}")
    print(f"Pertinência pressão média: {valor_medio_PRESSAO(part2.pressao_pedal):.2f}")
    print(f"Pertinência pressão alta: {valor_max_PRESSAO(part2.pressao_pedal):.2f}")
    print(f"Libera freio: {libera_freio():.2f}")
    print(f"Aperta freio: {aperta_freio():.2f}")
    print(f"Pressão final no freio (centroide): {centroide():.2f}")
