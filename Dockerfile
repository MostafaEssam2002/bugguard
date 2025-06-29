# 1.use python
FROM python:3.11-slim
# 2.create folder for app 
WORKDIR /app
# 3. copy project files 
COPY . .
# 4.install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# 5. run application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]