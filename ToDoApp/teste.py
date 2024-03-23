from dotenv import load_dotenv
import os 


load_dotenv()  # load environment variables from '.env' file.
url_postgresql = os.getenv("url_postgresql")
print(url_postgresql)  # Verifique se o valor é impresso corretamente.
