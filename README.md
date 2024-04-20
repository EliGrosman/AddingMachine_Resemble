# Resemble Wrapper

Check out `demo.py` for example usage! It imports the necessary code from `wrapper.py` and shows the different functions that it has. Currently you are able to do the following:
- List all projects
- List all voices
- Generate text-to-speech for any text using your voices

If there's any other way I can help, let me or Mackenzie know!! 

## How to use
1. Copy `wrapper.py`, `.env`, and `requirements.txt` to your working directory
2. Create folder called outputs in your working directory
3. Edit `.env`, add your Resemble API Key provided by their website
4. In terminal, run `python -m pip install -r requirements.txt`
5. Add `from wrapper import Resemble_Wrapper, play_wav` to the top of your file
6. Initialize Resemble with `resemble = Resemble_Wrapper("YOUR_API_KEY")`