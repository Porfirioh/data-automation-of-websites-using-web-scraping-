from crawler import sublink_array
import requests
from bs4 import BeautifulSoup
import sqlite3
"""
conn = sqlite3.connect('sqlite3.db')
print("Opened database successfully");

conn.execute('''CREATE TABLE if not exists jobapp_jobpost
    (title TEXT ,
     header TEXT);
    ''')
print("table is created sussesfully")
"""

for sublinkurl in sublink_array:
    r = requests.get(sublinkurl)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')

    job_pages = soup.find('div', {'class':'pb-3'})

    titles = job_pages.find('h1')
    headers = job_pages.find('div', {'class':'pb-3 spmeta'})

    job_page_details = job_pages.find('div', {'class':'post-content'})

    descriptions = job_page_details.find('p')

    organization_soup = job_pages.find('div', {'class':'pb-2 pt-2'})

    organization = organization_soup.find('a')

    #conn.execute("INSERT INTO jobapp_jobpost (title, header) \
    #         VALUES (?, ?)", titles.text, headers.text);

    #conn.commit()
    #conn.close()

    print('title:', titles.text)
    print('header:', headers.text)
    print('description:', descriptions.text)
    print('organization:', organization.text)

    conn = sqlite3.connect('db.sqlite3')
    print("Opened database successfully");

    title = titles.text
    company_name = headers.text
    employment_status = "full times"
    category = "team leaders"
    description = descriptions.text
    responsibilities = "responsible for the quality of the software products"
    experience = "2-3 yearss"
    job_location = organization.text
    Salary = "N/A"
    image = "media/featured-listing-2.jpgs"
    application_deadline = "2019-12-27 00:00:00"
    published_on = "2019-11-27 15:43:18"
    user_id = "6"
    gender = "male"
    vacancy = "15"

    conn.execute("INSERT INTO jobs_joblisting (title, company_name, employment_status, category, description, responsibilities, experience, job_location, Salary, image, application_deadline, published_on, user_id, gender, vacancy) \
             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (title, company_name, employment_status, category, description, responsibilities, experience, job_location, Salary, image, application_deadline, published_on, user_id, gender, vacancy));
    print("records inserted successfully");


    conn.commit()
    conn.close()
