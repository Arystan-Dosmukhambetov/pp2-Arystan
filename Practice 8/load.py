from connect import connect

def run(file):
    conn = connect()
    cur = conn.cursor()

    with open(file, "r", encoding="utf-8") as f:
        sql = f.read()

    cur.execute(sql)
    conn.commit()

    cur.close()
    conn.close()

run("functions.sql")
run("procedures.sql")