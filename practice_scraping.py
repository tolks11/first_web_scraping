from bs4 import BeautifulSoup
"""""
fake html document that would be scraping
THIS COULD EASILY BE THE BEGINNING OF A SCRIPT TO GET INFO FROM A PAGE 
WHEN THE PRICE OF THE THING YOU'RE MONITORING IS CHNAGING
i.e. xyz costs $abc --> alerts when price reaches a certain point
"""""
#program to scrape the data of specific HTML tags/buttons
with open('file_name.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text










