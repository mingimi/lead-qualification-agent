import streamlit as st
from agent import AISalesCopilot

st.set_page_config(
    page_title="AI Sales Copilot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Sales Copilot")

st.caption(
    "Transform customer information into actionable sales intelligence."
)
st.divider()

st.subheader("📋 Customer Information")

st.write(
    """
Paste whatever information you have about the customer.

Supported formats:
- ✅ Bullet Points
- ✅ Customer Emails
- ✅ CRM Notes
- ✅ Meeting Notes
- ✅ Company Information
- ✅ LinkedIn Profile Details
TIP: The more detailed the information, the better the analysis.
"""
)

lead_information = st.text_area(
    "Customer Information",
    height=250,
    placeholder="""• Company: ABC Technologies

• Industry: SaaS

• Around 150 employees

• Looking for an AI chatbot

• Wants to automate customer support

• Requested a product demo

• Decision expected this month

• Contact Person: John Smith"""
)

if st.button("🚀 qualify lead", use_container_width=True):

    if not lead_information.strip():
        st.warning("Please enter customer information.")
        st.stop()

    with st.spinner("Analyzing lead information..."):

        agent = AISalesCopilot(
            st.secrets["GEMINI_API_KEY"]
        )

        task = agent.receive_task(lead_information)

        prompt = agent.think(task)

        result = agent.execute(prompt)

        response = agent.respond(result)

    st.success("Analysis Complete!")

    st.markdown(response)