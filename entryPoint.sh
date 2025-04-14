#!/bin/bash

# Run the FastAPI Backend
uvicorn main:app --reload

# Run the streamlit app
streamlit run streamlit_app.py
