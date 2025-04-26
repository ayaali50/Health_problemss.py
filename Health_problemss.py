import streamlit as st
import datetime

# ألوان وتصميم خفيف
st.set_page_config(page_title="Genetic and Chronic Diseases", page_icon=":dna:", layout="wide")
st.markdown(
    """
    <style>
    body {
        background-color: #e6f7ff;
    }
    .main {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
    }
    </style>
    """, unsafe_allow_html=True
)

st.title("Genetic and Chronic Diseases App (تطبيق الأمراض الجينية والمزمنة)")

# اختيار المرض
disease = st.selectbox(
    "Choose a disease (اختر مرضًا):",
    [
        "Type 1 Diabetes", "Cystic Fibrosis", "Sickle Cell Anemia", "Hereditary Cancer", "Down Syndrome",
        "Aplastic Anemia", "Hereditary Blindness", "Wilson's Disease", "Multiple Sclerosis", "Lupus",
        "Rheumatoid Arthritis", "Hypertension", "Asthma", "Type 2 Diabetes", "Autism Spectrum Disorder",
        "Schizophrenia", "Breast Cancer", "Alzheimer's Disease", "ALS (Amyotrophic Lateral Sclerosis)"
    ]
)

# إدخال الأعراض للتحليل
user_symptoms = st.text_input("Enter your symptoms separated by commas (أدخل أعراضك مفصولة بفواصل):")

# وقت التذكير
reminder_time = st.time_input("Set a reminder time (حدد وقت التذكير):", value=datetime.time(9, 0))

st.markdown("---")

# قاعدة بيانات الأمراض
diseases_info = {
    "Type 1 Diabetes": {
        "definition": ("A chronic condition where the pancreas produces little or no insulin.", "حالة مزمنة حيث لا ينتج البنكرياس كمية كافية من الإنسولين."),
        "symptoms": ["Increased thirst", "Frequent urination", "Hunger", "Fatigue", "Blurred vision"],
        "causes": "Autoimmune destruction of insulin-producing beta cells.",
        "first_aid": "Monitor blood sugar. Administer insulin if prescribed.",
        "type_disorder": "Autoimmune (مناعي)",
        "gene": "Possible HLA-DR3/DR4 mutations."
    },
    "Cystic Fibrosis": {
        "definition": ("A genetic disorder that affects the lungs and digestive system.", "اضطراب جيني يؤثر على الرئتين والجهاز الهضمي."),
        "symptoms": ["Persistent cough", "Lung infections", "Poor growth", "Fatty stools"],
        "causes": "Mutation in CFTR gene.",
        "first_aid": "Clear airways. Seek emergency care for breathing difficulties.",
        "type_disorder": "Genetic (وراثي)",
        "gene": "Mutation in CFTR gene."
    },
    "Sickle Cell Anemia": {
        "definition": ("A group of inherited red blood cell disorders.", "مجموعة من اضطرابات خلايا الدم الحمراء الموروثة."),
        "symptoms": ["Anemia", "Pain episodes", "Swelling", "Frequent infections"],
        "causes": "Mutation in HBB gene.",
        "first_aid": "Hydration, pain management, urgent care for chest pain.",
        "type_disorder": "Genetic (وراثي)",
        "gene": "Mutation in HBB gene."
    },
    "Hereditary Cancer": {
        "definition": ("Cancer passed through genes, like BRCA1/2.", "سرطان موروث عبر الجينات مثل BRCA1/2."),
        "symptoms": ["Depends on cancer type", "Lumps", "Fatigue", "Bleeding"],
        "causes": "Inherited mutations in tumor suppressor genes.",
        "first_aid": "Seek urgent care for unusual symptoms.",
        "type_disorder": "Genetic (سرطاني وراثي)",
        "gene": "BRCA1, BRCA2 mutations (example)."
    },
    "Down Syndrome": {
        "definition": ("Genetic condition due to extra chromosome 21.", "حالة جينية بسبب نسخة إضافية من كروموسوم 21."),
        "symptoms": ["Intellectual disability", "Distinct facial features", "Heart defects"],
        "causes": "Trisomy 21 - Extra chromosome 21.",
        "first_aid": "Support care and medical monitoring.",
        "type_disorder": "Genetic (كروموسومي)",
        "gene": "Presence of extra chromosome 21."
    },
    "Aplastic Anemia": {
        "definition": ("Bone marrow failure to produce blood cells.", "فشل نخاع العظم في إنتاج خلايا الدم."),
        "symptoms": ["Fatigue", "Shortness of breath", "Frequent infections", "Bruising"],
        "causes": "Autoimmune or genetic causes.",
        "first_aid": "Avoid infections, urgent care for bleeding.",
        "type_disorder": "Immune/Genetic (مناعي/وراثي)",
        "gene": "Could involve genes regulating bone marrow."
    },
    "Hereditary Blindness": {
        "definition": ("Blindness caused by genetic mutations.", "العمى الناتج عن طفرات وراثية."),
        "symptoms": ["Night blindness", "Tunnel vision", "Vision loss"],
        "causes": "Mutations like RP1, RPE65.",
        "first_aid": "Use assistive tools, avoid injuries.",
        "type_disorder": "Genetic (وراثي)",
        "gene": "RP1, RPE65 mutations."
    },
    "Wilson's Disease": {
        "definition": ("Copper accumulation disorder.", "اضطراب تراكم النحاس."),
        "symptoms": ["Fatigue", "Jaundice", "Tremors", "Speech issues"],
        "causes": "Mutation in ATP7B gene.",
        "first_aid": "Low copper diet, urgent neurological care.",
        "type_disorder": "Genetic (وراثي متنحي)",
        "gene": "ATP7B gene mutation."
    },
    "Multiple Sclerosis": {
        "definition": ("Autoimmune disorder attacking CNS.", "اضطراب مناعي يهاجم الجهاز العصبي المركزي."),
        "symptoms": ["Numbness", "Tingling", "Vision problems", "Balance issues"],
        "causes": "Unknown, autoimmune.",
        "first_aid": "Immediate medical care for severe attacks.",
        "type_disorder": "Autoimmune (مناعي)",
        "gene": "Possible HLA-DRB1 mutations."
    },
    "Lupus": {
        "definition": ("Chronic autoimmune disease.", "مرض مناعي مزمن."),
        "symptoms": ["Fatigue", "Joint pain", "Skin rash"],
        "causes": "Unknown, likely genetic and environmental.",
        "first_aid": "Protect from sun, urgent care for organ symptoms.",
        "type_disorder": "Autoimmune (مناعي)",
        "gene": "Possible HLA and other immune gene mutations."
    },
    "Rheumatoid Arthritis": {
        "definition": ("Chronic autoimmune joint disease.", "مرض مناعي يؤثر على المفاصل."),
        "symptoms": ["Joint pain", "Swelling", "Morning stiffness"],
        "causes": "Autoimmune, genetics.",
        "first_aid": "Rest joints, apply cold/hot packs.",
        "type_disorder": "Autoimmune (مناعي)",
        "gene": "HLA-DR4 association."
    },
    "Hypertension": {
        "definition": ("High blood pressure condition.", "ارتفاع ضغط الدم."),
        "symptoms": ["Often none", "Headaches", "Shortness of breath"],
        "causes": "Genetic and lifestyle factors.",
        "first_aid": "Lower stress, emergency for high readings.",
        "type_disorder": "Chronic (مزمن)",
        "gene": "Genetic predisposition."
    },
    "Asthma": {
        "definition": ("Chronic inflammatory lung disease.", "مرض رئوي التهابي مزمن."),
        "symptoms": ["Wheezing", "Coughing", "Breathlessness"],
        "causes": "Genetics, allergens.",
        "first_aid": "Use inhaler, seek emergency help if severe.",
        "type_disorder": "Allergic/Chronic (تحسسي/مزمن)",
        "gene": "ADAM33, ORMDL3 gene involvement."
    },
    "Type 2 Diabetes": {
        "definition": ("Chronic condition affecting glucose metabolism.", "حالة مزمنة تؤثر على استقلاب الجلوكوز."),
        "symptoms": ["Increased thirst", "Fatigue", "Slow healing"],
        "causes": "Genetic and lifestyle.",
        "first_aid": "Control blood sugar urgently.",
        "type_disorder": "Metabolic/Chronic (استقلابي/مزمن)",
        "gene": "TCF7L2 gene involvement."
    },
    "Autism Spectrum Disorder": {
        "definition": ("Neurodevelopmental disorder.", "اضطراب في النمو العصبي."),
        "symptoms": ["Communication difficulties", "Repetitive behaviors"],
        "causes": "Genetic mutations and environmental factors.",
        "first_aid": "Supportive care for stress.",
        "type_disorder": "Neurodevelopmental (نمائي عصبي)",
        "gene": "Multiple gene involvement (e.g., SHANK3)."
    },
    "Schizophrenia": {
        "definition": ("Severe mental disorder.", "اضطراب عقلي شديد."),
        "symptoms": ["Hallucinations", "Delusions", "Disorganized thinking"],
        "causes": "Genetic and environmental factors.",
        "first_aid": "Calm environment, seek psychiatric help.",
        "type_disorder": "Psychiatric (نفسي)",
        "gene": "COMT, DISC1 gene involvement."
    },
    "Breast Cancer": {
        "definition": ("Cancer in breast cells.", "سرطان خلايا الثدي."),
        "symptoms": ["Lump", "Change in breast shape", "Nipple discharge"],
        "causes": "Genetic mutations like BRCA1/2.",
        "first_aid": "Early screening, urgent care for abnormalities.",
        "type_disorder": "Cancer (سرطاني)",
        "gene": "BRCA1, BRCA2."
    },
    "Alzheimer's Disease": {
        "definition": ("Progressive neurodegenerative disorder.", "اضطراب تنكسي عصبي تدريجي."),
        "symptoms": ["Memory loss", "Confusion", "Difficulty thinking"],
        "causes": "Genetic and age-related.",
        "first_aid": "Safe environment, emergency if lost.",
        "type_disorder": "Neurodegenerative (تنكسي عصبي)",
        "gene": "APOE-e4 gene risk."
    },
    "ALS (Amyotrophic Lateral Sclerosis)": {
        "definition": ("Motor neuron disease.", "مرض العصبون الحركي."),
        "symptoms": ["Muscle weakness", "Difficulty speaking", "Breathing problems"],
        "causes": "Genetic mutations like SOD1.",
        "first_aid": "Respiratory support, urgent neurological care.",
        "type_disorder": "Neurodegenerative (تنكسي عصبي)",
        "gene": "SOD1, C9orf72 mutations."
    }
}

# عرض بيانات المرض
if disease in diseases_info:
    info = diseases_info[disease]
    st.header(f"{disease} ({info['definition'][1]})")
    st.subheader("Definition (تعريف):")
    st.write(info['definition'][0])
    st.subheader("Symptoms (الأعراض):")
    st.write(", ".join(info['symptoms']))
    st.subheader("Causes (الأسباب):")
    st.write(info['causes'])
    st.subheader("First Aid (الإسعافات الأولية):")
    st.write(info['first_aid'])
    st.subheader("Type of Disorder (نوع الخلل):")
    st.write(info['type_disorder'])
    st.subheader("Gene Information (معلومات عن الجين):")
    st.write(info['gene'])

    st.markdown("---")

    # تحليل الأعراض
    if user_symptoms:
        symptoms_list = [s.strip().lower() for s in user_symptoms.split(",")]
        matched = any(symptom.lower() in " ".join(info['symptoms']).lower() for symptom in symptoms_list)
        if matched:
            st.success("Some of your symptoms match the disease profile. (بعض الأعراض متطابقة مع المرض المختار)")
        else:
            st.warning("Your symptoms do not strongly match this disease. (أعراضك لا تتطابق بقوة مع هذا المرض)")

# تذكير بالمواعيد
current_time = datetime.datetime.now().time()
if current_time >= reminder_time:
    st.info("This is your reminder! (هذا هو تذكيرك!)")
