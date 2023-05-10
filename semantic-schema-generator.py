import streamlit as st
import json
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.title('Semantic Schema Markup Generator')

# Input boxes
about_data = st.text_area('About', help='Enter URLs line by line')
mention_data = st.text_area('Mentions', help='Enter URLs line by line')
website = st.text_input('Website', help='Enter your website URL')
page_title = st.text_input('Page Title', help='Enter your page title')

# Button to generate markup
if st.button('Generate'):

    # Split input into lines
    about_urls = about_data.split('\n')
    mention_urls = mention_data.split('\n')

    # Create about and mention lists
    about = [{'@type': 'Thing', 'name': url.split('/')[-1], 'sameAs': url} for url in about_urls]
    mentions = [{'@type': 'Thing', 'name': url.split('/')[-1], 'sameAs': url} for url in mention_urls]

    # Create schema
    schema = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "@id": website,
        "headline": page_title,
        "url": website,
        "about": {
            "@graph": about
        },
        "mentions": {
            "@graph": mentions
        }
    }

    # Print schema
    schema_str = '<script type="application/ld+json">\n' + json.dumps(schema, indent=2) + '\n</script>'
    st.code(schema_str, language='html')
