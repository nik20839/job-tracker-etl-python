
import requests
from bs4 import BeautifulSoup
import os

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)

print(response.status_code)


soup = BeautifulSoup(response.text, "html.parser")

results = soup.find_all("div", class_="card-content")

print(len(results))

# first_job = results[0]

# title = first_job.find("h2")


# company = first_job.find("h3")
# location = first_job.find("p")

# print(title.text)
# print(company.text)
# print(location.text)
job_data = []
for job in results:

    title = job.find("h2")
    company = job.find("h3")
    location = job.find("p")
    date = job.find("time")

    # print(title.text.strip())
    # print(company.text.strip())     
    # print(location.text.strip())

    if "python" in title.text.lower():
        job_data.append({
            "title": title.text.strip(),
            "company": company.text.strip(),
            "location": location.text.strip(),
            "date": date.text.strip()
        })
for item in job_data:
    print(item)
   

import pandas as pd

df = pd.DataFrame(job_data)
df.drop_duplicates(inplace=True)
print(df.shape)

print(os.path.exists("jobs.csv"))

if os.path.exists("jobs.csv"):
    old_df = pd.read_csv("jobs.csv")
    print(old_df.shape)

combined_df = pd.concat([old_df, df])

print(combined_df.shape)

combined_df.drop_duplicates(inplace=True)

print(combined_df.shape)

combined_df.to_csv("jobs.csv", index=False)
print("CSV file created successfully")