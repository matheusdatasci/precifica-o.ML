<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Precifica-o.ML - README</title>
</head>
<body>

<h1>Precifica-o.ML</h1>
    <p>Este repositório contém os seguintes arquivos:</p>

 <h2>1. REQUISITOS E PACOTES NECESSÁRIOS.TXT</h2>
    <p>Este arquivo descreve quais bibliotecas são necessárias e suas respectivas versões usadas.</p>

 <h2>2. LH_CD_MATHEUSPINHEIRO.ipynb</h2>
    <p>Notebook com análise estatística, EDA e modelagem. Para utilizá-lo:</p>
    <ul>
        <li>Abra o notebook e, caso queira fazer algo além de apenas visualizar, baixe os pacotes necessários.</li>
        <li>Caso vá rodar o código em um ambiente de execução, como o Google Colab, só precisará importar as bibliotecas.</li>
        <li>Se for rodar em um ambiente local, instale os pacotes com os seguintes comandos:</li>
    </ul>
    <pre>
    !pip install numpy==1.26.4
    !pip install matplotlib==3.10.0
    !pip install pandas==2.2.2
    !pip install seaborn==0.13.2
    </pre>
    <p>Em seguida, realize as importações (os códigos JÁ ESTÃO no notebook).</p>

 <h2>3. TREINAMENTO_MODELO.ipynb</h2>
    <p>Notebook com o treinamento utilizado e avaliação do desempenho. Para utilizá-lo:</p>
    <ul>
        <li>Se for utilizar no Colab, instale o pacote CatBoost com o seguinte comando:</li>
    </ul>
    <pre>
    !pip install catboost==1.2.7
    </pre>
    <ul>
        <li>Em seguida, importe o CatBoostRegressor e as demais bibliotecas:</li>
    </ul>
    <pre>
    import CatBoostRegressor
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_absolute_error
    </pre>
    <p>Se for utilizar em outro ambiente de execução (local), instale os pacotes necessários:</p>
    <pre>
    !pip install catboost==1.2.7
    !pip install scikit-learn==1.6.1
    !pip install pandas==2.2.2
    </pre>
    <p>Em seguida, realize as importações:</p>
    <pre>
    import CatBoostRegressor
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_absolute_error
    </pre>
    <p>Os códigos JÁ ESTÃO no notebook.</p>

<h2>4. MODELO.zip</h2>
    <p>Este arquivo contém o modelo treinado, compactado para facilitar o envio (o GitHub não permite upload de arquivos maiores que 25MB). Para utilizá-lo:</p>
    <ul>
        <li>Baixe e extraia o arquivo. Dentro dele, você encontrará um arquivo .pkl.</li>
        <li>Para usar o modelo em um ambiente de execução, instale os pacotes necessários com:</li>
    </ul>
    <pre>
    !pip install catboost==1.2.7
    </pre>
    <ul>
        <li>Importe as bibliotecas:</li>
    </ul>
    <pre>
    import CatBoostRegressor
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_absolute_error  (Opcional, caso queira avaliar o modelo) 
    import pickle
    </pre>
    <ul>
        <li>Em seguida, carregue o modelo:</li>
    </ul>
    <pre>
    with open('caminho_do_modelo.pkl', 'rb') as file:
        modelo = pickle.load(file)
    </pre>
    <p>Se for utilizar o modelo em um ambiente local, instale os pacotes necessários com:</p>
    <pre>
    !pip install catboost==1.2.7
    !pip install scikit-learn==1.6.1
    !pip install pandas==2.2.2
    </pre>
    <p>Importe as bibliotecas:</p>
    <pre>
    import CatBoostRegressor
    import pandas as pd
    from sklearn.metrics import mean_absolute_error  (Opcional, caso queira avaliar o modelo)
    </pre>

 <h3>Atenção:</h3>
    <p>Para utilizar o modelo, os dados precisam estar modelados conforme o modelo foi treinado. Para isso, criei uma função que faz toda modelagem automaticamente. Basta inserir dois parâmetros: o dataframe dos dados que deseja prever e o dataframe original (o arquivo enviado para o desafio).</p>
    <pre>
    dados = modelar_dados(param1, param2)
    previsao = modelo.predict(dados)
    print(previsao)
    </pre>

 <h2>5. def_modelar_dados.py</h2>
    <p>Este é o arquivo Python com o código da função para modelar os dados antes de fazer previsões.</p>

 <h3>Informações adicionais:</h3>
    <p>Se precisar instalar o <a href="https://www.rust-lang.org/" target="_blank">Rust</a> para rodar algum pacote ou biblioteca relacionada, você pode seguir as instruções no <a href="https://www.rust-lang.org/learn/get-started" target="_blank">site oficial do Rust</a>.</p>

</body>
</html>
