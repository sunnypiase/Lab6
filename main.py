from DatabaseManager import DatabaseManager

if __name__ == '__main__':
    try:
        manager = DatabaseManager("localhost", "root", "password", "lib_db")

        manager.setup_db()
        manager.clear_data()

        # These would be defined somewhere with the actual data
        books_data = [
            ('Madeline Diaz', 'Actually worry above guess', 'artistic', 2016, 163, 89.73, 'periodical', 5, 22),
            ('William Luna', 'Hope world glass', 'economic', 2004, 992, 159.97, 'book', 2, 49),
            ('David Young', 'Beat case research hear yeah', 'economic', 1995, 794, 188.16, 'book', 2, 19),
            ('Stephanie Hunt', 'Report exist property degree general', 'technical', 2017, 116, 192.8, 'manual', 1, 8),
            ('Jason Bell', 'Mean suffer difficult choice', 'technical', 2014, 914, 198.67, 'book', 1, 8),
            ('Abigail Powell', 'College her', 'technical', 2016, 641, 130.45, 'manual', 2, 30),
            ('Andrew Jones', 'Test thank agree other', 'economic', 2011, 856, 94.1, 'book', 1, 48),
            ('Anna Shah', 'Push speech institution could', 'economic', 2013, 71, 71.75, 'book', 5, 52),
            ('Alexa Johnson', 'Him different result memory', 'economic', 1997, 314, 67.16, 'periodical', 3, 31),
            ('Amber Jennings', 'Bring growth state strong', 'artistic', 1996, 91, 126.08, 'manual', 5, 47),
            ('Henry Wells', 'Walk product law', 'technical', 2000, 813, 104.15, 'manual', 2, 34),
            ('Jessica Ellis', 'Role tend yourself important', 'economic', 2013, 591, 87.09, 'book', 4, 30),
            ('Aaron Smith', 'No Republican meeting ask', 'economic', 2010, 167, 13.14, 'book', 5, 35),
            ('Joshua Waters', 'Evening whatever card individual possible', 'technical', 2001, 516, 91.7, 'periodical', 1, 35)
        ]

        readers_data = [
            ('Horton', 'Sally', '120-029-7564', '5866 Lauren Plaza Apt. 852, Port Melissa, WA 38463', 1, 'Group 13'),
            ('Smith', 'Ryan', '120-029-7564', '246 Stewart Trafficway Suite 514, West Eric, MO 76619', 2, 'Group 3'),
            ('Beasley', 'Christopher', '120-029-7564', '636 Richard Forest Apt. 254, Douglasshire, VA 20077', 1, 'Group 5'),
            ('Allen', 'Miranda', '120-029-7564', 'PSC 5373, Box 4408, APO AP 42464', 3, 'Group 20'),
            ('Sanchez', 'Stephanie', '120-029-7564', '1741 Church Causeway Suite 411, North Gabrielfort, SC 93613', 2, 'Group 8'),
            ('Knight', 'Tamara', '120-029-7564', '87088 Potter Corner, North Mary, RI 74089', 2, 'Group 10'),
            ('Mendez', 'Aaron', '120-029-7564', '43796 Jason Ports Suite 305, Smithland, WI 54674', 2, 'Group 5'),
            ('Cooper', 'Tyrone', '120-029-7564', '94549 Justin Streets, West Joshuamouth, NJ 33003', 1, 'Group 18'),
            ('Campbell', 'Theresa', '120-029-7564', '821 Davis Glen, Michaelside, CT 66253', 1, 'Group 13')
        ]
        book_issues_data = [('2001-05-18', 4, 12),
                            ('2018-01-28', 1, 1),
                            ('1996-11-09', 3, 10),
                            ('2012-04-15', 7, 4),
                            ('2011-10-07', 8, 9),
                            ('2018-11-28', 2, 12),
                            ('2021-08-15', 1, 5),
                            ('2022-11-28', 6, 3),
                            ('2001-10-23', 7, 9),
                            ('2002-04-08', 9, 8),
                            ('2000-05-11', 3, 9)]

        manager.insert_data(books_data, readers_data, book_issues_data)

        print("1. Всі книги видані після 2001 року:")
        manager.query_books_published_after_2001()
        print("2. Кількість книг кожного виду:")
        manager.query_count_books_by_type()
        print("3. Всі читачі, що брали посібники:")
        manager.query_readers_who_borrowed_manuals()
        print(f"4. Всі книги з розділу technical:")
        manager.query_books_by_section('technical')
        print("5. Кінцевий термін повернення кожної книги:")
        manager.query_due_dates_for_borrowed_books()
        print("6. Кількість видань в кожному розділі:")
        manager.query_cross_count_books_by_section()

        manager.close()
    except Exception as e:
        print(f"An error occurred: {e}")
