import streamlit as st
import requests
from PIL import Image
import io
import os
import random

class StabilityAIApp:
    def __init__(self):
        self.api_key = os.getenv("STABILITY_API_KEY", "")
        self.history = []
        self.current_image = None

    def generate_image(self, prompt, cfg_scale, steps, style_preset):
        url = "https://api.stability.ai/v2beta/stable-image/generate/core"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "image/*"
        }
        data = {
            "prompt": prompt,
            "cfg_scale": cfg_scale,
            "steps": steps,
            "style_preset": style_preset,
            "output_format": "png"
        }

        try:
            response = requests.post(url, headers=headers, files={"none": ''}, data=data)
            response.raise_for_status()
            return response.content
        except requests.exceptions.RequestException as e:
            st.error(f"Failed to generate image: {str(e)}")
            return None

def generate_random_prompt():
    locations = [
        "village", "city", "town", "hamlet", "metropolis", "settlement", "outpost", 
        "castle", "fortress", "palace", "dungeon", "cavern", "island", "mountain base",
        "forest clearing", "desert oasis", "space station", "underwater dome", "treehouse community",
        "floating sky city", "underground bunker", "crystal cave", "volcanic lair", "ice fortress",
        "coastal port", "jungle temple", "desert bazaar", "mountain monastery", "swamp village",
        "cloud kingdom", "subterranean city", "glacier outpost", "canyon settlement", "asteroid colony",
        "nomadic caravan", "flying airship", "dimensional nexus", "time-locked citadel", "quantum realm",
        "pocket universe", "sentient hive", "bioluminescent grotto", "terraformed moon", "virtual reality hub",
        "ancient ruins", "forgotten library", "haunted mansion", "abandoned factory", "enchanted garden",
        "mechanical clockwork city", "holographic projection", "mirror dimension", "geothermal spa town",
        "interdimensional crossroads", "astral plane sanctuary", "nanite swarm hive", "gravity-defying archipelago",
        "psychic commune", "shapeshifting labyrinth", "temporal archive", "elemental confluence", "dream weavers' loom",
        "cosmic lighthouse", "primordial soup ecosystem", "perpetual storm eye", "living fossil reef", "membrane bubble cluster",
        "quantum entangled twin cities", "fractal recursion habitat", "void energy well", "crystalline thought construct",
        "paradox loop district", "probability wave settlement", "dark matter oasis", "antimatter mirror world",
        "cosmic string tightrope town", "wormhole transit hub", "neutron star forge", "black hole event horizon colony",
        "quasar-powered metropolis", "hyperbolic space habitat", "fourth-dimensional tesseract complex", "string theory manifold",
        "multiverse intersection point", "temporal anomaly zone", "quantum foam bubble", "holographic universe projection",
        "parallel reality bleed", "cosmic microwave background embassy", "dark energy harvesting station",
        "quantum tunneling network", "superposition city", "entanglement encoder nexus", "wave function collapse point"
    ]
    
    themes = [
        "medieval", "futuristic", "steampunk", "cyberpunk", "fantasy", "post-apocalyptic", 
        "ancient", "magical", "sci-fi", "western", "tropical", "arctic", "industrial", 
        "ethereal", "gothic", "whimsical", "prehistoric", "alien", "retro", "dystopian",
        "utopian", "baroque", "renaissance", "art deco", "art nouveau", "minimalist", "maximalist",
        "surrealist", "impressionist", "expressionist", "cubist", "abstract", "realistic", "hyper-realistic",
        "cartoon", "anime", "manga", "chibi", "pixel art", "vaporwave", "synthwave", "dieselpunk",
        "atompunk", "nanopunk", "biopunk", "solarpunk", "lunarpunk", "stonepunk", "clockpunk",
        "elfpunk", "mythpunk", "silkpunk", "nowpunk", "raypunk", "atompunk", "biopunk",
        "biopunk", "cyberprep", "decopunk", "dieselpunk", "dreampunk", "dungeon punk", "elfpunk", 
        "gaslight fantasy", "gothic horror", "grimdark", "gunpowder fantasy", "historical fantasy",
        "lovecraftian", "magical realism", "new weird", "noble bright", "planetary romance", "science fantasy",
        "sword and sorcery", "weird west", "afrofuturism", "indigenous futurism", "gulf futurism",
        "hopepunk", "capepunk", "mannerpunk", "migrant punk", "neuromatic", "oceanpunk", "rococopunk",
        "salvagepunk", "greenpunk", "hydropunk", "icepunk", "islandpunk", "junglepunk", "meadowpunk",
        "mountainpunk", "cavepunk", "desertpunk", "tidalpunk", "volcanopunk", "atomic age", "cassette futurism",
        "cyber noir", "formicapunk", "franken-tech", "ghibli-punk", "kaleidopunk", "neonpunk", "New Wave", 
        "paleolithicpunk", "pascalpunk", "periapunk", "Raygun Gothic", "retraux", "steelpunk", "zeerust",
        "Libra-punk", "paperpunk", "plaguepunk", "woodpunk", "candlepunk", "stonerpunk", "bronzepunk", "sandalpunk"
    ]
    
    features = [
        "with towering spires", "surrounded by a moat", "hidden in mist", "with floating islands",
        "covered in neon lights", "overgrown with vegetation", "built into massive trees",
        "with interconnected bridges", "powered by steam engines", "with holographic projections",
        "guarded by mythical creatures", "with underground tunnels", "adorned with crystals",
        "with clockwork mechanisms", "shrouded in eternal twilight", "with portals to other realms",
        "built from salvaged spacecraft", "with sentient buildings", "protected by force fields",
        "with ever-shifting architecture", "suspended in anti-gravity fields", "enveloped in a time bubble",
        "constructed from living matter", "powered by thought energy", "with shape-shifting structures",
        "infused with elemental magic", "built on the back of a giant creature", "existing in multiple dimensions",
        "with buildings that grow like plants", "protected by an AI defense system", "with streets paved in precious gems",
        "illuminated by bioluminescent life forms", "with buildings that rearrange at will", "powered by perpetual motion machines",
        "constantly phasing in and out of reality", "with architecture defying laws of physics", "built from programmable matter",
        "with structures that respond to emotions", "protected by a quantum encryption field", "existing simultaneously in past and future",
        "with buildings that communicate telepathically", "powered by miniature stars", "with roads that reconfigure like puzzle pieces",
        "shielded by a membrane of pure energy", "built from crystallized memories", "with structures that adapt to weather extremes",
        "powered by tidal forces of multiple moons", "with buildings grown from genetically engineered seeds", "protected by time-locked forcefield",
        "illuminated by captured aurora borealis", "with structures that harvest dark matter", "powered by cosmic string vibrations",
        "built on a foundation of quantum foam", "with buildings that exist in superposition", "protected by probability manipulation field",
        "illuminated by Cherenkov radiation", "with architecture based on fractal patterns", "powered by zero-point energy",
        "built from metamaterials with impossible properties", "with structures that tap into ley line energy", "protected by a swarm of nanobots",
        "illuminated by artificial mini-suns", "with buildings that manipulate their own gravity", "powered by harnessed black hole radiation",
        "built on the edge of a space-time rift", "with structures that phase through parallel universes", "protected by a dyson sphere",
        "illuminated by bioluminescent creatures", "with architecture mimicking neural networks", "powered by converted vacuum energy",
        "built from self-repairing smart materials", "with buildings that manipulate local time flow", "protected by a reality distortion field",
        "illuminated by captured starlight", "with structures that exist partially in subspace", "powered by tachyon particles",
        "built on a mobius strip landscape", "with architecture inspired by impossible geometry", "protected by a sentient weather system",
        "illuminated by refracted light from other dimensions", "with buildings that manipulate their atomic structure", "powered by psionics"
    ]
    
    details = [
        "bustling with alien life", "where magic and technology coexist", "home to legendary heroes",
        "known for its grand bazaar", "famous for its gladiatorial arena", "with a dark secret",
        "celebrating an annual festival", "recovering from a recent calamity", "preparing for war",
        "in the middle of a robot rebellion", "experiencing a gold rush", "under siege by dragons",
        "hosting an interdimensional conference", "where time flows backwards", "defying gravity",
        "where dreams manifest physically", "ruled by an AI", "in the belly of a cosmic whale",
        "where emotions are traded as currency", "experiencing a renaissance of banned arts", "in the midst of a planar convergence",
        "where thoughts are visible", "governed by a council of elemental spirits", "trapped in a time loop",
        "where the laws of physics are mutable", "undergoing a metamorphosis", "at war with its mirror universe",
        "where music shapes reality", "inhabited by living constellations", "in harmony with nature and machine",
        "where shadows have a life of their own", "experiencing a merging of parallel timelines", "under quarantine due to a reality virus",
        "where probability is determined by popular vote", "in the process of ascending to a higher dimension", "ruled by a pantheon of capricious gods",
        "where the environment reacts to collective emotions", "staging a rebellion against fate itself", "where every citizen is part of a hive mind",
        "experiencing a sudden evolution of consciousness", "where dreams and reality are indistinguishable", "undergoing a phase of rapid technological singularity",
        "where the past, present, and future coexist", "inhabited by beings of pure energy", "where every action spawns a parallel universe",
        "governed by the principles of quantum politics", "experiencing a cultural exchange with extradimensional entities", "where art comes to life",
        "undergoing a reality rewrite", "where memories are shared collectively", "ruled by a coalition of artificial and organic intelligences",
        "where the very fabric of space-time is fraying", "experiencing a renaissance of psychic abilities", "under the protection of cosmic guardians",
        "where every individual exists in multiple states simultaneously", "governed by the principles of chaos theory", "in the process of merging with a digital realm",
        "where the laws of cause and effect are in constant flux", "experiencing a sudden shift in universal constants", "under the influence of a reality-warping anomaly",
        "where the boundaries between species are blurring", "ruled by a dynasty of time travelers", "experiencing a convergence of all possible futures",
        "where the collective unconscious manifests physically", "undergoing a transformation into a living superorganism", "where every story ever told becomes reality",
        "governed by an ever-changing pantheon of conceptual entities", "experiencing a breakdown of fundamental forces", "under siege by xenomorphic idea parasites",
        "where the observer effect dominates everyday life", "ruled by a quantum supercomputer", "experiencing a reality-wide debugging and system update",
        "where fictional characters seek refuge from their stories", "undergoing a cosmic trial by a galactic federation", "where every surface is an interface to the infosphere",
        "governed by a rotating committee of future versions of itself", "experiencing waves of spontaneous mass transfiguration", "under a memetic quarantine",
        "where the exploration of inner space is as vital as outer space", "ruled by a gestalt entity of all citizens' minds", "in the midst of a soft apocalypse"
    ]

    prompt = f"A {random.choice(themes)} {random.choice(locations)} {random.choice(features)}, {random.choice(details)}. Rendered as a detailed isometric pixel art in the style of classic RPG games."
    return prompt

def main():
    st.set_page_config(page_title="RPG Style Pixel-Art Level Generator", layout="wide")
    st.title("RPG Style Pixel-Art Level Generator")

    app = StabilityAIApp()

    # Sidebar for inputs
    st.sidebar.header("Image Generation Settings")
    
    use_random_prompt = st.sidebar.checkbox("Use Random Prompt", value=True)
    
    if use_random_prompt:
        prompt = generate_random_prompt()
        st.sidebar.text_area("Generated Prompt:", value=prompt, height=100, disabled=True)
    else:
        prompt = st.sidebar.text_area("Enter your image prompt:", 
                                      value="An isometric pixel-art village, with wooden houses, cobblestone streets, large trees, and detailed scenery in the style of 90s RPG games.",
                                      height=100)
    
    cfg_scale = st.sidebar.slider("CFG Scale:", min_value=0, max_value=35, value=7)
    steps = st.sidebar.slider("Steps:", min_value=10, max_value=50, value=30)
    style_preset = st.sidebar.selectbox("Style Preset:", ["pixel-art", "fantasy-art", "isometric"])

    if st.sidebar.button("Generate Image"):
        if not app.api_key:
            st.error("API key not set. Please check your environment variables.")
        else:
            with st.spinner("Generating image..."):
                image_data = app.generate_image(prompt, cfg_scale, steps, style_preset)
                if image_data:
                    app.current_image = Image.open(io.BytesIO(image_data))
                    app.history.append(prompt)
                    st.success("Image generated successfully!")

    # Main area for image display
    if app.current_image:
        st.image(app.current_image, caption="Generated Image", use_column_width=True)
        
        # Save image button
        if st.button("Save Image"):
            buffered = io.BytesIO()
            app.current_image.save(buffered, format="PNG")
            st.download_button(
                label="Download Image",
                data=buffered.getvalue(),
                file_name="generated_image.png",
                mime="image/png"
            )

    # Display generation history
    if app.history:
        st.sidebar.header("Generation History")
        for i, hist_prompt in enumerate(reversed(app.history[-5:])):  # Show last 5 prompts
            st.sidebar.text(f"{len(app.history)-i}. {hist_prompt[:50]}...")

if __name__ == "__main__":
    main()