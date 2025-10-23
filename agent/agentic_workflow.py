from utils.model_loader import load_model
from prompt_library.prompt import SYTEM_PROMPT

from tools.weather_info_tool import WeatherInfoTool
from tools.destination_search_tool import DestinationSearchTool
from tools.calc_tool import CalcTool
from tools.currency_convert_tool import CurrencyConvertTool

from langgraph.graph import StateGraph, MessagesState, END, START
from langgraph.prebuilt import ToolNode, tools_condition




class GraphBuilder():

    def __init__(self):
        pass

    def agent_func(self):
        pass

    def build_graph(self):
        pass

    def __call__(self):
        pass