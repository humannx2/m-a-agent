from crewai import Crew,Process
from tasks import scrape_website_task, market_news_task, memo_synthesis_task
from agents import CompanyWebsiteAnalyst, MarketNewsResearcher, LeadInvestmentAnalyst
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
    agents=[CompanyWebsiteAnalyst, MarketNewsResearcher, LeadInvestmentAnalyst],
    tasks=[scrape_website_task, market_news_task, memo_synthesis_task],
    # process=Process.sequential,
    process=Process.hierarchical,
    manager_llm="gpt-4o",
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








