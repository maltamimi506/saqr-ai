import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="SAQR AI",
    page_icon="🦅",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #0B1424;
    color: white;
}
h1, h2, h3, p {
    direction: rtl;
    text-align: right;
}
.stButton button {
    background-color: #C5A45B;
    color: #101A2B;
    border-radius: 10px;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

st.title("🦅 SAQR AI")
st.subheader("نظام البحث والإنقاذ الذكي")
st.write("نستخدم الذكاء الاصطناعي لتحليل الصور الجوية والمساعدة في اكتشاف الأشخاص المفقودين في الصحراء.")

page = st.sidebar.radio(
    "القائمة الرئيسية",
    ["الرئيسية", "تحليل الصور", "عن المشروع"]
)

if page == "الرئيسية":
    st.header("مرحبًا بك في صقر AI")
    st.info("انتقلي إلى صفحة تحليل الصور لبدء التجربة.")

    col1, col2, col3 = st.columns(3)
    col1.metric("النظام", "AI")
    col2.metric("المجال", "الإنقاذ")
    col3.metric("المدخلات", "صور جوية")

elif page == "تحليل الصور":
    st.header("🔍 تحليل الصور الجوية")

    uploaded_file = st.file_uploader(
        "ارفعي صورة للتحليل",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, use_container_width=True)

        if st.button("بدء التحليل"):
            st.info("واجهة التحليل جاهزة. سيتم ربط نموذج YOLO لاحقًا.")

elif page == "عن المشروع":
    st.header("عن مشروع SAQR AI")
    st.write(
        "مشروع جامعي يستخدم الرؤية الحاسوبية "
        "لدعم البحث والإنقاذ في البيئات الصحراوية."
    )
    st.write("التقنيات: Python, Streamlit, YOLO")
