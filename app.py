from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from agent.agentic_workflow import GraphBuilder
import os

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def travel_agent_query(query: QueryRequest):

    try:
        print(query)
        graph = GraphBuilder(model_provider="groq")
        re_act_app = graph()

        graph_png = re_act_app.get_graph().draw_mermaid_png()

        with open("graph.png", "wb") as f:
            f.write(graph_png)

        print(f"Graph PNG saved as graph.png at {os.getcwd()}")

        messages = {"messages": [query.question]}
        
        res = re_act_app.invoke(messages)

        if isinstance(res, dict) and "messages" in res:
            finalout = res["messages"][-1].content
        else:
            finalout = str(res)

        return JSONResponse(content={"answer": finalout})
    
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
