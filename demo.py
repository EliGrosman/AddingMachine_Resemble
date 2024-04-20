# Import from wrapper.py 
from wrapper import Resemble_Wrapper, play_wav
import os

# Load Resemble API key and initialize Resemble_Wrapper
from dotenv import load_dotenv
load_dotenv()

resemble_api_key = os.environ["RESEMBLE_API_KEY"]
resemble = Resemble_Wrapper(resemble_api_key)


# List all projects
projects = resemble.list_projects()
print("All projects:\n", projects, "\n")

# List all available voices
voices = resemble.list_voices()
print("All voices:\n", voices, "\n")

title = "demo" # A title to help you find this clip. This also becomes your file name
text = "Hello, this is a test!" # The text for it to read out
project_uuid = projects[0]["uuid"] # Selects the uuid for the first project
voice_uuid = voices[0]["uuid"] # Selects the uuid for the first project

print("Example:")
print(f"   - Project uuid: {project_uuid}, ({projects[0]['name']})")
print(f"   - Voice uuid: {voice_uuid}, ({voices[0]['name']})")
print(f"   - Text to generate: \"{text}\"")


# Generate and download file to the output folder
output_path = resemble.generate(
    title=title,
    text=text,
    project_uuid=project_uuid,
    voice_uuid=voice_uuid,
    out_dir="./output"
)

# Play it back
play_wav(output_path)
