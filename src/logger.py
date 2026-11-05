# ==============================
# FUNCION guardar_log
# ==============================
def guardar_log(texto):
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(texto)
