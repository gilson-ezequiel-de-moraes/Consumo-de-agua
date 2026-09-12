# Programa para consumo de agua

def classificar_consumo():
    # Solicitação e tratamento dos dados de entrada
    tipo_imovel = input("Digite o tipo de imóvel (comercial, casa, apartamento): ").strip().lower()
    
    try:
        consumo = float(input("Digite o consumo mensal de água em m³: "))
    except ValueError:
        print("Erro: Por favor, insira um valor numérico válido para o consumo.")
        return

    # Tipos de imovel
    if tipo_imovel == "comercial":
        print("Tarifa comercial aplicada – consulte o plano corporativo.")
    elif tipo_imovel == "apartamento" and consumo < 10:
        print("Consumo econômico – excelente controle de água!")
    elif tipo_imovel in ["apartamento", "casa"] and consumo <= 25:
        print("Consumo moderado – dentro do padrão residencial.")
    else:
        print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")

if __name__ == "__main__":
    classificar_consumo()

