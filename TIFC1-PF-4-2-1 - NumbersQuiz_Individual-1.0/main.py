import requests

def trivia_fetch(numero):

    url = f"https://opentdb.com/api.php?amount={numero}"
    response = requests.get(url)
    trivia = response.json()
 
    trivia["number"] = numero
    
    return trivia

def main():
    cantidad = int(input("¿Cuántas preguntas de trivia quieres? "))
    trivia = trivia_fetch(cantidad)
    
    if "results" in trivia:
        for pregunta in trivia["results"]:
            print(pregunta["question"])
    else:
        print(trivia)

if __name__ == "__main__":
    main()