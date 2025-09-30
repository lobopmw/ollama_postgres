-- extensões mínimas
CREATE EXTENSION IF NOT EXISTS plpython3u;
CREATE EXTENSION IF NOT EXISTS vector;



-- tabela para RAG
CREATE TABLE IF NOT EXISTS docs (
  id BIGSERIAL PRIMARY KEY,
  source  text,
  content text NOT NULL,
  embedding vector(768)
);

CREATE INDEX IF NOT EXISTS idx_docs_embedding_cos
  ON docs USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);
