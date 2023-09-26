__Choose your language / escolha sua língua:__
* [README in English](#trend-and-momentum-indicators-for-investing-in-market-indices)
* [LEIA-ME em Português](#indicadores-técnicos-de-tendência-e-momentum-para-o-investimento-em-índices-de-mercado)

---------------------------------------

## Trend and Momentum Indicators for Investing in Market Indices

This repository contains the codes for the experiments of my final project for the MBA on Finance and Controllership from the [Luiz de Queiroz College of Agriculture - University of São Paulo](http://www.en.esalq.usp.br/).

__Summary:__
* [Abstract](#abstract)
* [How to install and run](#how-to-install-and-run)
* [File description](#file-description)
* [License (MIT)](LICENSE.txt)

### Abstract

Technical analysis indicators use only past prices and volumes of shares traded to determine when to buy or sell a security. Its effectivity has been the subject of study for decades in the economics literature. Many favorable and unfavorable papers have already been published. Considering such a debate, we introduced an empirical study of 4 trend indicators and 4 momentum indicators for the investment on 7 different market indices. Additionally, we employed a parameter optimization methodology for each indicator, and compared their results with those achieved by classical parameters reported in the literature. For the evaluation of each indicator, we used two risk-adjusted performance measures. Afterwards, the best results of each indicator were compared with the passive buy-and-hold strategy, which consists of buying a security and keeping it for a long period before selling it. During the experiments, we have not identified any improvements in the results that justify the extra computational step required by the optimization procedure. Besides, no technical indicator was able to consistently beat the buy-and-hold strategy in the long run.

### How to install and run

1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

2. Install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) on your system (as an alternative, you can [install git using conda](https://anaconda.org/anaconda/git)).

3. Open a terminal and clone this repository.

```
git clone https://github.com/padilha/technical_analysis_study.git
```

4. Create and activate conda environment.

```
conda env create -f env.yml -n ta-study
conda activate ta-study
```

5. To list the available command line arguments type:

```
python experiment.py -h
```

The available options are:

* ```-h``` : displays the help message.

* ```-d``` : datasets directory.

* ```-o``` : output directory.

* ```-n``` : number of jobs to run in parallel (default: 1).

* ```-r``` : risk-free file path (default: ```./US_TBond.csv```).

6. Example of how to run:

```
python experiment.py -d ./datasets -o ./output -n 5
```

7. After running the codes, you can deactivate the environment.

```
conda deactivate
```

### File description

* ```US_TBond.csv``` : annual returns on investiments in US T. Bond (source: [Damodaran](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html)). It is used as the risk-free rate for the Sharpe ratio.

* ```backtest.py``` : backtesting structure. It performs parameter optimization of the trading rules and simulates trades and fees.

* ```data.py``` : fetches price and volume series from Yahoo Finance.

* ```env.yml``` : specifies the virtual environment for this project.

* ```evaluation.py``` : evaluation measures (Sharpe ratio and Calmar ratio).

* ```experiment.py``` : runs the experiment.

* ```rules.py``` : contains the implementation of trading rules.

* ```results_default.zip```: result files of the default parameters.

* ```results_optimization.zip```: result files of the parameter optimization procedure.

* Each result filename follows the convention MARKET__STRATEGY__EVALUATIONMEASURE (for example DJIA__BH__calmar refers to the results of the buy-and-hold strategy on the Dow Jones Industry Average Index using the Calmar ratio). For each market-strategy-evaluation combination, there are two files:
    * JSON file: contains the dictionary of results in the format {year : evaluation measure value}.

    * CSV file: contains the resulting time series.

---------------------------------------

## Indicadores Técnicos de Tendência e Momentum para o Investimento em Índices de Mercado

Este repositório contém os códigos para os experimentos do meu trabalho de conclusão de curso para o MBA em Finanças e Controladoria da [Escola Superior de Agricultura Luiz de Queiroz - Universidade de São Paulo](http://www.esalq.usp.br/).

__Sumário:__
* [Resumo](#resumo)
* [Como instalar e rodar](#como-instalar-e-rodar)
* [Descrição dos arquivos](#descrição-dos-arquivos)
* [Licença (MIT)](LICENSE.txt)

### Resumo

Indicadores de análise técnica baseiam-se exclusivamente em preços e volumes de negociação passados para se tomar a decisão de compra ou venda de um ativo. O debate acerca de sua efetividade estende-se por décadas na literatura econômica. Diversos estudos sobre o tema, tanto favoráveis quanto desfavoráveis, já foram publicados e discutidos. Tomando por base tal debate, buscou-se investigar empiricamente o uso de 4 indicadores de tendência e 4 indicadores de momentum para o investimento em 7 índices de mercado. Para isso, foi empregada uma metodologia de otimização dos parâmetros dos indicadores, comparando seus resultados com parametrizações clássicas da literatura. Para avaliação das performances, foram utilizadas 2 medidas de retorno ajustado ao risco incorrido pelo investimento. Os melhores resultados foram contrastados com uma estratégia de investimento passiva, conhecida por buy-and-hold, a qual consiste em comprar um ativo e mantê-lo por um longo período até sua venda. Durante os experimentos, não foram identificadas melhoras nos resultados que justifiquem o custo computacional extra do procedimento de otimização. Além disso, ao se confrontar os indicadores com o buy-and-hold, não foi possível obter uma performance consistentemente superior para o longo prazo.

### Como instalar e rodar

1. Instale o [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

2. Instale o [Git](https://git-scm.com/book/pt-br/v2/Come%C3%A7ando-Instalando-o-Git) no seu sistema (como alternativa, você pode [instalar o git por meio do conda](https://anaconda.org/anaconda/git)).

3. Abra um terminal e clone este repositório.

```
git clone https://github.com/padilha/technical_analysis_study.git
```

4. Crie e ative o ambiente conda.

```
conda env create -f env.yml -n ta-study
conda activate ta-study
```

5. Para listar os argumentos utilize este comando:

```
python experiment.py -h
```

As opções disponíveis são:

* ```-h``` : mostra a mensagem de ajuda.

* ```-d``` : diretório contendo as bases de dados.

* ```-o``` : diretório de saída.

* ```-n``` : número de processos para rodar os experimentos em paralelo.

6. Exemplo de como rodar:

```
python experiment.py -d ./datasets -o ./output -n 5
```

7. Após rodar os códigos, o ambiente conda pode ser desativado.

```
conda deactivate
```

### Descrição dos arquivos

* ```US_TBond.csv``` : retornos anuais do investimento em US T. Bond (fonte: [Damodaran](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html)). É utilizado para o cálculo do retorno do ativo livre de risco no índice Sharpe.

* ```backtest.py``` : estrutura de backtesting. Realiza a otimização de parâmetros dos indicadores técnicos e simula as compras e vendas de ativos e cobrança de taxas de transação.

* ```data.py``` : coleta as séries de preço e volume no Yahoo Finance.

* ```env.yml``` : especifica o ambiente virtual para este projeto.

* ```evaluation.py``` : implementa as medidas de avaliação (índices Sharpe e Calmar).

* ```experiment.py``` : roda o experimento.

* ```rules.py``` : contém as implementações das regras de trade.

* ```results_default.zip```: arquivos de resultados para os parâmetros padrão.

* ```results_optimization.zip```: arquivos de resultados para o procedimento de otimização de parâmetros.

* O nome de cada arquivo de resultado segue a convenção MERCADO__ESTRATÉGIA__AVALIAÇÃO (por exemplo, DJIA__BH__calmar refere-se aos resultados da estratégia buy-and-hold no índice Dow Jones Industry Average utilizando o índice Calmar). Para cada combinação mercado-estratégia-avaliação, existem dois arquivos:
    * Arquivo JSON: contém um dicionário de resultados no formato {ano : valor da medida de avaliação}.

    * Arquivo CSV: contém a série temporal resultante.