import requests
import bs4
import sqlite3

page=requests.get("https://govtjobguru.in/government-jobs-openings/")

soup= bs4.BeautifulSoup(page.text,'lxml')

table=soup.find('table',id="tablepress-285")

headers=[ heading.text.replace(",Other","") for heading in table.find_all('th')]
#print(headers)
table_rows=[ row for row in table.find_all('tr')]
#print(table_rows)


results=[{headers[index]:cell.text for index,cell in enumerate(row.find_all("td")) }for row in table_rows]
print(len(results))
print(results)
results_a = results[1:]
for x in results_a:
    if ('Organization' in x):
        print("Organization : " + x.get('Organization'))
    if ('Post Name' in x):
        print("post name : "+ x.get('Post Name'))
    if ('Qualification' in x):
        print("Qualification : " + x.get('Qualification'))
    if ('Deadline' in x):
        print("Deadline : " + x.get('Deadline'))
    print("\n")

    conn = sqlite3.connect('db.sqlite3')
    print("Opened database successfully");

    title = x.get('Post Name')
    company_name = x.get('Qualification')
    employment_status = "full times"
    category = "team leaders"
    description = x.get('Deadline')
    responsibilities = "responsible for the quality of the software products"
    experience = "2-3 yearss"
    job_location = x.get('Organization')
    Salary = "none"
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

