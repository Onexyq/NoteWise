#HackSC 2023
#Authors: Boshe Zhang, Yiqi Xue, Zhiyuan Zhangm, Ying Sun

from fastapi import FastAPI, Request
import uvicorn
from process import get_mind_map, get_explanation

# build flask app
app = FastAPI()


@app.get("/api")
async def base():
    return "NoteWise API"


@app.post('/api/mindmap')
async def api_mindmap(request: Request):
    data = await request.body()
    text_data = data.decode('utf-8')
    print(text_data)   
    processed_data = await get_mind_map(text_data)
    print(processed_data)
    return processed_data



@app.post('/api/explain')
async def api_explanation(request: Request):
    data = await request.body()
    text_data = data.decode('utf-8')    
    processed_data = await get_explanation(text_data)
    print(processed_data)
    return processed_data


if __name__ == "__main__":
    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=8080,
        log_level="info",
        access_log=True,
        use_colors=True,
        proxy_headers=True,
    )
