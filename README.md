Multi-Agent Level 1

Level 1 — Prompt Engineering (LLM-Only Smart Assistant)

This project is the first level of a multi-stage AI assignment.
At this level, we build a simple Python CLI chatbot that uses a Large Language Model (LLM) through the Gemini API.

The focus here is on prompt engineering:
	•	The chatbot always explains answers step-by-step.
	•	It refuses to solve arithmetic problems directly.
	•	It provides clear, structured outputs.

⸻

⚙️ Setup and Installation
	1.	Ensure you have Python 3.9 or higher installed.

  	
   2.	Clone this repository and navigate to the level1 directory.
	
 3.	Install the required dependencies:
            pip install -r ../requirements.txt
            
   		 The requirements.txt file includes:
                    •	google-generativeai
                    •	python-dotenv
   4.	Create a .env file in the same directory with your Gemini API key:

     		GEMINI_API_KEY=your_api_key_here
5.	Run the chatbot:

  			 python chatbot.py



💬 Example Interactions

   ✅ Example 1 — List Output
        You: what are the colors in a rainbow  
        Bot: 
            1. Red  
            2. Orange  
            3. Yellow  
            4. Green  
            5. Blue  
            6. Indigo  
            7. Violet


 ✅ Example 2 — Step-by-step Explanation     

        You: Tell me why the sky is blue?    
        Bot: 
                    The blue color of the sky is a result of a phenomenon called **Rayleigh scattering**. Here's a step-by-step explanation:

            1. **Sunlight is made of all colors:**  Sunlight appears white to us, but it's actually composed of all the colors of the rainbow.  Think of a prism separating white light into its constituent colors.

            2. **Sunlight enters the atmosphere:**  As sunlight enters the Earth's atmosphere, it collides with tiny air molecules (mostly nitrogen and oxygen).  These molecules are much smaller than the wavelengths of visible light.

            3. **Rayleigh scattering occurs:** This collision process is called Rayleigh scattering.  It's where light is scattered in all directions by the particles.  Crucially, the amount of scattering is inversely proportional to the fourth power of the wavelength.  This means shorter wavelengths are scattered much more strongly than longer wavelengths.

            4. **Blue light is scattered most:**  Blue and violet light have the shortest wavelengths in the visible spectrum.  Therefore, they are scattered much more effectively by the air molecules than longer wavelengths like red and orange.

            5. **We see the scattered blue light:**  This scattered blue light is what we see when we look at the sky.  Our eyes are also slightly more sensitive to blue than violet, contributing to the perception of a blue sky.

            6. **Why not violet?** While violet light is scattered even more than blue light, our eyes are less sensitive to violet, and the sun emits slightly less violet light than blue.  The combination of these factors results in a sky that appears blue rather than violet.

            7. **Sunsets are different:** At sunrise and sunset, the sunlight travels through a much thicker layer of atmosphere.  This means that most of the blue light is scattered away before it reaches our eyes, leaving the longer wavelengths like red and orange to dominate, resulting in the beautiful colors of sunrise and sunset. 


✅ Example 3 — Arithmetic Refusal

         You: What is 15 + 23?
         Bot: 
                I cannot perform calculations. Please use a calculator. 
✅ Example 4 — General Knowledge           
        	
		  You:  prime minister of India
         Bot:
                The current Prime Minister of India is **Narendra Modi**. 

<img width="1680" height="1050" alt="Screenshot 2025-09-10 at 18 35 15" src="https://github.com/user-attachments/assets/ff0ecaae-05e1-4266-a6c1-c7e0205d6b2e" />


