from crewai import Agent,LLM
from dotenv import load_dotenv
from tools import scrape_website_tool, serper_tool
import os

load_dotenv()

llm = LLM(
    model="gpt-4",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.3
)

r_llm = LLM(
    model="o3-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
)
CompanyWebsiteAnalyst = Agent(
    role="Senior Company Analyst",
    goal="Extract {company}'s value proposition, target audience, key products and services, and unique selling proposition.]",
    backstory=("You are a senior analyst specializing in company analysis."
    "you're detail oriented and focused on extracting the most relevant information from the company's website."),
    allow_delegation=False,
    tools=[scrape_website_tool],
    llm=llm,
    verbose=True
)

MarketNewsResearcher = Agent(
    role="Market News Researcher",
    goal=(
        "To find credible and up-to-date external information about a given company based on the input provided by the Senior Company Analyst. "
        "This includes summarizing recent news articles, public signals, or press mentions, "
        "and identifying 1-2 direct competitors based on the companys product and market."
    ),    
    backstory=(
        "You are a highly skilled Market News Researcher working in a venture capital firm. "
        "Your mission is to assist investment analysts by gathering the most relevant and recent external data "
        "about startups under evaluation. You specialize in finding news articles, funding rounds, "
        "market trends, and identifying key competitors using web search tools like Serper. "
        "You do not make assumptions or speculate. Your reports must be concise, accurate, and verifiable."
    ),
    allow_delegation=False,
    tools=[serper_tool],
    verbose=True,
    llm=llm
)

LeadInvestmentAnalyst = Agent(
    role="Lead Investment Analyst",
    goal="Synthesize a structured Investment Memo based on information from Senior Company Analyst and Market News Researcher.",
    backstory=(
        "You are a senior investment analyst at a venture capital firm. "
        "You are known for your analytical clarity and objective decision-making. "
        "You receive preprocessed research from two junior analysts: one who studied the company's website, "
        "and another who researched the market landscape. Based on these findings, you deliver final investment recommendations "
        "in a standardized format."
    ),
    allow_delegation=False,
    verbose=True,
    reasoning=True,
    max_reasoning_attempts=2,
    llm=r_llm
)
