#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from crewai.flow.flow import Flow, listen, start

from typing import Any
import json

from automate_linkedin_posts.crews.content_crew.content_crew import ContentCrew
from automate_linkedin_posts.crews.extraction_crew.extraction_crew import ExtractionCrew
from automate_linkedin_posts.crews.research_crew.research_crew import ResearchCrew

class WebContentState(BaseModel):
    url: str = ""
    question: str = ""
    raw_content: str = ""
    extracted_info: Any = None  # Allow any type of extracted info
    research_data: Any = None   # Allow any type of research data
    content: str = ""
    final_post: str = ""

class LinkedInContentFlow(Flow[WebContentState]):
    @start()
    def gather_user_input(self):
        print("Gathering input url.")
        self.state.url = input("Enter the url of the real estate property listing.")
        """Determine whether to start with extraction or research based on input"""

    @listen(gather_user_input)
    def initialize_flow(self):
        """Determine whether to start with extraction or research based on input"""
        print("Starting flow execution")
        if self.state.url:
            print("Starting content extraction from URL...")
            return self.extract_information()
        elif self.state.question:
            print("Starting research based on question...")
            return self.initialize_research()
        else:
            raise ValueError("Either url or question must be provided")

    def extract_information(self):
        """Extract information from a given URL"""
        print("Extracting content from URL...")
        result = ExtractionCrew().crew().kickoff(
            inputs={"url": self.state.url}
        )
        
        # Handle the result - if it's a string, try to parse it as JSON
        if isinstance(result.raw, str):
            try:
                data = json.loads(result.raw)
                # Handle potential nested JSON string
                if isinstance(data.get("main_content"), str) and data["main_content"].startswith("{"):
                    try:
                        nested_data = json.loads(data["main_content"])
                        data = nested_data
                    except json.JSONDecodeError:
                        pass
                self.state.extracted_info = data
            except json.JSONDecodeError:
                self.state.extracted_info = {
                    "property": {
                        "description": result.raw,
                        "amenities": [],
                        "contact_info": {}
                    }
                }
        else:
            self.state.extracted_info = result.raw
            
        return result

    def initialize_research(self):
        """Start the research process based on a question"""
        print("Researching answer to question...")
        result = ResearchCrew().crew().kickoff(
            inputs={"question": self.state.question}
        )
        self.state.research_data = result.raw
        return result

    @listen("initialize_flow")
    def create_content(self):
        """Create the LinkedIn content based on property data"""
        print("Creating LinkedIn content...")
        
        # Simply pass along whatever was extracted
        inputs = {
            "extracted_info": self.state.extracted_info,
            "url": self.state.url
        }
                
        result = ContentCrew().crew().kickoff(inputs=inputs)
        self.state.final_post = result.raw
        return result


def kickoff():
    linkedin_content_flow = LinkedInContentFlow()
    linkedin_content_flow.kickoff()


def plot():
    linkedin_content_flow = LinkedInContentFlow()
    linkedin_content_flow.plot()


if __name__ == "__main__":
    kickoff()
