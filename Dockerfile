# 1. استخدم Python الرسمي
FROM python:3.11-slim

# 2. أنشئ مجلد للتطبيق
WORKDIR /app

# 3. انسخ ملفات المشروع
COPY . .

# 4. ثبّت المتطلبات
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 5. شغّل التطبيق
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
