import streamlit as st
from PIL import Image

st.set_page_config(page_title='MIRQAP AI | مرقاب', page_icon='🇸🇦', layout='wide', initial_sidebar_state='expanded')

st.markdown('''<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800&display=swap');
html, body, [class*="css"], .stApp {font-family:'Tajawal',sans-serif;}
.stApp {background:radial-gradient(circle at 85% 0%,#12382f 0%,#071b1b 40%,#071216 85%);color:#f3f6f1;}
[data-testid="stSidebar"] {background:#081b1d;border-right:1px solid #255147;}
[data-testid="stSidebar"] * {font-family:'Tajawal',sans-serif;}
.block-container {max-width:1260px;padding-top:2rem;}
h1,h2,h3,p {direction:rtl;text-align:right;}
h1,h2,h3 {color:#f5f7f3!important;}
.mq-hero {padding:48px 44px;border:1px solid #2b6456;border-radius:26px;background:linear-gradient(115deg,rgba(12,55,49,.96),rgba(10,29,35,.95));position:relative;overflow:hidden;}
.mq-eyebrow {color:#d8b875;letter-spacing:3px;font-size:13px;font-weight:800;text-align:right;direction:rtl;}
.mq-title {font-size:clamp(40px,6vw,78px);font-weight:800;letter-spacing:1px;line-height:1.12;color:#f6f5ed;text-align:right;direction:rtl;margin:15px 0;}
.mq-title span {color:#d9bb7d;}
.mq-sub {color:#c5d8d2;font-size:20px;max-width:650px;line-height:1.9;text-align:right;direction:rtl;margin-left:auto;}
.mq-pill {display:inline-block;border:1px solid #4b8675;color:#d1e8df;background:#123e35;border-radius:999px;padding:8px 16px;font-size:13px;}
.mq-card {background:linear-gradient(155deg,#112c2e,#0d2026);border:1px solid #27504c;border-radius:20px;padding:24px;min-height:152px;direction:rtl;text-align:right;}
.mq-card .ey {font-size:14px;color:#9dbbb2;}
.mq-card .big {font-size:29px;font-weight:800;color:#f4f4ed;margin-top:16px;}
.mq-card .sm {font-size:13px;color:#d1b679;margin-top:6px;}
.mq-section {font-size:30px;font-weight:800;margin:30px 0 10px;direction:rtl;text-align:right;}
.mq-note {background:#102a2b;border-right:3px solid #c9ab6b;padding:18px 22px;border-radius:12px;color:#cbdcd6;direction:rtl;text-align:right;line-height:1.8;}
div.stButton>button {background:linear-gradient(90deg,#c5a365,#e1c78e);color:#12211e;border:0;border-radius:12px;font-weight:800;padding:12px 22px;}
[data-testid="stFileUploader"] {border:1px dashed #4d8577;border-radius:18px;padding:14px;background:#0e2829;}
[data-testid="stMetric"] {background:#102c2d;border:1px solid #28524c;border-radius:15px;padding:16px;}
@media(max-width:700px){.mq-hero{padding:28px 22px}.mq-title{font-size:42px}}
</style>''', unsafe_allow_html=True)

with st.sidebar:
    st.markdown('## 🇸🇦 مرقاب | MIRQAP')
    st.caption('INTELLIGENT SEARCH & RESCUE')
    st.divider()
    page = st.radio('القائمة الرئيسية', ['الرئيسية', 'تحليل الصور', 'لوحة المعلومات', 'عن مرقاب'])
    st.divider()
    st.caption('● نسخة أولية تعليمية')
    st.caption('صُممت لخدمة تحديات البحث في البيئات الصحراوية')

if page == 'الرئيسية':
    st.markdown('''<div class="mq-hero"><div class="mq-eyebrow">SAUDI-BORN INTELLIGENCE · ذكاء من أرض المملكة</div><div class="mq-title">نرى ما قد<br><span>يغيب عن الأنظار</span></div><div class="mq-sub">مرقاب منصة سعودية تجريبية لدعم البحث والإنقاذ، تستخدم الرؤية الحاسوبية لتحليل الصور الجوية والمساعدة في تحديد مواقع الأشخاص في البيئات الصحراوية.</div><div style="text-align:right;margin-top:24px"><span class="mq-pill">MIRQAP AI · منصة الرصد الذكي</span></div></div>''', unsafe_allow_html=True)
    st.markdown('<div class="mq-section">من الرصد إلى القرار</div>', unsafe_allow_html=True)
    a,b,c=st.columns(3)
    with a: st.markdown('<div class="mq-card"><div class="ey">01 / الإدخال</div><div class="big">صورة جوية</div><div class="sm">رفع ومعاينة الصورة</div></div>', unsafe_allow_html=True)
    with b: st.markdown('<div class="mq-card"><div class="ey">02 / المعالجة</div><div class="big">رؤية حاسوبية</div><div class="sm">الربط بنموذج YOLO قيد التطوير</div></div>', unsafe_allow_html=True)
    with c: st.markdown('<div class="mq-card"><div class="ey">03 / المخرجات</div><div class="big">مؤشرات مرئية</div><div class="sm">مربعات الكشف والثقة بعد الربط</div></div>', unsafe_allow_html=True)
    st.write('')
    st.markdown('<div class="mq-note">🇸🇦 <b>لماذا مرقاب؟</b> لأن اتساع المساحات الصحراوية يجعل تحليل الصور الجوية تحديًا مهمًا. نطوّر نموذجًا أوليًا لاستكشاف كيف يمكن للذكاء الاصطناعي أن يساعد فرق البحث في مراجعة الصور بسرعة ووضوح.</div>', unsafe_allow_html=True)
    if st.button('ابدئي تحليل صورة ←', use_container_width=True):
        st.info('اختاري «تحليل الصور» من القائمة الجانبية للبدء.')

elif page == 'تحليل الصور':
    st.markdown('<div class="mq-eyebrow">MIRQAP / IMAGE INTELLIGENCE</div><div class="mq-section">مركز تحليل الصور الجوية</div>', unsafe_allow_html=True)
    st.markdown('<div class="mq-note">ارفعي صورة JPG أو PNG. حاليًا تعمل المعاينة فقط؛ سيتم تفعيل الكشف الفعلي عند دمج نموذج YOLO من فريق المشروع.</div>', unsafe_allow_html=True)
    st.write('')
    uploaded=st.file_uploader('اختاري صورة للتحليل',type=['jpg','jpeg','png'])
    if uploaded is not None:
        try:
            image=Image.open(uploaded).convert('RGB')
            st.image(image,caption='معاينة الصورة المرفوعة',use_container_width=True)
            a,b=st.columns(2)
            a.metric('حالة الإدخال','جاهز')
            b.metric('نموذج الكشف','بانتظار الربط')
            if st.button('بدء التحليل',use_container_width=True):
                from sahi import AutoDetectionModel
                model = AutoDetectionModel.from_pretrained(model_type="yolov8", model_path="yolo11n.pt", confidence_threshold=0.25, device="cpu")
                from sahi.predict import get_sliced_prediction
                results = get_sliced_prediction(image, model, slice_height=320, slice_width=320, overlap_height_ratio=0.25, overlap_width_ratio=0.25)
                results.object_prediction_list = [p for p in results.object_prediction_list if p.category.name == "person"]
                st.success(f"عدد الأشخاص المكتشفين: {len(results.object_prediction_list)}")
                results.export_visuals(export_dir="runs/sahi")
                st.image("runs/sahi/prediction_visual.png", caption="نتيجة كشف الأشخاص")
        except Exception as e:
            st.error(str(e))
    else:
        st.info('لم تُرفع أي صورة بعد.')

elif page == 'لوحة المعلومات':
    st.markdown('<div class="mq-eyebrow">MIRQAP / INSIGHTS</div><div class="mq-section">لوحة المعلومات</div>', unsafe_allow_html=True)
    st.markdown('<div class="mq-note">هذه اللوحة جاهزة لعرض نتائج الاختبارات بعد جمع البيانات من الفريق. لا توجد أرقام أداء مؤكدة حتى الآن.</div>',unsafe_allow_html=True)
    a,b,c=st.columns(3)
    a.metric('الصور المختبرة','—')
    b.metric('Precision','—')
    c.metric('Recall','—')
    st.markdown('### ما الذي سنقيسه؟')
    st.write('عدد الصور، حالات الكشف الصحيحة، الإنذارات الخاطئة، الحالات الفائتة، والدقة والاسترجاع بعد الاختبار.')

else:
    st.markdown('<div class="mq-eyebrow">ABOUT / MIRQAP AI</div><div class="mq-section">مرقاب | ذكاء يراقب الأفق</div>',unsafe_allow_html=True)
    st.write('مرقاب مشروع طلابي سعودي يختبر استخدام الذكاء الاصطناعي والرؤية الحاسوبية لدعم البحث عن الأشخاص في البيئات الصحراوية باستخدام الصور الجوية.')
    st.markdown('### التقنيات')
    st.write('Python · Streamlit · YOLO · Computer Vision · Data Analytics')
    st.markdown('<div class="mq-note">تنويه: مرقاب نموذج أولي تعليمي، وليس أداة معتمدة للاستخدام في عمليات الإنقاذ الفعلية. يتطلب الاستخدام الميداني بيانات مناسبة واختبارات وتحققًا صارمًا.</div>',unsafe_allow_html=True)

st.divider()
st.caption('MIRQAP AI © 2026  |  Saudi Student Innovation  |  Educational Prototype')
