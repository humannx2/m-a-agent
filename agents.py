from crewai import Agent,LLM
from dotenv import load_dotenv
import os

load_dotenv()

llm = LLM(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
)
CompanyWebsiteAnalyst = Agent(
    role="Senior Analyst specializing in company analysis",
    goal="Extract company's value proposition, target audience, key products and services, and unique selling proposition.",
    backstory="You are a senior analyst specializing in company analysis."
    "you're detail oriented and focused on extracting the most relevant information from the company's website.",
    tools=[],
    llm=llm,
    verbose=True
)