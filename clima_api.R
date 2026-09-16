# FARMTECH SOLUTIONS - IR ALÉM: DADOS METEOROLÓGICOS VIA API PÚBLICA
# Integrante: André Frederick Abreu Lima
# RM: 576424
#
# Este script conecta a uma API meteorológica pública (Open-Meteo).
# Não é necessário criar conta nem usar chave de API (gratuita e aberta).
# Ele coleta os dados climáticos atuais de Rio Verde (GO), polo de
# produção de soja e milho, e exibe as informações em texto simples
# no terminal.
#
# Pacotes necessários. Se não estiverem instalados, rode antes:
# install.packages("httr")
# install.packages("jsonlite")

library(httr)
library(jsonlite)

# Definimos a localização (Rio Verde - GO).
latitude <- -17.7975
longitude <- -50.9269

# Montamos a URL da API com os parâmetros desejados.
url <- paste0(
  "https://api.open-meteo.com/v1/forecast?",
  "latitude=", latitude,
  "&longitude=", longitude,
  "&current=temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m",
  "&timezone=America%2FSao_Paulo"
)

# Fazemos a requisição GET para a API.
resposta <- GET(url)

# Verificamos se a requisição funcionou (código 200 = sucesso).
if (status_code(resposta) == 200) {

  # Convertemos o conteúdo da resposta (JSON) para uma lista em R.
  dados <- fromJSON(content(resposta, "text", encoding = "UTF-8"))

  # Extraímos os dados meteorológicos atuais.
  horario <- dados$current$time
  temperatura <- dados$current$temperature_2m
  umidade <- dados$current$relative_humidity_2m
  precipitacao <- dados$current$precipitation
  vento <- dados$current$wind_speed_10m

  # Exibimos as informações em texto simples no terminal.
  cat("========================================\n")
  cat("FARMTECH SOLUTIONS - DADOS METEOROLÓGICOS\n")
  cat("========================================\n")
  cat("Local: Rio Verde - GO\n")
  cat("Horário da leitura:", horario, "\n")
  cat("Temperatura atual:", temperatura, "°C\n")
  cat("Umidade relativa do ar:", umidade, "%\n")
  cat("Precipitação:", precipitacao, "mm\n")
  cat("Velocidade do vento:", vento, "km/h\n")
  cat("========================================\n")

  # Fazemos uma leitura simples para apoiar o manejo da lavoura.
  if (precipitacao > 0) {
    cat("Observação: há registro de chuva no momento.\n")
  } else if (umidade < 40) {
    cat("Observação: umidade baixa, atenção à necessidade de irrigação.\n")
  } else {
    cat("Observação: condições dentro da faixa considerada normal.\n")
  }

} else {
  cat("Não foi possível obter os dados meteorológicos. Código HTTP:", status_code(resposta), "\n")
}
