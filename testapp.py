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
import streamlit as st

# CSS to hide specific GitHub elements using more specific selectors
hide_github_links_style = """
<style>
/* Make sure the Streamlit menu remains visible */
#MainMenu { visibility: visible !important; }

/* Hide the GitHub repository link */
a[href*="github.com"]:not(#MainMenu a) {
    display: none !important; /* Hide any link containing 'github.com' */
}

/* Hide the fork link */
a[aria-label="Fork"] {
    display: none !important; /* Hide any link with aria-label 'Fork' */
}

/* You can also try hiding the parent container if the above fails */
/* Replace 'header div' with specific parent element selectors */
header div[data-testid="stHeader"] {
    display: none !important; /* This would hide the entire header if needed */
}
</style>
"""

# # Inject the custom CSS into the Streamlit app
# st.markdown(hide_github_links_style, unsafe_allow_html=True)



# Inject the custom CSS
st.markdown(hide_github_links_style, unsafe_allow_html=True)
