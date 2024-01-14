import streamlit as st
import datetime

# Function to get the current date
def get_current_date():
    return datetime.date.today()

# Function to calculate days between two dates
def calculate_days_since_last_visit(last_visit_date):
    current_date = get_current_date()
    return (current_date - last_visit_date).days

def display_occasions_suggestions():
    st.subheader("Occasions Suggestions:")
    occasions_suggestions = {
        "Dashara": "2024-10-10",
        "Diwali": "2024-11-04",
        "Christmas": "2024-12-25",
        "New Year": "2025-01-01"
    }
    for occasion, date_str in occasions_suggestions.items():
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        st.button(f"{occasion} - {date.strftime('%Y-%m-%d')}")

def display_deadstock_suggestions():
    st.subheader("Deadstock Suggestions:")
    deadstock_suggestions = {
        "Kurta": 50,
        "Sherwani": 30,
        "Tuxedo": 20  # Corrected the spelling of "Tuxido" to "Tuxedo"
    }
    for item, stock in deadstock_suggestions.items():
        st.button(f"{item} - Stock: {stock}")

def display_retention_suggestions():
    st.subheader("Retention Suggestions:")
    retention_suggestions = {
        "Dewansh Assawa": "2024-01-01",  # Corrected the date format
        "Rakesh": "2024-02-15",
        "Kshitij": "2024-03-20"
    }
    for customer, last_visit_date_str in retention_suggestions.items():
        last_visit_date = datetime.datetime.strptime(last_visit_date_str, "%Y-%m-%d").date()
        days_since_last_visit = calculate_days_since_last_visit(last_visit_date)
        st.button(f"{customer} - Last Visit: {last_visit_date.strftime('%Y-%m-%d')}, Days Since Last Visit: {days_since_last_visit}")

def main():
    st.title("Smart Marketing Campaign")

    # Create clickable square cards
    occasions_card = st.empty()
    deadstock_card = st.empty()
    retention_card = st.empty()

    # Handle card clicks/hovering
    if occasions_card.button("Occasions", key="occasions"):
        display_occasions_suggestions()

    if deadstock_card.button("Deadstock", key="deadstock"):
        display_deadstock_suggestions()

    if retention_card.button("Retention", key="retention"):
        display_retention_suggestions()

if __name__ == "__main__":
    main()
