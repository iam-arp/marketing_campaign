import streamlit as st
import datetime

# Function to get the current date
def get_current_date():
    return datetime.date.today()

# Function to calculate days between two dates
def calculate_days_since_last_visit(last_visit_date):
    current_date = get_current_date()
    return (current_date - last_visit_date).days

# Function to fetch dynamic data from an external source
def fetch_data(category):
    # Replace this with your actual data fetching logic
    # Here, I'm using hardcoded data for demonstration purposes
    data = {
        "Occasions": {
            "Dashara": "2024-10-10",
            "Diwali": "2024-11-04",
            "Christmas": "2024-12-25",
            "New Year": "2025-01-01"
        },
        "Deadstock": {
            "Kurta": 50,
            "Sherwani": 30,
            "Tuxido": 20
        },
        "Retention": {
            "Dewansh Assawa": "2024-01-01",
            "Rakesh": "2024-02-15",
            "Kshitij": "2024-03-20"
        }
    }

    return data.get(category, {})

# Function to display suggestions based on a category
def display_suggestions(category, data):
    st.markdown(f"<div class='suggestions slide-in' id='{category.lower()}'>{category} Suggestions:</div>", unsafe_allow_html=True)

    for key, value in data.items():
        if category.lower() == 'retention':
            last_visit_date = datetime.datetime.strptime(value, "%Y-%m-%d").date()
            days_since_last_visit = calculate_days_since_last_visit(last_visit_date)
            st.button(f"{key} - Last Visit: {last_visit_date.strftime('%Y-%m-%d')}, Days Since Last Visit: {days_since_last_visit}", key=f"{category.lower()}_{key}", style="background-color: var(--card-bg-color); color: var(--button-text-color); padding: 10px 20px; margin: 5px; font-size: 1em; border: none; border-radius: 5px; cursor: pointer; transition: background-color 0.3s;")
        else:
            st.button(f"{key} - {value}", key=f"{category.lower()}_{key}", style="background-color: var(--card-bg-color); color: var(--button-text-color); padding: 10px 20px; margin: 5px; font-size: 1em; border: none; border-radius: 5px; cursor: pointer; transition: background-color 0.3s;")

# Function to create clickable cards
def create_cards(categories):
    st.markdown("<div class='card-container'>", unsafe_allow_html=True)
    
    for category in categories:
        data = fetch_data(category)
        if st.button(category.capitalize(), key=f"{category.lower()}_button", style="background-color: var(--card-bg-color); color: var(--button-text-color); padding: 20px; text-align: center; font-size: 1.5em; border-radius: 10px; cursor: pointer; transition: background-color 0.3s;"):
            display_suggestions(category, data)

    st.markdown("</div>", unsafe_allow_html=True)

# Function to set up the main UI
def setup_ui():
    st.markdown("""
        <style>
            :root {
                --main-bg-color: #f8f9fa;
                --container-bg-color: #ffffff;
                --card-bg-color: #3498db;
                --card-hover-bg-color: #2980b9;
                --header-text-color: #3498db;
                --button-text-color: #ffffff;
            }

            body {
                font-family: 'Arial', sans-serif;
                background-color: var(--main-bg-color);
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            .container {
                max-width: 90%; /* Set a responsive max-width */
                margin: 50px auto;
                padding: 20px;
                background-color: var(--container-bg-color);
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }

            .header {
                text-align: center;
                font-size: 2em;
                color: var(--header-text-color);
                margin-bottom: 30px;
            }

            .card-container {
                display: flex;
                justify-content: space-between;
                margin-bottom: 20px;
            }

            .card {
                position: relative;
                background-color: var(--card-bg-color);
                color: var(--button-text-color);
                padding: 20px;
                text-align: center;
                font-size: 1.5em;
                border-radius: 10px;
                cursor: pointer;
                transition: background-color 0.3s;
            }

            .card:hover {
                background-color: var(--card-hover-bg-color);
            }

            .suggestions {
                text-align: center;
                font-size: 1.2em;
                margin-top: 20px;
                display: none;
            }

            .suggestion-button {
                display: none;
                background-color: var(--card-bg-color);
                color: var(--button-text-color);
                padding: 10px 20px;
                margin: 5px;
                font-size: 1em;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                transition: background-color 0.3s;
            }

            .suggestion-button:hover {
                background-color: var(--card-hover-bg-color);
            }

            .slide-in {
                animation: slideIn 0.5s forwards;
            }

            @keyframes slideIn {
                from {
                    opacity: 0;
                    transform: translateX(50px);
                }
                to {
                    opacity: 1;
                    transform: translateX(0);
                }
            }
        </style>
    """, unsafe_allow_html=True)

# Function to run the Streamlit app
def run_app():
    if __name__ == "__main__":
        setup_ui()

        # Define categories
        categories = ["Occasions", "Deadstock", "Retention"]

        # Create clickable cards based on categories
        create_cards(categories)
        st.markdown("</div>", unsafe_allow_html=True)

run_app()
