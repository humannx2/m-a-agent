from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crewai import Crew, Process
from tasks import scrape_website_task, market_news_task, memo_synthesis_task
from agents import CompanyWebsiteAnalyst, MarketNewsResearcher, LeadInvestmentAnalyst
from dotenv import load_dotenv
import uvicorn
from models import FullInvestmentMemo

# load the environment variables
load_dotenv()

app = FastAPI(
    title="M&A Analysis API",
    description="An API for running the M&A analysis crew to generate investment memos.",
    version="0.1.0"
)

class AnalysisInput(BaseModel):
    company: str
    website_url: str

@app.post("/analyse", response_model=FullInvestmentMemo)
async def analyse(data: AnalysisInput):
    """
    Takes a company name and website URL, and returns a full investment memo.
    """
    try:
        # create the input variables
        input_variables = {
            "company": data.company,
            "website_url": data.website_url
        }

        # create the crew
        crew = Crew(
            agents=[CompanyWebsiteAnalyst, MarketNewsResearcher, LeadInvestmentAnalyst],
            tasks=[scrape_website_task, market_news_task, memo_synthesis_task],
            process=Process.hierarchical,
            manager_llm="gpt-4o",
            verbose=True,
        )

        # kickoff the crew
        result = crew.kickoff(inputs=input_variables)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)








