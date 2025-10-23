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
        self.tools=[
            WeatherInfoTool(),
            DestinationSearchTool(),
            CalcTool(),
            CurrencyConvertTool()
        ]

        self.system_prompt = SYTEM_PROMPT

    def agent_func(self, state: MessagesState):
        user_question = state["messages"]
        input_question = [self.system_prompt]+user_question
        resp = self.llm_with_tools.invoke(input_question)
        return {"messages":[resp]}

    def build_graph(self):
        graph_build = StateGraph(MessagesState)
        graph_build.add_node("agent",self.agent_func)
        graph_build.add_node("tools", ToolNode(tools=self.tools))
        graph_build.add_edge(START, "agent")
        graph_build.add_conditional_edges("agent",tools_condition)
        graph_build.add_edge("tools", "agent")
        graph_build.add_edge("agent", END)

        self.graph = graph_build.compile()

        return self.graph



    def __call__(self):
        return self.build_graph()