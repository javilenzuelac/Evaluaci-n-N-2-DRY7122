import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "ddwXo09jT2z6OxAfkqZqZ3jz69fmYYSB"

while True:
    orig = input("Ciudad de Origen: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Ciudad de Destino: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print("URL: " + url)
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        duracion = json_data['route']['formattedTime']
        duracion_horas, duracion_minutos, duracion_segundos = map(int, duracion.split(':'))
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Direcciones desde " + orig + " a " + dest)
        print("Narrativa del viaje:")
        for step in json_data["route"]["legs"][0]["maneuvers"]:
            print(step["narrative"])
        print(f"Duración del viaje: {duracion_horas} horas, {duracion_minutos} minutos, {duracion_segundos} segundos")
        print("Kilometros:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Combustible Utilizado (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
