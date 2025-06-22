from crewai import Task
from agents import CompanyWebsiteAnalyst, MarketNewsResearcher, LeadInvestmentAnalyst
from tools import scrape_website_tool, serper_tool
from models import WebsiteData, MarketAnalysis, FullInvestmentMemo


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
        "- Use only credible sources.\n"
        "- Prioritize recent results (within the last 6 months).\n"
        "- Do NOT invent or speculate. If a certain piece of data isn't found, clearly say so.\n\n"
    ),
    expected_output=("Your goal is to analyze the market and make a precise summary of {company}'s current standing in the market"
    "and top 2 competitors."),
    agent=MarketNewsResearcher,
    tools=[serper_tool],
    output_pydantic=MarketAnalysis
)

memo_synthesis_task = Task(
    description=(
        "Your task is to create a structured investment memo about {company} based of the information you recieved from Senior Company Analyst and Market News Researcher.\n\n"
        "Guidelines:\n"
        "- Be objective and concise.\n"
        "- Highlight market opportunity, product strength, and possible risks.\n"
        "- Do not make up information — only base your judgment on the provided structured inputs.\n"
    ),
    expected_output=("A detailed Investment Memo with all the company details like"
    "Value Proposition, Target Customer, Key Product Features"
    "news_summary, competitors"
    "and final verdict on Investing in the company with a confidence rating between 1-10, 1 is lowest, while 10 is highest"),
    agent=LeadInvestmentAnalyst,
    output_pydantic=FullInvestmentMemo,
    output_file='investment_memo.json'
)








