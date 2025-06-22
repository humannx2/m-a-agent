from crewai import Task
from agents import CompanyWebsiteAnalyst, MarketNewsResearcher
from tools import scrape_website_tool, serper_tool
from models import WebsiteData, MarketAnalysis


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

market_news_task = Task(
    description=(
        "You are tasked with performing detailed market research for a given company. "
        "Your job is to:\n"
        "Search the web for:\n"
        "- Recent news, announcements, or press coverage about the company (e.g., product launches, funding rounds, partnerships, controversies).\n"
        "- Identify and list 1-2 direct competitors offering similar products or targeting similar customers.\n"
        "How to proceed:\n"
        "- Use only credible sources (e.g., TechCrunch, Crunchbase, Forbes, company blogs, LinkedIn, etc.).\n"
        "- Prioritize recent results (within the last 6 months).\n"
        "- Do NOT invent or speculate. If a certain piece of data isn't found, clearly say so.\n\n"
    ),
    expected_output=("Your goal is to analyze the market and make a precise summary of {company}'s current standing in the market"
    "and top 2 competitors."),
    agent=MarketNewsResearcher,
    tools=[serper_tool],
    output_pydantic=MarketAnalysis
)







