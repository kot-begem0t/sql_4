import psycopg2


#main class
class MainCommandsForDB:
    def __init__(self, name_db: str, user: str, password: str):
        self.name_db = name_db
        self.user = user
        self.password = password

    def create_table_users(self):
        with psycopg2.connect(database=self.name_db, user=self.user, password=self.password) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                CREATE TABLE IF NOT EXISTS users(
                id_user SERIAL PRIMARY KEY,
                first_name VARCHAR(30) NOT NULL,
                last_name VARCHAR(40) NOT NULL,
                email VARCHAR(50) UNIQUE NOT NULL
                );
                """)
                conn.commit()
                cur.execute("""
                CREATE TABLE IF NOT EXISTS number_phones(
                id_number_phone SERIAL PRIMARY KEY,
                number_phone INT UNIQUE NOT NULL,
                id_user INT REFERENCES users(id_user),
                CONSTRAINT users FOREIGN KEY(id_user) REFERENCES users(id_user) ON DELETE CASCADE
                );
                """)
                conn.commit()

main1 = MainCommandsForDB('postgres', 'postgres', '1997')
main1.create_table_users()