from bs4 import BeautifulSoup
import requests
import lxml
import time


"""
web scraping job information from timesjobs.com
"""
#input to filter jobs by specific skillset
print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')
#get url and build/scrape base logic
def find_jobs():
    url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-box')
    for index, job in enumerate(jobs):
    #after getting specific html elements, to get farther information, reference the data
    #stored in the first scrape i.e. job here to drill farther down
        date_posted = job.find('span', class_='sim-posted').span.text
        if 'few' in date_posted:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', ' ')
            skills = job.find('span', class_='srp-skills').text.replace(' ', ' ')
            more_info = job.header.h2.a['href'] #chain together to drill down
            if unfamiliar_skill not in skills:
                #assigning each post to a new file with info and the file name
                #as the index of each job post for clean separation
                with open(f"posts/{index}.txt", 'w') as f:
                    f.write(f"Company Name: {company_name.strip()}")
                    f.write(f"Skills: {skills.strip()}")
                    f.write(f"More Info: {more_info}")
                print(f"File saved: {index}")

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes to re-run...')
        time.sleep(time_wait * 600)





