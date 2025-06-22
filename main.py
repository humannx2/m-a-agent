from crewai import Crew,Process
from tasks import scrape_website_task,market_news_task
from agents import CompanyWebsiteAnalyst,MarketNewsResearcher
from dotenv import load_dotenv

# load the environment variables
load_dotenv()

# get the company name and website url from the user
print("Enter the company name: ")
company = input()
print("Enter the website URL: ")
website_url = input()
print("Starting the crew...")

# create the crew
crew = Crew(
    agents=[CompanyWebsiteAnalyst,MarketNewsResearcher],
    tasks=[scrape_website_task,market_news_task],
    process=Process.sequential,
    verbose=True,
)

# create the input variables
input_variables = { 
    "company": company,
    "website_url": website_url
}

# kickoff the crew
try:
    result = crew.kickoff(inputs=input_variables)
    print(result.raw)
except ValueError as e: # if the input variables are not provided, the crew will raise a ValueError
    print(f"Error: {e}")








