import json

with open("output_results/history.json") as f:
    history = json.load(f)

maximo_detectado = max(item["count"] for item in history)

print(f"Estimativa: passaram até {maximo_detectado} pessoas pela câmera.")