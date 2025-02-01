import uvicorn

uvicorn.run("plantapp.main:app", reload=True, host="0.0.0.0", port=8888)