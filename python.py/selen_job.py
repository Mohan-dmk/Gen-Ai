import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Step 1: Setup
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.dice.com/jobs?q=data+scientist&location=Boston,%20MA,%20USA")

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[@data-testid='job-search-serp-card']"))
)

job_cards = driver.find_elements(By.XPATH, "//div[@data-testid='job-search-serp-card']")
job_data = []

# Step 2: Loop through top 20 job cards
for card in job_cards[:15]:
    try:
        job_url = card.find_element(By.XPATH, ".//a[@data-testid='job-search-job-card-link']").get_attribute("href")
    except:
        continue

    try:
        company = card.find_element(By.XPATH, ".//p[contains(@class,'text-sm') and string-length(text()) > 1]").text.strip()
    except:
        company = "N/A"

    try:
        location = card.find_element(By.XPATH, ".//p[contains(text(),'Remote') or contains(text(),'Boston') or contains(text(),'Massachusetts')]").text.strip()
    except:
        location = "N/A"

    try:
        salary = card.find_element(By.XPATH, ".//p[contains(text(),'USD')]").text.strip()
    except:
        salary = "N/A"

    # Step 3: Visit job detail page to extract title
    driver.execute_script("window.open(arguments[0]);", job_url)
    driver.switch_to.window(driver.window_handles[1])

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//a[@data-testid='job-search-job-detail-link']"))
        )
        job_title = driver.find_element(By.XPATH, "//a[@data-testid='job-search-job-detail-link']").text.strip()
    except:
        try:
            job_title = driver.find_element(By.XPATH, "//h1").text.strip()
        except:
            job_title = "N/A"

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    job_data.append([job_title, company, location, salary, job_url])
    print(f"✔ {job_title} | {company} | {location} | {salary}")

# Step 4: Save to CSV
with open("dice_jobs.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Job Title", "Company", "Location", "Salary", "Job URL"])
    writer.writerows(job_data)

print(f"\n✅ Saved {len(job_data)} jobs to dice_jobs.csv")
driver.quit()
