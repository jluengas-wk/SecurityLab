import json
import os

# Configuración de archivos
INPUT_FILE = "resultados_sast.json"
OUTPUT_FILE = "vulnerabilidades_criticas.txt"

def parse_semgrep_results():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: No se encontró el archivo {INPUT_FILE}")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    results = data.get("results", [])
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write("=== REPORTE DE VULNERABILIDADES CRÍTICAS (SAST) ===\n")
        out.write(f"Total de hallazgos analizados: {len(results)}\n")
        out.write("-" * 50 + "\n\n")

        for i, res in enumerate(results, 1):
            cwe = res["extra"]["metadata"].get("cwe", ["N/A"])[0]
            message = res["extra"]["message"]
            file_path = res["path"]
            line = res["start"]["line"]

            out.write(f"Hallazgo #{i}\n")
            out.write(f"CWE: {cwe}\n")
            out.write(f"Archivo: {file_path} (Línea {line})\n")
            out.write(f"Descripción: {message}\n")
            out.write("-" * 30 + "\n")

    print(f"Proceso completado. Se generó: {OUTPUT_FILE}")

if __name__ == "__main__":
    parse_semgrep_results()