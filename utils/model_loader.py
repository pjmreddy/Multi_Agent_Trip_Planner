from pydantic import BaseModel, Field
from typing import Literal, Optional, Any
import os
from dotenv import load_dotenv
from utils.config_loader import load_config
from langchain_groq import ChatGroq

load_dotenv()

class ConfigLoader(BaseModel):
    def __init__(self):
        print("Loading configuration...")
        self.config = load_config()

    def __getitem__(self, key):
        return self.config[key]

class ModelLoader(BaseModel):
    llm_provider: Literal['groq']
    config: Optional[ConfigLoader]= Field(default=None, exclude=True)

    def model_post__init__(self, __context: Any) -> None:
        self.config = ConfigLoader()

    class Config:
        arbitery_types_allowed = True

    def load_model(self):
        print("LLM is loading...")
        print(f"LLM is loading from the provider:{self.llm_provider}")

        if self.llm_provider == 'groq':
            print("Loading Groq LLM model...")
            groq_api_key = os.getenv("GROQ_API_KEY")
            model_name = self.config.llm.groq.model_name
            llm = ChatGroq(model=model_name, api_key=groq_api_key)

        return llm



        

