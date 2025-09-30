import json
import psycopg2

JSON_PATH = "documents.json"

with open(JSON_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

if isinstance(data, list):
    data = data[0]

course = data["course"]
documents = data["documents"]

# conecta e insere
conn = psycopg2.connect(
    dbname="vectordb",
    user="postgres",
    password="postgres",
    host="127.0.0.1",
    port="5432",
)

try:
    with conn:
        with conn.cursor() as cur:
            inserted = 0
            for doc in documents:
                cur.execute(
                    "INSERT INTO course_faq (course, section, question, answer) VALUES (%s, %s, %s, %s)",
                    (course, doc["section"], doc["question"], doc["text"]),
                )
                inserted += 1
    print(f"✅ Inserção concluída: {inserted} linhas adicionadas em course_faq.")
except Exception as e:
    print(f"❌ Erro na inserção: {e}")
finally:
    conn.close()
