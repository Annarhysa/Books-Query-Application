import requests

def get_subject(book_name):
    query_book = book_name.lower()
    query_book = query_book.replace(' ', '+')


    resp = requests.get(f'https://openlibrary.org/search.json?title={query_book}')
    info = resp.json()
    
    subjects = info['docs'][0]['subject']
    
    author_name = info['docs'][0]['author_name'][0]
    first_publish_year = info['docs'][0]['first_publish_year']
    
    book = book_name.title()

    print(f"->Author of '{book}' is {author_name}. It was first published in {first_publish_year}")
    
    print()
    
    return subjects

book_name1 = input()
book_name2 = input()
sub1 = get_subject(book_name1)
sub2 = get_subject(book_name2)

s1 = set(sub1)
s2 = set(sub2)

common = s1&s2
common = list(common)
common.sort()

print("COMMON SUBJECTS ARE:")
j = 1
for i in common:
    print(f"{j})", i)
    j = j+1
    