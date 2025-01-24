import matplotlib.pyplot as plt
# import seaborn as sns
import os
from dotenv import load_dotenv

load_dotenv(".env")

gpt_key = os.getenv("Gptpassword")
print(gpt_key)