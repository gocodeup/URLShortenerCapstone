/* run on the mac with `psql postgres -f initialize_db.pgsql` */
DROP DATABASE IF EXISTS url_shortener;
DROP ROLE IF EXISTS url_shortener;

CREATE USER url_shortener CREATEDB PASSWORD 'Passw0rd';
CREATE DATABASE url_shortener OWNER url_shortener;
GRANT ALL PRIVILEGES ON DATABASE url_shortener TO url_shortener;

\connect url_shortener

CREATE TABLE urls (
    id SERIAL PRIMARY key,
    url VARCHAR(1024) NOT NULL,
    shortcode CHAR(10) NOT NULL,
    created timestamptz NOT NULL,
    creator inet NOT NULL
); 

GRANT ALL PRIVILEGES ON TABLE urls TO url_shortener;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO url_shortener;