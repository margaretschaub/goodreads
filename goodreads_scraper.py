from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import math


#  Takes into account how many books are shown per page to generate url links
def find_number_of_pages(user_id):
    r = requests.get(f"https://www.goodreads.com/review/list/{user_id}?page=1&shelf=read")
    soup = BeautifulSoup(r.content, "lxml")
    items_statement = soup.find('div', id="infiniteStatus").text
    book_count_list = re.findall(r'\d+', items_statement)
    items_per_page = int(book_count_list[0])
    total_items = int(book_count_list[1])
    pages_in_links_upper = math.ceil(total_items/items_per_page)
    return pages_in_links_upper


def export_goodreads_data(user_id, pages_in_links_upper, output_file):

    dm = []

    for x in range(1, pages_in_links_upper+1):
        url_form = f"https://www.goodreads.com/review/list/{user_id}?page={x}&shelf=read"

        # Scrape the title
        title_list = []
        r = requests.get(url_form)
        soup = BeautifulSoup(r.content, "lxml")
        titles = soup.find_all('td', class_="field title")
        for each in titles:
            title = each.contents[1].text.strip()
            title_list.append(title)

        # Scrape the author
        author_list = []
        authors = soup.find_all('td', class_="field author")
        for each in authors:
            almost_author = each.contents[1].text
            author = almost_author.replace("*", "").strip()
            author_list.append(author)

        # Scrape the isbn
        isbn_list = []
        isbns = soup.find_all('td', class_="field isbn13")
        for each in isbns:
            isbn = each.contents[1].text.strip()
            isbn_list.append(isbn)

        # Scrape number of pages
        pages_list = []
        pages = soup.find_all('td', class_="field num_pages")
        for each in pages:
            almost_page_count = each.contents[1].text
            page_count = almost_page_count.replace("pp", "").strip()
            pages_list.append(page_count)

        # Scrape average rating
        ratings_list = []
        ratings = soup.find_all('td', class_="field avg_rating")
        for each in ratings:
            ratings = each.contents[1].text.strip()
            ratings_list.append(ratings)

        # Scrape number of ratings
        ratings_num_list = []
        ratings_num = soup.find_all('td', class_="field num_ratings")
        for each in ratings_num:
            number_of_ratings = each.contents[1].text.strip()
            ratings_num_list.append(number_of_ratings)

        # Scrape date published
        dates_list = []
        dates_published = soup.find_all('td', class_="field date_pub")
        for each in dates_published:
            date = each.contents[1].text.strip()
            dates_list.append(date)

        # Scrape date read:
        dates_read_list = []
        dates_read = soup.find_all('td', class_="field date_read")
        for each in dates_read:
            date_read = each.contents[1].text.strip()
            dates_read_list.append(date_read)

        zip_create = zip(title_list, author_list, isbn_list, pages_list, ratings_list, ratings_num_list, dates_list,
                         dates_read_list)

        for item in zip_create:
            dm.append(item)

    # Move it into a dataframe and print to a csv
    df = pd.DataFrame(dm, columns=['Title', 'Author', 'ISBN', 'Page Count', 'Ratings', 'Number of Ratings',
                                   'Publication Date', 'Date Finished'])

    df.to_csv(output_file)
    print("GoodReads data successfully exported")


def main():
    user_id = 145198074
    output_file = r'/Users/margaretschaub/Desktop/Goodreads_log.csv'
    pages_in_links_upper = find_number_of_pages(user_id)
    export_goodreads_data(user_id, pages_in_links_upper, output_file)


if __name__ == "__main__":
    main()
