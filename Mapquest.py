import requests
import urllib.parse

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "pmp9aYEbDqBwX98dZIxrTDWvwL4TnWEg" 

while True:
    orig = input("Ciudad de Origen: ")
    if orig == "quit" or orig == "s":
        break
    dest = input("Ciudad de Destino: ")
    if dest == "quit" or dest == "s":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    print("URL: " + url)
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("Estado de la API: " + str(json_status) + " = Llamada de ruta exitosa.\n")
        print("=============================================")
        print("Direcciones desde " + orig + " hasta " + dest)
        print("Duración del viaje: " + json_data["route"]["formattedTime"])
        print("Millas: " + str(json_data["route"]["distance"]))
        print("Kilómetros: " + str("{:.1f}".format(json_data["route"]["distance"] * 1.61)))
        print("=============================================")
        print("Combustible requerido: " + str("{:.1f}".format(json_data["route"]["distance"] * 0.08)) + " litros")
        print("=============================================")
    for each in json_data["route"]["legs"][0]["maneuvers"]:
        print(each["narrative"] + " (" + str("{:.1f}".format(each["distance"] * 1.61)) + " km)")
        print("=============================================\n")

