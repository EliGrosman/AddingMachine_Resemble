from wrapper import Resemble_Wrapper, play_wav
import os

from dotenv import load_dotenv
load_dotenv()

resemble_api_key = os.environ["RESEMBLE_API_KEY"]
resemble = Resemble_Wrapper(resemble_api_key)

projects = resemble.list_projects()
print("All projects:\n", projects, "\n")

voices = resemble.list_voices()
print("All voices:\n", voices, "\n")

text = "Hello, this is a test!"
title = "demo"
print("Example:")
print(f"   - Project uuid: {projects[0]['uuid']}, ({projects[0]['name']})")
print(f"   - Voice uuid: {voices[0]['uuid']}, ({voices[0]['name']})")
print(f"   - Text to generate: \"{text}\"")

output_path = resemble.generate(
    title=title,
    text=text,
    project_uuid=projects[0]["uuid"],
    voice_uuid=voices[0]["uuid"]
)

play_wav(output_path)
