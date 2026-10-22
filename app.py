import streamlit as st
from PIL import Image
from model import waste_analyzer

st.set_page_config(
    page_title="Smart Waste Segregation Assistant",
    page_icon="♻️",
    layout="wide"
)
if "result" not in st.session_state:
    st.title("Smart Waste Segregation Assistant♻️")
    st.subheader("AI Smart Waste Analyzer♻️")
    st.write(
        "Upload an image and Smart Waste Segregation Assistant "
        "will identify the item and provide useful waste information."
    )
    st.write("")

    # Upload Section 
    left, center, right = st.columns([1, 2, 1])
    with center:
        upload_file = st.file_uploader(
            "Upload the Image of the waste you want to classify",
            type=["jpg", "jpeg", "png"]
        )

        if upload_file is not None:
            image = Image.open(upload_file)

        # Small preview
            st.image(
                image,
                caption="Uploaded Waste",
                width=220
            )
            if st.button("♻️Analyze Waste"):
                with st.spinner("AI is analyzing..."):
                    try:
                        image_bytes = upload_file.getvalue()
                        result = waste_analyzer(image_bytes)
                        st.session_state["result"] = result
                        st.session_state["image"] = image_bytes
                        st.rerun()

                    except Exception as e:
                        st.error(
                            f"Error analyzing the image: {e}"
                        )

    # Work Flow 
    st.divider()
    left, center, right = st.columns([1, 2, 1])
    with center:
        st.subheader("Work Flow")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.write("📷 **Upload**")
            st.write("Upload an image of the waste item you want to classify. Ensure the image is clear and well-lit for accurate analysis.")
        with col2:
            st.write("🤖 **Analyze**")
            st.write("Click the 'Analyze Waste' button to let the AI model identify the waste item and provide classification and disposal guidance.")
        with col3:
            st.write("🌱 **Learn**")
            st.write("View the analysis results, including the identified item, material, waste category, and recycling guidance.")

else:
# result page
    st.title("♻️ Waste Analysis")

    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(
            st.session_state["image"],
            caption="Uploaded Waste",
            width=220
        )
        
        st.info("Try to reuse or recycle the waste item if possible. Follow local guidelines for proper disposal.")
    with col2:
        st.subheader("Analysis Result")
        st.write(
            st.session_state["result"]
        )
    st.divider()
    st.subheader("🌱 Think Before You Throw")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("🔄Reuse")
    with col2:
        st.write("♻️Recycle")
    with col3:
        st.write("🌍Protect the Environment")

    st.divider()
    if st.button("← Analyze Another Waste"):
        del st.session_state["result"]
        del st.session_state["image"]
        st.rerun()

st.divider()
st.caption(
    "This application is designed to assist users in properly "
    "segregating waste. Local waste-management rules may differ."
)