import mysql.connector


class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()

    def setup_db(self):
        self.cursor.execute('''
          CREATE TABLE IF NOT EXISTS books (
            book_id INT AUTO_INCREMENT PRIMARY KEY,
            author VARCHAR(255),
            title VARCHAR(255),
            section ENUM('technical', 'artistic', 'economic'),
            year_of_publication YEAR,
            pages INT,
            price DECIMAL(10, 2),
            type ENUM('manual', 'book', 'periodical'),
            copies INT,
            max_loan_days INT
          )
        ''')

        self.cursor.execute('''
          CREATE TABLE IF NOT EXISTS readers (
            reader_id INT AUTO_INCREMENT PRIMARY KEY,
            last_name VARCHAR(255),
            first_name VARCHAR(255),
            phone VARCHAR(25),
            address VARCHAR(255),
            course INT CHECK(course BETWEEN 1 AND 4),
            group_name VARCHAR(50)
          )
        ''')

        self.cursor.execute('''
          CREATE TABLE IF NOT EXISTS book_issues (
            issue_id INT AUTO_INCREMENT PRIMARY KEY,
            issue_date DATE,
            reader_id INT,
            book_id INT,
            FOREIGN KEY(reader_id) REFERENCES readers(reader_id),
            FOREIGN KEY(book_id) REFERENCES books(book_id)
          )
        ''')

    def insert_data(self, books_data, readers_data, book_issues_data):
        self.cursor.executemany(
            "INSERT INTO books (author, title, section, year_of_publication, pages, price, type, copies, max_loan_days) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            books_data)
        self.db.commit()

        self.cursor.executemany("INSERT INTO readers (last_name, first_name, phone, address, course, group_name) VALUES (%s, %s, %s, %s, %s, %s)",
                                readers_data)
        self.db.commit()

        self.cursor.executemany("INSERT INTO book_issues (issue_date, reader_id, book_id) VALUES (%s, %s, %s)", book_issues_data)
        self.db.commit()

    def clear_data(self):
        self.cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
        self.cursor.execute("TRUNCATE TABLE book_issues;")
        self.cursor.execute("TRUNCATE TABLE readers;")
        self.cursor.execute("TRUNCATE TABLE books;")
        self.cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
        self.db.commit()

    def query_books_published_after_2001(self):
        query = '''
            SELECT * FROM books
            WHERE year_of_publication > 2001
            ORDER BY title ASC;
        '''
        self.execute_and_print_query(query)

    def query_count_books_by_type(self):
        query = '''
            SELECT type, COUNT(*) AS count FROM books
            GROUP BY type;
        '''
        self.execute_and_print_query(query)

    def query_readers_who_borrowed_manuals(self):
        query = '''
            SELECT DISTINCT r.* FROM readers r
            JOIN book_issues bi ON r.reader_id = bi.reader_id
            JOIN books b ON bi.book_id = b.book_id
            WHERE b.type = 'manual'
            ORDER BY r.last_name ASC;
        '''
        self.execute_and_print_query(query)

    def query_books_by_section(self, section):
        query = f'''
            SELECT * FROM books
            WHERE section = '{section}';
        '''
        self.execute_and_print_query(query)

    def query_due_dates_for_borrowed_books(self):
        query = '''
            SELECT b.title, bi.issue_date, b.max_loan_days, 
                   DATE_ADD(bi.issue_date, INTERVAL b.max_loan_days DAY) AS due_date
            FROM book_issues bi
            JOIN books b ON bi.book_id = b.book_id;
        '''
        self.execute_and_print_query(query)

    def query_cross_count_books_by_section(self):
        query = '''
            SELECT section, type, COUNT(*) AS count
            FROM books
            GROUP BY section, type;
        '''
        self.execute_and_print_query(query)

    def execute_and_print_query(self, query):
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        column_names = [i[0] for i in self.cursor.description]
        print(f"{column_names}")
        for row in results:
            print(row)
        print("\n")

    def close(self):
        self.db.close()
