# Indicators
Programa criado para calcular média móvel exponencial e bandas de bollinger com base nos dados do Bitcoin.

# Install
Recomendo o uso do ambiente virtual<br>
https://virtualenv.pypa.io/en/latest/installation.html
```bash
virtualenv venv
```
```bash
pip install requirements.txt
```

# Importante
O arquivo final.csv precisa ser criado em sua pasta, ou copiado do repositório.

O código possui as variáveis de ambiente DATA_INICIO e DATA_FIM, no entanto, a utilização delas não está funcionando como deveria. Em sua aplicação, o dataFrame criado recebe apenas os dados de data, ignorando todo o resto.

Esse repositório continuará sendo atualizado com novos estudos.

# Funcionamento
<ol>
<li>getDataSetFile: Função criada para recebimento de dados. Ela recebe como parâmetro um caminho para o arquivo csv. Retorna o dataFrame completo com as colunas Timestamp,Open,High,Low,Close,Volume_(BTC),Volume_(Currency),Weighted_Price. Dentro dessa função temos diversos comentários referentes a testes realizados para tentar realizar a filtragem por data (não funcionando ainda).</li>
<li>simpleMovingAverage: Recebe um dataSet e um período (caso não seja passado, usa o padrão da SB, 40 períodos) Utiliza a função <b>rolling</b> para realizar o cálculo da média simples, recebendo o valor do period como parâmetro </li>
<li>movingAverage: Recebe o mesmo dataSet e o período. Utiliza o valor da coluna 'Close' e aplica a função .ewm para o cálculo da média exponencial</li>
<li>bollingerBands: Recebe o dataSet, período e o desvio padrão. Realiza o cálculo da média simples chamando a função simpleMovingAverage (essa média é apresentada na bollinger como a média central). Em seguida, realiza o cálculo do desvio padrão para aplicar nas bandas superior e inferior</li>
<li>RSI: Recebe o dataSet e o período. O funcionamento do IFR é um pouco mais complicado, ele precisa verificar a diferença entre o preço atual para o preço anterior e armazenar se esse valor. Em seguida, precisamos definir se esse valor é maior ou menor que zero. Se ele for maior que zero, é mantido na lista de positivos, no mesmo lugar da lista de negativos é colocado um zero e vice versa.<br> Agora vamos definir os preços médios de ganho e perda, para isso vamos usar os valores separados no item anterior. Decidi calcular o indicador com base em uma média exponencial para os valores médios de ganho e perda. Em seguida, podemos realizar o cálculo necessário da força, definida pelo médio de ganho divido pelo médio de perda. AO final, vamos colocar esses valores dentro da dataSet na coluna 'RSI', o resultado é baseado na fórmula 100 - (100 / (1 + força relativa)) </li>
<li>plotIndicatorsOnGraph: Apresenta dados no gráfico</li>
</ol>

# Indicadores
- [x] Médias Móveis Exponenciais 10/12/2020
- [x] Índice de Força Relativa 10/12/2020
- [x] Bandas de Bollinger 10/12/2020
- [ ] MACD
- [ ] HiLo
- [ ] Stop Atr
- [ ] Fibonacci