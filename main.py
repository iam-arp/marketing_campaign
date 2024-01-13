import streamlit as st

def display_occasions_suggestions():
    st.subheader("Occasions Suggestions:")
    occasions_suggestions = ["Dashara", "Diwali", "Christmas", "New Year"]
    for suggestion in occasions_suggestions:
        st.button(suggestion)

def display_deadstock_suggestions():
    st.subheader("Deadstock Suggestions:")
    deadstock_suggestions = ["Kurta", "Sherwani", "Tuxido"]
    for suggestion in deadstock_suggestions:
        st.button(suggestion)

def display_retention_suggestions():
    st.subheader("Retention Suggestions:")
    retention_suggestions = ["Dewansh Assawa", "Rakesh", "Kshitij"]
    for suggestion in retention_suggestions:
        st.button(suggestion)

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
