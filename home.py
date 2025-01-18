import streamlit as st
from streamlit.components.v1 import html

def main():
    st.set_page_config(
        page_title="Matthew Hansen Coaching Assistant",
        page_icon="🎯",
        layout="centered"
    )
    
    # Header
    st.title("Welcome to com-unique-ation")
    st.subheader("Your AI Assistant for Matthew Hansen's Coaching Services")
    
    # Introduction
    st.markdown("""
    Welcome to Matthew Hansen's coaching assistant. This AI-powered tool is designed to help you
    learn more about Matthew's coaching services and find the right solution for your needs.
    Feel free to ask questions about his services, approach, or how he can help you achieve your goals.
    """)
    
    # Two-column layout for key information
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Core Roles")
        st.markdown("""
        * 🎯 **Coach**
          - Creates safe spaces for exploration
          - Leads to new clarity
          - Enables natural progression
          
        * 🤝 **Sparring Partner**
          - Collaborates on business challenges
          - Provides fresh perspectives
          - Offers creative input
          
        * ✨ **Talent Wizard**
          - Identifies key strengths
          - Aligns talents with tasks
          - Fosters effective utilization
        """)
    
    with col2:
        st.markdown("### Service Lines")
        st.markdown("""
        * 🌟 **Identity, Mission, and Community**
          - Personal alignment
          - Professional insight
          - Purpose discovery
          
        * 📈 **Self-Leadership Improvement**
          - Enhanced work relationships
          - Improved performance
          - Better decision-making
          
        * 🔄 **Career Transition Support**
          - Professional narrative
          - Target definition
          - Self-marketing strategies
        """)
    
    # Feazy chat component
    st.markdown("### Chat with the Assistant")
    feazy_html = """
    <script type="module" src="https://unpkg.com/feazy-plugin/dist/feazy-chat-component.es.js"></script>
    <chat-component 
        theme="neutral-theme"
        promptId="28c99f7b-ce8a-4693-8c03-e887962eb1ad"
        chatTitle="Matthew Hansen Coaching Assistant"
        showDataProtection="true"
        baseUrl="">
    </chat-component>
    
    <style>
        chat-component {
            --primary-color: #2C3E50;
            --secondary-color: #f8f9fa;
            --text-color: #333333;
            --border-color: #dee2e6;
            --bot-message-bg: #f1f3f5;
            --user-message-bg: #e9ecef;
            --header-bg: #2C3E50;
            --header-text: #ffffff;
            --chat-button-bg: #2C3E50;
            --chat-button-color: #ffffff;
            --send-button-bg: #2C3E50;
            --send-button-color: #ffffff;
        }
    </style>
    """
    
    # Render the Feazy chat component
    html(feazy_html, height=600)
    
    # Additional information in expandable sections
    with st.expander("📚 About Matthew's Approach"):
        st.markdown("""
        Matthew Hansen's coaching philosophy centers on creating a supportive environment where clients can:
        - Explore their professional goals with clarity
        - Develop effective leadership strategies
        - Align personal strengths with career objectives
        - Navigate transitions with confidence
        
        His holistic approach helps translate personal insights into actionable professional strategies.
        """)
    
    with st.expander("🌐 Languages"):
        st.markdown("""
        Services are available in:
        - English
        - German
        
        The AI assistant can help you in both languages - feel free to chat in your preferred language.
        """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
        💼 **Ready to take the next step?**  
        Visit [com-unique-ation.com](https://www.com-unique-ation.com/) to learn more or schedule a session.
    """)

if __name__ == "__main__":
    main()