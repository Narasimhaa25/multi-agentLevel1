# multi-agent
Level 1 — Prompt Engineering (LLM-Only Smart Assistant)

This project is the first level of a multi-stage AI assignment. At this level, we build a simple Python CLI chatbot that uses a Large Language Model (LLM) through the Gemini API. The focus here is on prompt engineering, ensuring that the chatbot always explains answers step-by-step, refuses to solve arithmetic problems directly, and gives clear structured outputs.

To run this project, first make sure you have Python 3.9 or higher installed on your system. Clone this repository and navigate to the level1 directory. Install the required dependencies by running:

**pip install -r ../requirements.txt**


The requirements.txt file includes the following:



google-generativeai
python-dotenv


Next, create a .env file in the same directory with your Gemini API key:

GEMINI_API_KEY=your_api_key_here

Once dependencies are installed and the API key is set up, you can run the chatbot using:


python chatbot.py

When you run the chatbot, it will prompt you for input. You can ask questions such as:

You: what are the colors in a rainbow
Bot: 1. Red
2. Orange
3. Yellow
4. Green
5. Blue
6. Indigo
7. Violet 

You: tell me why the sky is blue
Bot: The blue color of the sky is a result of a phenomenon called Rayleigh scattering. Here's a step-by-step explanation:

1. **Sunlight is composed of all colors:**  Sunlight appears white to us, but it's actually made up of all the colors of the rainbow, each with a different wavelength.  Violet and blue have the shortest wavelengths, while red and orange have the longest.

2. **Sunlight enters the atmosphere:**  As sunlight enters the Earth's atmosphere, it collides with tiny air molecules (mostly nitrogen and oxygen).

3. **Rayleigh scattering occurs:**  These air molecules are much smaller than the wavelengths of visible light.  When light interacts with particles smaller than its wavelength, Rayleigh scattering occurs. This scattering effect is inversely proportional to the fourth power of the wavelength.  This means shorter wavelengths are scattered *much* more strongly than longer wavelengths.

4. **Blue and violet light are scattered most:** Because blue and violet light have the shortest wavelengths, they are scattered in all directions by the air molecules much more effectively than the longer wavelengths like red and orange.

5. **We see the scattered blue light:** This scattered blue light reaches our eyes from all directions, making the sky appear blue.

6. **Why not violet?** While violet light is scattered even more than blue light, our eyes are less sensitive to violet, and the sun emits slightly less violet light than blue.  This is why the sky appears blue rather than violet.

7. **Sunsets and sunrises are different:** At sunrise and sunset, the sunlight travels through a much longer path in the atmosphere.  This means more of the blue light is scattered away, leaving the longer wavelengths like red and orange to reach our eyes, resulting in the reddish hues we see during those times.



You: What is 15 + 23?
Bot: I cannot perform calculations. Please use a calculator. 




