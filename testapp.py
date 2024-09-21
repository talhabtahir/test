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

# Inject the custom CSS
st.markdown(hide_github_links_style, unsafe_allow_html=True)
