import psycopg2
import string


#main class
class MainCommandsForDB:
    def __init__(self, name_db: str, user: str, password: str):
        self.name_db = name_db
        self.user = user
        self.password = password

    def processing_phone(number: str):
        """

        """
        allowed = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        num = '+7'
        res = []
        number_s = str(number)
        for n in number_s:
            if n in allowed:
                res.append(n)
        if len(res) != 11:
            return 'incorrect number of digits'
        if res[1] != '9':
            return 'code should start with 9, for example: 902, 920, 923'
        if res[0] == '7' or res[0] == '8':
            res[0] = num
            return ''.join(res)
        else:
            return 'incorrect format of number phone, it should start 7 or 8'

    def processing_name(name):
        lower = list(string.ascii_lowercase)
        upper = list(string.ascii_uppercase)
        name_s = str(name)
        for n in name:
            if (n in lower) or (n in upper):
                pass
            else:
                return 'need use only english letters'
        return True

    def create_table_users(self):
        """

        """
        with psycopg2.connect(
            database=self.name_db, user=self.user, password=self.password) as conn:
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
                number_phone VARCHAR(12) UNIQUE NOT NULL,
                id_user INT REFERENCES users(id_user),
                CONSTRAINT users FOREIGN KEY(id_user) REFERENCES users(id_user) ON DELETE CASCADE
                );
                """)
                conn.commit()

    def add_new_user(self, first_name: str, last_name: str, email: str, number='0'):




# main1 = MainCommandsForDB('postgres', 'postgres', '1997')
# main1.create_table_users()