CREATE EXTENSION pg_trgm;
CREATE EXTENSION btree_gin;
CREATE INDEX books_title_idx ON books USING gin(title);