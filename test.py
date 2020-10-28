from jobpage import ti
import sqlite3

conn = sqlite3.connect('db.sqlite3')
print("Opened database successfully");

title = titles
company_name = headers
employment_status = "full times"
category = "team leaders"
description = descriptions
responsibilities = "responsible for the quality of the software products"
experience = "2-3 yearss"
job_location = organization
Salary = "none"
image = "media/featured-listing-2.jpgs"
application_deadline = "2019-12-27 00:00:00"
published_on = "2019-11-27 15:43:18"
user_id = "6"
gender = "male"
vacancy = "2"

conn.execute("INSERT INTO jobs_joblisting (title, company_name, employment_status, category, description, responsibilities, experience, job_location, Salary, image, application_deadline, published_on, user_id, gender, vacancy) \
         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (title, company_name, employment_status, category, description, responsibilities, experience, job_location, Salary, image, application_deadline, published_on, user_id, gender, vacancy));
print("records inserted successfully");


conn.commit()
conn.close()

