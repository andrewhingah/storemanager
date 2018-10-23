import psycopg2
import os

url = "dbname='store_manager' host='localhost' port='5432' user='postgres' password='postgres'"

db_url = os.getenv('DATABSE_URL')

def connection (url):
	con = psycopg2.connect(url)
	return con
def init_db():
	con = connection(url)
	return con

def create_tables():
	conn = connection(url)
	curr = conn.cursor()
	queries = tables()

	for query in queries:
		curr.execute(query)
		conn.commit()

def destroy_tables():
	pass

def tables():
	tb1 = """CREATE TABLE IF NOT EXISTS products (
		product_id serial PRIMARY KEY NOT NULL,
		name character varying(1000) NOT NULL,
		price numeric NOT NULL,
		quantity  numeric NOT NULL,
		date_created timestamp with time zone DEFAULT ('now'::text)::date NOT NULL
		)"""

    tb2 = """CREATE TABLE IF NOT EXISTS sales (
	    sales_id serial PRIMARY KEY NOT NULL,
	    product_id numeric NOT NULL,
	    price numeric NOT NULL,
	    attendant character varying(200) NULL,
	    date_created timestamp with time zone DEFAULT ('now'::text)::date NOT NULL
	    )"""

    tb3 = """CREATE TABLE IF NOT EXISTS users (
	    user_id serial PRIMARY KEY NOT NULL,
	    first_name character varying(50) NOT NULL,
	    last_name character varying(50),
	    username character varying(50) NOT NULL,
	    email character varying(50),
	    role character varying(10), 
	    date_created timestamp with time zone DEFAULT ('now'::text)::date NOT NULL,
	    password character varying(500) NOT NULL
	    )"""

	queries = [tb1, tb2, tb3]
	return queries