import streamlit as st

# 1. This sets up the look of your browser tab
st.set_page_config(page_title="Secure Portal", page_icon="🔒")

# 2. This is the app's memory. It remembers if someone successfully logged in.
# If the app just opened, we set "logged_in" to False because they haven't typed a password yet.
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# 3. This is the Login Box design. It only shows up if you aren't logged in.
def login():
    st.title("Welcome to the Client Portal")
    
    # Creates text boxes for the user to type in
    username = st.text_input("Username")
    password = st.text_input("Password", type="password") # "type=password" hides the keys as dots
    
    # What happens when they click the button:
    if st.button("Log In"):
        # It checks if the text matches these exact words:
        if username == "admin" and password == "portal2026":
            st.session_state.logged_in = True  # Changes memory to logged in!
            st.success("Login successful!")
            st.rerun()  # Refreshes the page to show the hidden portal content
        else:
            st.error("Invalid credentials") # Shows a red error box if wrong

# 4. The Gatekeeper Logic
# If the user is NOT logged in, show them the login screen we made above.
if not st.session_state.logged_in:
    login()

# If they ARE logged in, skip the login screen and show them the real web portal!
else:
    st.title("👋 Welcome Back, Admin!")
    st.write("Use the sidebar menu to navigate through your private portal tools.")
    
    # Gives them a way to leave the portal securely
    if st.button("Log Out"):
        st.session_state.logged_in = False # Clears the memory
        st.rerun() # Refreshes the page back to the login screen