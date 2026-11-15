from pathlib import Path

LOG_DIR = Path.home() / ".local" / "state" / "tam-n"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "log.txt"

def guardar_log(texto):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(texto)
