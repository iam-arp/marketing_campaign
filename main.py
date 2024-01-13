import streamlit as st
import datetime

# Function to get the current date
def get_current_date():
    return datetime.date.today()

# Function to calculate days between two dates
def calculate_days_since_last_visit(last_visit_date):
    current_date = get_current_date()
    return (current_date - last_visit_date).days

# Custom CSS style for the app
custom_css = """
<style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f8f9fa;
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    .container {
        max-width: 800px;
        margin: 50px auto;
        padding: 20px;
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }

    .header {
        text-align: center;
        font-size: 2em;
        color: #3498db;
        margin-bottom: 30px;
    }

    .card {
        background-color: #3498db;
        color: #ffffff;
        padding: 20px;
        text-align: center;
        font-size: 1.5em;
        border-radius: 10px;
        margin-bottom: 20px;
        cursor: pointer;
        transition: background-color 0.3s;
    }

    .card:hover {
        background-color: #2980b9;
    }

    .suggestions {
        text-align: center;
        font-size: 1.2em;
        margin-top: 20px;
    }

    .suggestion-button {
        background-color: #3498db;
        color: #ffffff;
        padding: 10px 20px;
        margin: 5px;
        font-size: 1em;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s;
    }

    .suggestion-button:hover {
        background-color: #2980b9;
    }
</style>
"""

# Apply custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

def display_occasions_suggestions():
    st.markdown("<div class='suggestions'>Occasions Suggestions:</div>", unsafe_allow_html=True)
    occasions_suggestions = {
        "Dashara": "2024-10-10",
        "Diwali": "2024-11-04",
        "Christmas": "2024-12-25",
        "New Year": "2025-01-01"
    }
    for occasion, date_str in occasions_suggestions.items():
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        st.button(f"{occasion} - {date.strftime('%Y-%m-%d')}", class="suggestion-button")

def display_deadstock_suggestions():
    st.markdown("<div class='suggestions'>Deadstock Suggestions:</div>", unsafe_allow_html=True)
    deadstock_suggestions = {
        "Kurta": 50,
        "Sherwani": 30,
        "Tuxido": 20
    }
    for item, stock in deadstock_suggestions.items():
        st.button(f"{item} - Stock: {stock}", class="suggestion-button")

def display_retention_suggestions():
    st.markdown("<div class='suggestions'>Retention Suggestions:</div>", unsafe_allow_html=True)
    retention_suggestions = {
        "Dewansh Assawa": "2024-01-01",
        "Rakesh": "2024-02-15",
        "Kshitij": "2024-03-20"
    }
    for customer, last_visit_date_str in retention_suggestions.items():
        last_visit_date = datetime.datetime.strptime(last_visit_date_str, "%Y-%m-%d").date()
        days_since_last_visit = calculate_days_since_last_visit(last_visit_date)
        st.button(f"{customer} - Last Visit: {last_visit_date.strftime('%Y-%m-%d')}, Days Since Last Visit: {days_since_last_visit}", class="suggestion-button")

def main():
    st.markdown("<div class='container'>", unsafe_allow_html=True)
    st.markdown("<div class='header'>Smart Marketing Campaign</div>", unsafe_allow_html=True)

    # Create clickable square cards
    if st.button("Occasions", class="card"):
        display_occasions_suggestions()

    if st.button("Deadstock", class="card"):
        display_deadstock_suggestions()

    if st.button("Retention", class="card"):
        display_retention_suggestions()

    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
