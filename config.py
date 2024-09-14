import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24255185"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "0b4ed6a0fa4fc5d7246cea90ad35af92")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://yadavjii:cIlZFjHD6RkFeh6S@cluster0.empcj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
