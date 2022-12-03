from vitrina.models import Books
from datetime import datetime
def cargar_datos_book():
    import json
    with open('book_to_clean.json', encoding="utf-8") as data_file:
        json_data = json.loads(data_file.read())
        for book_data in json_data:
            del book_data['bookID']

            if 'FIELD13' in book_data.keys():
                print('siuuuuuuuu')
                book_data['publication_date'] = book_data['publisher']
                book_data['publisher'] = book_data['FIELD13']
                del book_data['FIELD13']
                        

           
            book = Books.objects.create(
                title = book_data['title'],
                authors = book_data['authors'],
                average_rating= float(book_data['average_rating']) if len(book_data['average_rating'])==4 else 0.0,
                isbn= book_data['isbn'],
                isbn13= book_data['isbn13'],
                language_code= book_data['language_code'],
                num_pages= book_data['num_pages'],
                ratings_count= book_data['ratings_count'],
                text_reviews_count= book_data['text_reviews_count'],
                publication_date= datetime.strptime(book_data['publication_date'], "%m/%d/%Y"),
                publisher= book_data['publisher']
            )