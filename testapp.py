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

# Custom CSS and JavaScript to hide specific elements
hide_specific_elements_script = """
<style>
/* Keep the Streamlit main menu visible */
#MainMenu {visibility: visible;}
</style>

<script>
// Wait for the page to fully load before hiding the elements
document.addEventListener('DOMContentLoaded', function() {
    // Hide GitHub repo link based on its unique identifier or class
    var githubLinks = document.querySelectorAll('a[href*="github.com"]');
    githubLinks.forEach(function(link) {
        if (link.href.includes('github.com')) {
            link.style.display = 'none';
        }
    });

    // Hide the fork link (if it has a specific class or identifier)
    var forkLinks = document.querySelectorAll('[aria-label="Fork"]'); // Replace with actual selector if different
    forkLinks.forEach(function(link) {
        link.style.display = 'none';
    });
});
</script>
"""

# Inject the custom CSS and JavaScript into the Streamlit app
st.markdown(hide_specific_elements_script, unsafe_allow_html=True)


# Inject the custom CSS
st.markdown(hide_github_links_style, unsafe_allow_html=True)
