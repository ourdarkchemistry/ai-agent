#Установка + Запуск
##Шаг 1) Клонировать
git clone https://github.com/ourdarkchemistry/ai-agent.git
cd ai-agent

##Шаг 2) Установить зависимости
pip install -r requirements.txt
playwright install

##Шаг 3) Настроить API ключи
cp .env.example .env
vim .env  # добавить ключи

##Шаг 4) Запустить агента
python main.py
