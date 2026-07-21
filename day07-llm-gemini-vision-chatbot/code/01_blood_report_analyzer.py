# ==========================================================
# Blood Report Analysis using Gemini Vision (Multimodal LLM)
# Compatible with google-genai >= 1.x
#
# Install:
#   pip install -U google-genai pillow python-dotenv
#
# SECURITY: API key is read from an environment variable / .env
# file - never hardcode it directly in the script.
# ==========================================================
import os
from google import genai
from PIL import Image
from dotenv import load_dotenv

# ----------------------------------------------------------
# Load API key from a local .env file (kept OUT of git, see .gitignore)
# .env file should contain one line: GEMINI_API_KEY=your_key_here
# ----------------------------------------------------------
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise EnvironmentError(
        "GEMINI_API_KEY not found. Create a .env file with:\n"
        "GEMINI_API_KEY=your_key_here"
    )

# ----------------------------------------------------------
# IMAGE PATH
# ----------------------------------------------------------
IMAGE_PATH = "blood_test.jpg"  # place your report image next to this script

# ----------------------------------------------------------
# Initialize Gemini Client
# ----------------------------------------------------------
client = genai.Client(api_key=API_KEY)

# ----------------------------------------------------------
# Check Image Exists
# ----------------------------------------------------------
if not os.path.exists(IMAGE_PATH):
    raise FileNotFoundError(f"Image not found: {IMAGE_PATH}")

image = Image.open(IMAGE_PATH)

# ----------------------------------------------------------
# Get Available Models
# ----------------------------------------------------------
print("Fetching available Gemini models...\n")
available_models = [m.name for m in client.models.list()]

# ----------------------------------------------------------
# Preferred Models (Newest First)
# ----------------------------------------------------------
preferred_models = [
    "models/gemini-3.5-flash",
    "models/gemini-3.1-flash-image",
    "models/gemini-3.1-flash-lite",
    "models/gemini-3.1-pro-preview",
    "models/gemini-flash-latest",
    "models/gemini-pro-latest",
    "models/gemini-2.0-flash",
    "models/gemini-2.0-flash-001",
    "models/gemini-2.0-flash-lite",
    "models/gemini-2.0-flash-lite-001"
]

model_name = None
for model in preferred_models:
    if model in available_models:
        model_name = model
        break

if model_name is None:
    print("\nNo compatible model found.")
    print("Available Models:")
    for m in available_models:
        print(m)
    exit()

print(f"Using Model: {model_name}\n")

# ----------------------------------------------------------
# Prompt
# ----------------------------------------------------------
prompt = """
You are an expert medical laboratory report analyzer.
Analyze the uploaded blood report carefully.
Return your response in the following format.
================================================
PATIENT REPORT SUMMARY
================================================
1. Extract every laboratory test into a markdown table.
Columns:
- Test Name
- Patient Value
- Normal Range
- Status (Low / Normal / High)
------------------------------------------------
2. Explain every abnormal value.
3. Mention possible causes.
4. Mention possible symptoms.
5. Suggest foods that may help.
6. Suggest lifestyle improvements.
7. Mention whether immediate doctor consultation is recommended.
8. Give an overall health summary.
9. Mention that this analysis is AI-assisted and not a medical diagnosis.
"""

# ----------------------------------------------------------
# Generate Response
# ----------------------------------------------------------
print("Analyzing report...\n")
try:
    response = client.models.generate_content(
        model=model_name,
        contents=[prompt, image]
    )
    print("=" * 80)
    print(response.text)
    print("=" * 80)

    with open("blood_report_analysis.txt", "w", encoding="utf-8") as f:
        f.write(response.text)

    print("\nAnalysis saved to: blood_report_analysis.txt")

except Exception as e:
    print("\nError while generating response:\n")
    print(e)