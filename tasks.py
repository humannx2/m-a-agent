from crewai import Task
from agents import CompanyWebsiteAnalyst
from tools import scrape_website_tool
from models import WebsiteData


scrape_website_task = Task(
    description="Scrape {company}'s website {website_url} for the company's value proposition, target audience, key products and services, and unique selling proposition.",
    expected_output=("Your goal is to extract the following structured data from the company website content:"
    "1. Value Proposition - What is the company trying to solve or offer?"
    "2. Target Customer - Who is their product aimed at?"
    "3. Key Product Features - What are the main product features mentioned?"),
    agent=CompanyWebsiteAnalyst,
    tools=[scrape_website_tool],
    output_pydantic=WebsiteData,
)







