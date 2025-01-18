import streamlit as st
from streamlit.components.v1 import html

def main():
    st.set_page_config(
        page_title="Coaching Explorer - Matthew Hansen",
        page_icon="🎯",
        layout="centered"
    )
    
    st.title("Explore Your Coaching Journey")
    st.subheader("Discover Your Path to Professional Growth")
    
    # Introduction
    st.markdown("""
    Ready to explore your professional development needs? Our AI coaching assistant can help you:
    - Identify key areas for growth
    - Discover quick improvements
    - Understand how coaching can support your journey
    """)
    
    # Areas of Focus
    tabs = st.tabs(["Self-Assessment", "Quick Wins", "Growth Areas"])
    
    with tabs[0]:
        st.markdown("""
        #### Self-Assessment 🔍
        
        Common areas to explore:
        * Leadership capabilities
        * Communication patterns
        * Career satisfaction
        * Team dynamics
        * Work-life balance
        
        Our AI assistant can help you identify which areas might benefit most from coaching support.
        """)
    
    with tabs[1]:
        st.markdown("""
        #### Quick Wins 🌟
        
        Immediate steps for improvement:
        * Simple reflection exercises
        * Communication techniques
        * Priority setting methods
        * Stress management practices
        
        Get started with some actionable insights while exploring deeper coaching opportunities.
        """)
    
    with tabs[2]:
        st.markdown("""
        #### Growth Areas 📈
        
        Long-term development through coaching:
        * Strategic leadership skills
        * Career advancement
        * Team effectiveness
        * Personal branding
        * Professional relationships
        
        Discover how coaching can support your long-term professional growth.
        """)
    
    # Feazy chat component
    st.markdown("### Start Your Exploration")
    feazy_html = """
    <div style="height: 600px;">
    <script type="module" src="https://unpkg.com/feazy-plugin/dist/feazy-chat-component.es.js"></script>
    <chat-component 
        theme="neutral-theme"
        promptId="4a443b92-e52a-44db-a507-17457ec3de14"
        chatTitle="Coaching Explorer"
        showDataProtection="true"
        isDialogVisible="true"
        baseUrl="https://api.feazy.ai">
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
    </div>
    """
    
    # Render the Feazy chat component
    html(feazy_html, height=600)
    
    # Benefits of Coaching
    with st.expander("🌟 Benefits of Professional Coaching"):
        st.markdown("""
        ### Transform Your Professional Life
        
        #### Leadership Excellence
        Develop advanced leadership skills and strategic thinking capabilities.
        
        #### Career Growth
        Navigate transitions and accelerate your professional development.
        
        #### Team Success
        Build and lead high-performing teams with improved communication.
        
        Ready to take the next step? Chat with our AI assistant above to explore how coaching can support your goals.
        """)
    
    # Footer with call-to-action
    st.markdown("---")
    st.markdown("""
        💡 **Start Your Growth Journey Today**  
        Explore your development needs with our AI assistant and discover how professional coaching can accelerate your success.
    """)

    # Add prompt template at the bottom
    st.markdown("---")
    with st.expander("🤖 Coaching Explorer Prompt Configuration"):
        st.markdown("""
        # Feazy Prompt Template: Com-unique-ation Coach Bot

        ## General Information
        **Name:** Com-unique-ation Coach Bot
        
        **Description:** AI coaching assistant designed to help professionals explore their development needs, gain initial insights, and understand how Matthew Hansen's coaching services can support their growth journey.
        
        ## Instructions
        
        ### Description
        Initial touchpoint for potential coaching clients, helping them articulate challenges, identify areas for growth, and discover quick wins while showcasing how Matthew's coaching can provide deeper, lasting transformation.
        
        ### Languages
        - Primary: English
        - Secondary: German
        
        ### Audience
        - Professionals seeking personal development
        - Leaders facing workplace challenges
        - Individuals in career transition
        - Teams seeking better dynamics
        - Anyone interested in professional growth
        
        ### Objectives
        1. Help users articulate current challenges
        2. Provide initial insights and quick wins
        3. Demonstrate the value of professional coaching
        4. Guide users toward Matthew's services when appropriate
        5. Create a safe space for exploration while maintaining clear boundaries
        
        ### Tasks
        1. Initial Assessment
           - Ask targeted questions to understand challenges
           - Help identify underlying patterns
           - Guide self-reflection
           - Spot immediate improvement opportunities
        
        2. Quick Wins
           - Suggest simple, actionable steps
           - Share basic frameworks for immediate use
           - Provide reflection exercises
           - Recommend initial self-development practices
        
        3. Service Matching & Conversion
           - Connect challenges to Matthew's services
           - Explain coaching benefits
           - Share success stories
           - Guide toward next steps
        
        ### Opening Message
        "Welcome! I'm the Com-unique-ation Coach Bot. I can help you explore your professional challenges, discover some quick improvements, and understand how Matthew Hansen's coaching could support your growth journey. What brings you here today?"
        
        ### Personality & Style
        - Empathetic and understanding
        - Professional yet approachable
        - Solution-focused
        - Curious and explorative
        - Clear about boundaries
        
        ### Guardrails
        1. Maintain Clear Boundaries
           - Don't provide deep coaching
           - Focus on exploration and initial insights
           - Avoid specific advice on complex issues
        
        2. Stay Within Scope
           - Offer only basic frameworks and exercises
           - Keep suggestions general and low-risk
           - Direct complex issues to professional coaching
        
        3. Ethical Guidelines
           - Be transparent about being an AI
           - Don't handle crisis situations
           - Maintain confidentiality
        """)

if __name__ == "__main__":
    main()