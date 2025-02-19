import pandas as pd
import plotly.express as px

data = pd.read_csv("Data/Online Shopping Data.csv")
print(data)

# Discover lack and false data insert into the table
gender = data["Gender"]
major = data["Major_Drawback"]
freq_products = data["Frequent_Products"]
pd.set_option("display.max_rows", None)
print(gender)
print(major)
print(freq_products)

# remove rows with corrupted data, leaving only male and female at gender column
data_list = data.drop(data.index[98]).drop(data.index[200]).drop(data.index[59]).drop(data.index[31])

# Check the new data table
print(data_list)

for column in data_list:
    graphic = px.histogram(data_list, x=column, color="Gender")
    graphic.show()

'''
Analysis about data graphics:
1  - A maioria dos consumidores nessa pesquisa são do sexo feminino 
2  - A maioria realiza pelo menos 1 compra por mês (F), M são mais desligados para isso
3  - Para os M são maioria até 20%, para F pode chegar até 40%
4  - Os consumidores sempre olham as verificações e avaliações sobre o produto que querem comprar
5  - Consumidores acham o fator mais atrativo o conforte e facilidade de comprar sem sair de casa
6  - Consumidores levam muito mais em conta na hora de escolher onde comprar as avaliaçoes e reviews de outros consumidores
7  - Preferem realizar o pagamento em dinheiro na hora da entrega
8  - Não possuem preferencia por comprar em um varejista local ou internacional
9  - XXXXXXXX
10 - A grande maioria é muito preocupada com a segurança do site que estão comprando
11 - Definitivamente promocoes não são o maior diferencial para atrair o consumidor a compra determinado produto
12 - Em algumas vezes os consumidores podem comprar um produto similar dependendo do preço
13 - Uma range confortavel para a maioria é entre 1k - 5k dol
14 - F são mais atraidas por roupas e acessrios fashions, livros e produtos de beleza, M roupas e acessrios fashions e eletronicos
15 - Principal desvantagem são problemas com a qualidade dos produtos
16 - A maioria já teve problemas com autenticidade dos produtos
17 - Melhorias mais desejadas Melhor descricao dos produtos e imagens dele, Sistema Aprimorado de Avaliações e Classificações de Clientes

Para alguma empresa que pretender abrir um ecommerce para oferece seus produtos, existem alguns topicos
que ela precisa atender:
1 - Ter uma sessão onde os clientes colocam suas avaliações, reviews e fotos do produto
2 - Incluir o pagamento em dinheiro na entrega 
3 - Mostrar ao consumidor que o site é seguro, colocando selos e premios se for o caso no rodapé
4 - Ter uma página de recomendação baseada nos gostos do cliente

'''