import os
import streamlit as st
import google.generativeai as genai

# ------------- CONFIGURE GEMINI API KEY -------------
API_KEY = os.getenv("GEMINI_API_KEY")

if API_KEY is None:
    st.error(
        "GEMINI_API_KEY is not set. "
        "Add it as an environment variable locally or in Streamlit Cloud secrets."
    )
else:
    genai.configure(api_key=API_KEY)

# ------------- INITIALIZE MODEL -------------
def get_model():
    if API_KEY is None:
        return None
    # You can also use "gemini-1.5-pro" if available
    return genai.GenerativeModel("models/gemini-flash-latest")


# ------------- HELPER: BUILD PROMPT -------------
def build_prompt(platform, tone, content_type, language, brand_desc, niche, goal, num_posts):
    return f"""
You are an expert social media content strategist AI called ContentCraft.

Generate high-quality social media content ONLY in {language}.

Platform: {platform}
Tone of voice: {tone}
Content Type: {content_type}
Number of post ideas/captions: {num_posts}

Brand / Business Description:
{brand_desc}

Niche / Industry:
{niche}

Campaign / Goal:
{goal}

Instructions:
- Return content in a clean, numbered list.
- For each idea, give:
  - A short title (3–6 words)
  - Main caption (2–4 lines)
  - 3–8 relevant hashtags.
- Adapt style to the selected platform.
- Do NOT add any extra explanation outside the content.
"""


# ------------- STREAMLIT UI -------------
def main():
    st.set_page_config(
        page_title="ContentCraft – Social Media AI Agent",
        page_icon="✨",
        layout="centered"
    )

    st.title("✨ ContentCraft – AI Social Media Agent")
    st.write(
        "Generate **captions, post ideas, and content plans** for your brand using the free **Gemini API**."
    )

    with st.sidebar:
        st.header("⚙️ Content Settings")

        platform = st.selectbox(
            "Platform",
            ["Instagram", "LinkedIn", "Twitter/X", "YouTube", "Facebook"]
        )

        tone = st.selectbox(
            "Tone of Voice",
            ["Casual", "Professional", "Humorous", "Inspirational", "Bold", "Friendly"]
        )

        content_type = st.selectbox(
            "Content Type",
            [
                "Single Post Captions",
                "Carousel Ideas",
                "Short Video/Reel Ideas",
                "Thread / LinkedIn Post",
                "Weekly Content Plan"
            ]
        )

        language = st.selectbox(
            "Content Language",
            ["English", "Hindi", "Kannada", "Tamil", "Telugu"]
        )

        num_posts = st.slider(
            "Number of ideas/captions",
            min_value=1,
            max_value=10,
            value=5
        )

    st.subheader("🧩 Brand / Business Details")

    brand_desc = st.text_area(
        "Describe your brand or client",
        placeholder="Example: A small café in Bangalore that sells handcrafted coffee and snacks..."
    )

    niche = st.text_input(
        "Niche / Industry",
        placeholder="e.g., Fitness, EdTech, Fashion, SaaS, Café"
    )

    goal = st.text_area(
        "Goal of this content",
        placeholder="Example: Increase followers, promote a Diwali offer, launch a new product..."
    )

    generate_button = st.button("🚀 Generate Content")

    if generate_button:
        if API_KEY is None:
            st.error("GEMINI_API_KEY is missing. Please configure it first.")
            return

        if not brand_desc or not niche or not goal:
            st.warning("Please fill all fields before generating content.")
            return

        with st.spinner("Generating content with Gemini..."):
            prompt = build_prompt(
                platform=platform,
                tone=tone,
                content_type=content_type,
                language=language,
                brand_desc=brand_desc,
                niche=niche,
                goal=goal,
                num_posts=num_posts
            )

            try:
                model = get_model()
                response = model.generate_content(prompt)
                content = response.text

                st.subheader("📌 Generated Content")
                st.write(content)

                st.success("Content generated successfully! You can copy and use it directly.")
            except Exception as e:
                st.error(f"Something went wrong while calling Gemini API: {e}")


if __name__ == "__main__":
    main()
