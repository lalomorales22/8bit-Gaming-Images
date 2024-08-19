# RPG Style Pixel-Art Level Generator
<img width="883" alt="Screenshot 2024-08-19 at 9 13 38 AM" src="https://github.com/user-attachments/assets/a2c7b1ae-2a2d-43c2-a9f1-8f785b699f21">

This Streamlit app generates unique, RPG-style pixel art images of game levels, villages, and cities using the Stability AI API. It features a random prompt generator for creating diverse and imaginative scenes.

## Features

- Generate pixel art images of RPG-style levels, villages, and cities
- Random prompt generator for unique scene descriptions
- Customizable image generation parameters
- Option to use custom prompts
- Image download functionality
- Generation history display

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- A Stability AI API key (sign up at https://platform.stability.ai/)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/rpg-pixel-art-generator.git
   cd rpg-pixel-art-generator
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Stability AI API key:
   - Create a `.env` file in the project root directory
   - Add your API key to the file:
     ```
     STABILITY_API_KEY=your_api_key_here
     ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your web browser and go to the URL displayed in the terminal (usually `http://localhost:8501`).

3. Use the sidebar to configure your image generation:
   - Toggle "Use Random Prompt" to generate random scene descriptions
   - Adjust CFG Scale, Steps, and Style Preset as desired
   - Click "Generate Image" to create your pixel art level

4. View the generated image in the main area of the app.

5. Click "Save Image" to download the generated image.

6. Check the "Generation History" in the sidebar to see your recent prompts.

## Customization

You can customize the app's appearance by modifying the `.streamlit/config.toml` file. The current theme is set to a retro-futuristic dark mode that complements the pixel art aesthetic.

## Contributing

Contributions to the RPG Style Pixel-Art Level Generator are welcome. Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Stability AI](https://stability.ai/) for providing the image generation API
- [Streamlit](https://streamlit.io/) for the web app framework

## Contact

If you have any questions or feedback, please open an issue on this repository.

Enjoy generating your unique RPG-style pixel art levels!
