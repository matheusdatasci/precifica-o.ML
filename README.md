# precifica-o.ML
Temos cinco arquivos no repositório: 
REQUISITOS E PACOTES NECESSÁRIOS.TXT: Quais bibliotecas são necessarias e suas respectivas versôes usadas.

LH_CD_MATHEUSPINHEIRO.ipynb (Notebook com an´lise estattistica, EDA e modelagem)
Abra e, caso queira fazer algo além de apenas visualizar, baixe os pacotes necessários(Caso vá rodar o código em um ambiente de execução, Como do google Colab, só precisará importar)
Caso contrário, instale os pcacotes com:
!pip install numpy==1.26.4
!pip install matplotlib==3.10.0
!pip install pandas==2.2.2
!pip install seaborn==0.13.2
e realize as importações.
(os códigos JÁ ESTÃO no notebook)

TREINAMENTO_MODELO.ipynb (Notebook com o treinamento utilizado e avaliação do desempenho)
Abra e, caso queira fazer algo além de apenas visualizar, baixe os pacotes necessários:

Caso vá usar no Colab:
!pip install catboost==1.2.7
e então importe o CatBoostRegressor
importe o train_test_split do sklearn(já existe a lib no colab)
importe o mean_absolute_error
(os códigos JÁ ESTÃO no notebook)

Caso NÃO vá utilizar no Colab ou em outro ambiente de execução(Utilizando em um ambiente local):
Necessária instalação do Rust e Cargo para conseguir instalr o catboost: Segue o link - https://rustup.rs/
!pip install catboost==1.2.7
!pip install scikit-learn==1.6.1
!pip install pandas==2.2.2
e então importe o CatBoostRegressor
importe o train_test_split do sklearn
importe o mean_absolute_error
(os códigos JÁ ESTÃO no notebook)

MODELO.zip (Baixe e extraia, você terá o arquivo .pkl, precisei compactar pois o github não permite upload de arquivos maiores que 25MB)

Para usar o modelo em um ambiente de execução:
!pip install catboot==1.2.7
import CatBoostRegressor
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error ((OPCIONAL, caso queira avaliar o modelo)
import pickle
with open('caminho_do_modelo.pkl', 'rb') as file:
    modelo = pickle.load(file)


Para usar o modelo em um ambiente local:
!pip install catboost==1.2.7 (não esqueça do Rust e Cargo:https://rustup.rs/)
!pip install scikit-learn==1.6.1
!pip install pandas==2.2.2
import CatBoostRegressor
import pandas as pd
from sklearn.metrics import mean_absolute_error ((OPCIONAL, caso queira avaliar o modelo)

ATENÇÃO: Para utilizar o modelo, os dados precisarão estar modelados conforme o modelo foi treinado.

Para isso, criei uma função que faz toda modelagem sozinha, basta inserir dois parametros(dataframe dos dados que querem prever valores, dataframe original(o arquivo mandado para o desafio))

Salve o retorno dessa função em uma variável como: dados = modelar_dados(param1. param2) e então, finalmente:

previsao = modelo.predict(dados)
print(previsao)


def_modelar_dados.py: Arquivo python com o código da função para modelar os dados antes de fazer previsões.















