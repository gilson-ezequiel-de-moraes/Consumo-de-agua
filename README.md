# Consumo de Água

Este programa em Python solicita o tipo de imóvel e o consumo mensal de água em metros cúbicos ($m^3$) para classificar a tarifa e o nível de consumo de acordo com regras de negócio predefinidas.

## 📌 Funcionalidades

O script realiza a leitura do tipo de imóvel (`comercial`, `casa` ou `apartamento`) e do consumo mensal (número decimal), aplicando as seguintes regras de exibição:

* **Imóvel Comercial:** Exibe `"Tarifa comercial aplicada – consulte o plano corporativo."`
* **Apartamento com consumo < 10 $m^3$:** Exibe `"Consumo econômico – excelente controle de água!"`
* **Apartamento ou Casa com consumo de até 25 $m^3$:** Exibe `"Consumo moderado – dentro do padrão residencial."`
* **Outros casos (consumo elevado):** Exibe `"Consumo excessivo – adote medidas de economia e verifique vazamentos."`

## 🚀 Como Executar

### Pré-requisitos
* Python instalado em sua máquina.
* Abre o VsCode

### Passo a passo
1. Baixe o arquivo `app.py`.
2. Abra o terminal na pasta do arquivo.
3. Execute o comando:
