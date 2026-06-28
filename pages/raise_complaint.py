import streamlit as st
import pandas as pd
import os
from datetime import datetime
import uuid
from utils.ai_engine import analyze_complaint

def generate_complaint_id():
    return "CMP-" + str(uuid.uuid4())[:8].upper()


def show_raise_complaint():

    st.title("📝 Raise a Complaint")
    st.write("Fill in the details below to register a new complaint.")

    with st.form("complaint_form", clear_on_submit=True):

        name = st.text_input("👤 Full Name")

        email = st.text_input("📧 Email")

        phone = st.text_input("📱 Phone Number")

        location = st.text_input("📍 Complaint Location")

        category = st.selectbox(
            "📂 Complaint Category",
            [
                "Garbage",
                "Road Damage",
                "Water Leakage",
                "Street Light",
                "Drainage",
                "Traffic",
                "Public Toilet",
                "Electricity",
                "Other"
            ]
        )

        priority = st.selectbox(
            "⚠ Priority",
            ["Low", "Medium", "High", "Emergency"]
        )

        description = st.text_area(
            "📝 Complaint Description",
            height=150
        )

        image = st.file_uploader(
            "📷 Upload Image (Optional)",
            type=["png", "jpg", "jpeg"]
        )

        submit = st.form_submit_button("🚀 Submit Complaint")

    if submit:

        complaint_id = generate_complaint_id()
        if description:

    with st.spinner("🤖 AI is analyzing your complaint..."):

        ai_result = analyze_complaint(description)

    st.subheader("🤖 AI Analysis")

    st.code(ai_result)

        image_name = ""

        if image is not None:

            os.makedirs("uploads", exist_ok=True)

            image_name = f"{complaint_id}_{image.name}"

            with open(
                os.path.join("uploads", image_name),
                "wb"
            ) as f:
                f.write(image.getbuffer())

        complaint = {

            "Complaint ID": complaint_id,
            "Date": datetime.now().strftime("%d-%m-%Y %H:%M"),
            "Name": name,
            "Email": email,
            "Phone": phone,
            "Location": location,
            "Category": category,
            "Priority": priority,
            "Description": description,
            "Image": image_name,
            "Status": "Pending"

        }

        os.makedirs("data", exist_ok=True)

        file = "data/complaints.csv"

        if os.path.exists(file):

            df = pd.read_csv(file)

        else:

            df = pd.DataFrame()

        df = pd.concat(
            [df, pd.DataFrame([complaint])],
            ignore_index=True
        )

        df.to_csv(file, index=False)
insert_complaint(
    complaint_id=complaint_id,
    user_email=st.session_state.email,
    category=category,
    priority=priority,
    location=location,
    description=description,
    image=image_name,
    ai_summary=ai_summary,
    assigned_department=department,
)

        st.success("✅ Complaint Registered Successfully!")

        st.info(f"Complaint ID: {complaint_id}")
