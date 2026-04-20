import streamlit as st

def main():
    st.set_page_config(page_title="IPL Predictor", page_icon="🏏", layout="centered")

    st.title("🏏 IPL Prediction System")
    st.subheader("Machine Learning Powered Cricket Analytics")

    st.markdown("""
    ### 👋 Welcome!

    This application provides:
    
    - 📊 **First Innings Score Prediction**
    - 🏆 **Match Winner Prediction**
    
    Built using Machine Learning models trained on historical IPL data.

    ---
    """)

    st.info("👉 Use the sidebar to navigate between features")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Go to Score Predictor"):
            st.switch_page("app.py")

    with col2:
        if st.button("Go to Match Predictor"):
            st.switch_page("app1.py")

    st.markdown("---")
    st.caption("Developed for academic and project demonstration purposes.")

if __name__ == "__main__":
    main()