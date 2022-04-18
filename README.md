__Choose your language / escolha sua língua:__
* [README in English](#trend-and-momentum-indicators-for-investing-in-market-indices)
* [LEIA-ME em Português](#indicadores-técnicos-de-tendência-e-momentum-aplicados-ao-investimento-em-índices-de-mercado)

## Trend and Momentum Indicators for Investing in Market Indices

This repository contains the codes for the experiments of my final project for the MBA on Finance and Controllership from the [Luiz de Queiroz College of Agriculture - University of São Paulo](http://www.en.esalq.usp.br/).

__Summary:__
* [Abstract](#abstract)
* [Instructions](#instructions)
* [License (MIT)](LICENSE.txt)

### Abstract

Technical analysis indicators use only past prices and volumes of shares traded to determine when to buy or sell a security. Its effectivity has been the subject of study for decades in the economics literature. Many favorable and unfavorable papers have already been published. Considering such a debate, we introduced an empirical study of 4 trend indicators and 4 momentum indicators for the investment on 7 different market indices. Additionally, we employed a parameter optimization methodology for each indicator, and compared their results with those achieved by classical parameters reported in the literature. For the evaluation of each indicator, we used two risk-adjusted performance measures. Afterwards, the best results of each indicator were compared with the passive buy-and-hold strategy, which consists of buying a security and keeping it for a long period before selling it. During the experiments, we have not identified any improvements in the results that justify the extra computational step required by the optimization procedure. Besides, no technical indicator was able to consistently beat the buy-and-hold strategy in the long run.

### Instructions

1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

2. Install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) (you can also check how to [install git using conda](https://anaconda.org/anaconda/git)).

3. Open a terminal and clone this repository.

```
git clone https://github.com/padilha/technical_analysis_study.git
```

4. Create and activate conda environment.

```
conda env create -f env.yml -n ta-study
conda activate ta-study
```

5. 

## Indicadores Técnicos de Tendência e Momentum Aplicados ao Investimento em Índices de Mercado

Este repositório contém os códigos para os experimentos do meu trabalho de conclusão de curso para o MBA em Finanças e Controladoria da [Escola Superior de Agricultura Luiz de Queiroz - Universidade de São Paulo](http://www.esalq.usp.br/).

__Sumário:__
* [Resumo](#resumo)
* [Instruções](#instruções)
* [Licença (MIT)](LICENSE.txt)

### Resumo

Indicadores de análise técnica baseiam-se exclusivamente em preços e volumes de negociação passados para se tomar a decisão de compra ou venda de um ativo. O debate acerca de sua efetividade estende-se por décadas na literatura econômica. Diversos estudos sobre o tema, tanto favoráveis quanto desfavoráveis, já foram publicados e discutidos. Tomando por base tal debate, buscou-se investigar empiricamente o uso de 4 indicadores de tendência e 4 indicadores de momentum para o investimento em 7 índices de mercado. Para isso, foi empregada uma metodologia de otimização dos parâmetros dos indicadores, comparando seus resultados com parametrizações clássicas da literatura. Para avaliação das performances, foram utilizadas 2 medidas de retorno ajustado ao risco incorrido pelo investimento. Os melhores resultados foram contrastados com uma estratégia de investimento passiva, conhecida por buy-and-hold, a qual consiste em comprar um ativo e mantê-lo por um longo período até sua venda. Durante os experimentos, não foram identificadas melhoras nos resultados que justifiquem o custo computacional extra do procedimento de otimização. Além disso, ao se confrontar os indicadores com o buy-and-hold, não foi possível obter uma performance consistentemente superior para o longo prazo.

### Instruções

1. Instale o [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

2. Instale o [Git](https://git-scm.com/book/pt-br/v2/Come%C3%A7ando-Instalando-o-Git) (você também pode [instalar o git por meio do conda](https://anaconda.org/anaconda/git)).

3. Abra um terminal e clone este repositório.

```
git clone https://github.com/padilha/technical_analysis_study.git
```

4. Crie e ative o ambiente conda.

```
conda env create -f env.yml -n ta-study
conda activate ta-study
```

5. 