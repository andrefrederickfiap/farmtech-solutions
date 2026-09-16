# FARMTECH SOLUTIONS - ANALISE EM R
# Integrante: André Frederick Abreu Lima
# RM: 576424
#
# Nesta etapa usamos dados obtidos nos testes do programa Python.
# O objetivo é calcular estatísticas básicas: média e desvio-padrão.

# Criamos um vetor com os nomes das culturas usadas nos testes.
culturas <- c("Soja", "Soja", "Milho", "Milho")

# Criamos um vetor com as áreas, em hectares, obtidas nos testes do Python.
areas <- c(2.0, 1.5, 3.0, 4.0)

# Criamos um vetor com as quantidades totais de insumo, em kg.
quantidades <- c(300, 180, 300, 440)

# Mostramos os dados das culturas no terminal.
cat("Culturas testadas:\n")
print(culturas)

# Mostramos as áreas no terminal.
cat("\nÁreas (hectares):\n")
print(areas)

# Mostramos as quantidades de insumo no terminal.
cat("\nQuantidades de insumo (kg):\n")
print(quantidades)

# Calculamos a média das áreas.
media_areas <- mean(areas)

# Calculamos o desvio-padrão das áreas.
desvio_areas <- sd(areas)

# Calculamos a média das quantidades de insumo.
media_quantidades <- mean(quantidades)

# Calculamos o desvio-padrão das quantidades de insumo.
desvio_quantidades <- sd(quantidades)

# Mostramos os resultados de forma organizada no terminal.
cat("\n========================================\n")
cat("RESULTADOS ESTATÍSTICOS - FARMTECH SOLUTIONS\n")
cat("========================================\n")
cat("Média das áreas (ha):", media_areas, "\n")
cat("Desvio-padrão das áreas (ha):", desvio_areas, "\n")
cat("Média das quantidades de insumo (kg):", media_quantidades, "\n")
cat("Desvio-padrão das quantidades de insumo (kg):", desvio_quantidades, "\n")
cat("========================================\n")
