import streamlit as st
import pandas as pd
import os


def show_track_complaint():

    st.title("📍 Track Complaint")

    st.write("Enter your Complaint ID to check its status.")

    complaint_id = st.text_input(
        "Complaint ID",
        placeholder="Example: CMP-AB12CD34"
    )

    if st.button("🔍 Track Complaint"):

        file = "data/complaints.csv"

        if not os.path.exists(file):
            st.error("No complaints found.")
            return

        df = pd.read_csv(file)

        result = df[
            df["Complaint ID"].str.upper()
            == complaint_id.upper()
        ]

        if result.empty:

            st.error("❌ Complaint ID not found.")

        else:

            complaint = result.iloc[0]

            st.success("✅ Complaint Found")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Status", complaint["Status"])
                st.metric("Category", complaint["Category"])
                st.metric("Priority", complaint["Priority"])

            with col2:
                st.metric("Location", complaint["Location"])
                st.metric("Date", complaint["Date"])
                st.metric("Complaint ID", complaint["Complaint ID"])

            st.subheader("Description")

            st.info(complaint["Description"])

            if complaint["Image"] != "":

                image_path = "uploads/" + complaint["Image"]

                if os.path.exists(image_path):
                    st.image(
                        image_path,
                        caption="Uploaded Image",
                        use_container_width=True
                    )
