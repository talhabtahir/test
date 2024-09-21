import streamlit as st

# Add a mock GitHub link for testing
st.write("This is a test app.")
st.markdown('[Mock GitHub Link](https://github.com/talhabtahir/test/blob/main/testapp.py)', unsafe_allow_html=True)

# Add the footer
st.write("This is the footer.")

# Custom CSS to test hiding GitHub link
hide_github_links_style = """
<style>
a[href*="github.com"] {
    display: none !important; /* Hides any link containing 'github.com' */
}
</style>
"""
# import streamlit as st

# Custom CSS to hide only GitHub repo and fork links, but keep the main menu visible
hide_github_links_style = """
<style>
/* Keep the Streamlit main menu visible */
#MainMenu {visibility: visible;}

/* Target specific GitHub and fork links using attributes */
/* Hide the GitHub repo link */
a[href*="github.com"] { 
    display: none !important; 
}

/* Hide the fork link if it has a unique class or identifier */
/* Example: */
.stApp .css-1q1n0ol a[aria-label="View source"] { 
    display: none !important; 
}

/* This selector targets any 'iframe' with 'github.com' in its src attribute */
iframe[src*="github.com"] {
    display: none !important;
}
</style>
"""

# # Inject the custom CSS into the Streamlit app
# st.markdown(hide_github_links_style, unsafe_allow_html=True)

# Inject the custom CSS
st.markdown(hide_github_links_style, unsafe_allow_html=True)
