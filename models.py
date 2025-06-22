from pydantic import BaseModel
from typing import List

class WebsiteData(BaseModel):
    value_proposition: str
    target_customer: str
    key_product_features: List[str]

class MarketAnalysis(BaseModel):
    news_summary: str
    competitors: List[str]

class InvestmentMemo(BaseModel):
    final_verdict: str
    confidence_score: float

class FullInvestmentMemo(BaseModel):
    company_name: str
    website_analysis:WebsiteData
    market_analysis: MarketAnalysis
    investment_memo: InvestmentMemo






