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
    <p>Este arquivo contém o modelo treinado, compactado para facilitar o envio (o GitHub não pe
