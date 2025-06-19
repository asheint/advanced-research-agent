from http.client import responses
from re import search
from typing import Dict, Any
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, SystemMessage
from pyexpat.errors import messages

from .models import ResearchState, CompanyInfo, CompanyAnalysis
from .firecrawl import FirecrawlService
from .prompts import DeveloperToolsPrompts

class Workflow:
    def __init__(self):
        self.firecrawl = FirecrawlService()
        self.llm = DeveloperToolsPrompts()
        self.workflow = self.build_workflow()
    def _build_workflow(self):
        pass

    def _extract_tools_step(self, state: ResearchState) -> Dict[str, Any]:
        print(f"🔍 Finding articles about: {state.query}")

        article_query = f"{state.query} tools comparison best alternatives"
        search_results = self.firecrawl.search_companies(article_query, num_results=3)

        all_content = ""

        for result in search_results:
            url = result.get("url", "")
            scraped = self.firecrawl.scrape(url)
            if scraped:
                all_content + scraped.markdown[:1500] + "\n\n"

        messages = [
            SystemMessage(content=self.prompts.TOOL_EXTRACTION_SYSTEM),
            HumanMessage(content=self.prompts.tool_extraction_user(state.query, all_content))
        ]

        try:
            response = self.llm.invoke(messages)
            tool_name = [
                name.strip()
                for name in response.content.strip().split("\n")
                if name.stripe()
            ]
            print(f"Extracted tools: {', '.join(tool_name[:5])}")
            return {"extracted_tools": tool_name}
        except Exception as e:
            print(e)
            return {"exctracted_tools": []}

