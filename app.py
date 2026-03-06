import streamlit as st
import pandas as pd

# --- PAGE SETUP ---
st.set_page_config(page_title="Nyati Post Tender Dashboard", layout="wide")

# --- CUSTOM CSS (Table Styling, Fonts & Background Blur) ---
st.markdown("""
    <style>
    /* 1. BACKGROUND BLUR (Building Image) */
    .stApp {
        background-image: url("https://nyatigroup.com/wp-content/uploads/2021/08/Nyati-Unitree-Entrance-Night-1-scaled.jpg"); 
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .stApp::before {
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background-color: rgba(255, 255, 255, 0.5); 
        backdrop-filter: blur(12px); 
        z-index: -1;
    }

    /* 2. TABLE FONT & HIGHLIGHTING (Red/Blue Circle Fix) */
    /* st.table use karne par ye font 100% kaam karega */
    
    /* Table Headers (Red Circle) */
    [data-testid="stTable"] thead tr th {
        background-color: #002366 !important;
        color: white !important;
        font-size: 28px !important; /* Bada font size headings ke liye */
        font-weight: 800 !important;
        text-align: center !important;
        padding: 20px !important;
    }

    /* Table Data/Rows (Blue Circle) */
    [data-testid="stTable"] tbody td {
        font-size: 24px !important; /* Bada font size Excel data ke liye */
        font-weight: 600 !important;
        color: #000000 !important;
        padding: 15px !important;
        background-color: rgba(255, 255, 255, 0.7) !important; /* Halka white background readability ke liye */
    }

    /* 3. LANDING PAGE TITLES */
    .main-title { 
        color: #002366; 
        font-size: 80px !important; 
        font-weight: 650; 
        text-align: center;
        width: 100%;
        margin-top: 60px;
    }

    .sub-title { 
        color: #444444; 
        font-size: 60px !important; 
        font-weight: bold; 
        text-align: center;
        width: 100%;
        margin-bottom: 80px;
    }

    /* 4. BUTTONS & BOXES */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        justify-content: center !important; 
        align-items: center !important;
        gap: 60px !important; 
        width: 100% !important;
    }

    div.stButton > button {
        width: 580px !important; 
        height: 280px !important; 
        border-radius: 35px !important;
        border: 6px solid #002366 !important; 
        background-color: #f0f2f6 !important;
        color: #002366 !important;
        transition: 0.4s;
    }

    div.stButton > button p {
        font-size: 40px !important; 
        font-weight: 700 !important;
    }

    div.stButton > button:hover {
        background-color: #002366 !important;
        color: white !important;
        transform: scale(1.08);
    }
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE ---
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'landing'

# --- 1. PROJECT DATA (SAAF BLOCKS FORMAT) ---
projects = [
    {
        "Project Name": "ATS BYCULLA",
        "Type of Contractor": "Lumpsum",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Total Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_Link": "ID_ATS"
    },
    {
        "Project Name": "GERA IMPERIUM GATEWAY",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Total Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_Link": "ID_GERA_GATEWAY"
    },
    {
        "Project Name": "GERA KHARADI POJ",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Total Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_Link": "ID_GERA_KHARADI"
    },
    {
        "Project Name": "MEDICAL COLLEGE BHOJPUR",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Total Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_Link": "ID_BHOJPUR"
    },
    {
        "Project Name": "MEDICAL COLLEGE JALGAON",
        "Type of Contractor": "EPC",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Total Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_Link": "ID_JALGAON"
    },
    {
        "Project Name": "NAGPUR SYMBIOSIS-HOSTEL",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Total Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_Link": "ID_NAGPUR_SYM"
    },
    {
        "Project Name": "TATA REALTY",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Total Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_Link": "ID_TATA"
    },
    {
        "Project Name": "ADMIN BUILDING, RATNAGIRI",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Total Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_Link": "ID_ADMIN_RAT"
    },
    {
        "Project Name": "INCUBATION CENTER KALAMBOLI",
        "Type of Contractor": "Item rate",
        "Area": 69677,
        "Original BOQ Amount": 6405401141,
        "Original Budget": 6195118021,
        "Total Revised Budget": 6195118021,
        "Client Bill Amount": 0,
        "Consumed Amount": 678730011,
        "Sheet_Link": "https://docs.google.com/spreadsheets/d/1sgtzzcx32ZpiBpVJTIADtKpNfim4R-UJyRmQrFqFKIY/edit?usp=sharing"
    },
    {
        "Project Name": "KHAJAJI NAIK",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Total Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_Link": "ID_KHAJAJI"
    },
    {
        "Project Name": "MEDICAL COLLEGE MUNGER",
        "Type of Contractor": "Item rate",
        "Area": 0,
        "Original BOQ Amount": 0,
        "Original Budget": 4754076309,
        "Total Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_Link": "https://docs.google.com/spreadsheets/d/1dfN4irDAWO_RRzvo2rNB844OEMi7o-GuAEQenXc5-nY/edit?usp=sharing"
    },
    {
        "Project Name": "MEDICAL COLLEGE SATARA",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Total Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_Link": "ID_SATARA"
    },
    {
        "Project Name": "POLICE HOUSING KANDIVALI",
        "Type of Contractor": "Lumpsum",
        "Area":  71801,
        "Original BOQ Amount": 1989235222.30,
        "Original Budget": 3202892275.83,
        "Total Revised Budget": 2118577309.09,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_Link": "https://docs.google.com/spreadsheets/d/1rclVTwxgLKL45TF0JLJfCmskA9fDKXx4eb7gRpYLVxA/edit?usp=sharing"
    },
    {
        "Project Name": "RATNAGIRI AIR TERMINAL",
        "Type of Contractor": "EPC",
        "Area": 4900,
        "Original BOQ Amount": 555633790 ,
        "Original Budget": 591843869,
        "Total Revised Budget": 490145615,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_Link": "https://docs.google.com/spreadsheets/d/13TLSTX6YYcWinDHkpRKaedq9OqtJFt0Xw9IU9LSbkoY/edit?usp=sharing"
    },
    {
        "Project Name": "PLATFORM BEUTIFICATION",
        "Type of Contractor": "Item rate",
        "Area": 0,
        "Original BOQ Amount": 389863792,
        "Original Budget": 380895649,
        "Total Revised Budget": 384598873,
        "Client Bill Amount": 0,
        "Consumed Amount": 120577963,
        "Sheet_Link": "https://docs.google.com/spreadsheets/d/10ggGX0YSWQ6f-DFbdNar0sYK6cr37OY9X9qedOhDi0o/edit?usp=sharing"
    },
    {
        "Project Name": "RATNAGIRI RAILWAY STATION",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Total Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_Link": "ID_RAT_RAIL"
    },
    {
        "Project Name": "SMART CITY RATNAGIRI",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Total Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_Link": "ID_SMART_CITY"
    },
    {
        "Project Name": "BMC T&C HUB DAHISAR",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Total Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_Link": "ID_DAHISAR"
    },
    {
        "Project Name": "SYMBIOSIS CANTEEN BUILDING",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Total Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_Link": "ID_SYM_CANTEEN"
    },
    {
        "Project Name": "SYMBIOSIS WORLD SCHOOL",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Total Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_Link": "ID_SYM_SCHOOL"
    },
    {
        "Project Name": "SYMBIOSIS 944 HOSTEL",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Total Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_Link": "ID_SYM_944"
    },
    {
        "Project Name": "SYMBIOSIS 1320 HOSTEL",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Total Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_Link": "ID_SYM_1320"
    },
    {
        "Project Name": "UDAIPUR AIR TERMINAL",
        "Type of Contractor": "EPC",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Total Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_Link": "ID_UDAIPUR"
    },
    {
        "Project Name": "MEDITATION CENTRE SYMBIOSIS NAGPUR",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Total Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_Link": "ID_SYM_MED"
    },
    {
        "Project Name": "SYMBIOSIS 1320 HOSTEL LAVALE",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Total Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_Link": "ID_LAVALE_1320"
    },
    {
        "Project Name": "SYMBIOSIS SIBM EXTENSION LAVALE",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Total Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_Link": "ID_SIBM_EXT"
    },
    {
        "Project Name": "IICT CAMPUS - GOREGAON",
        "Type of Contractor": "Lumpsum",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Total Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_Link": "ID_GOREGAON"
    }
]

# Landing Page Logic

if st.session_state.current_page == 'landing':
    st.markdown('<div class="main-title">Nyati Engineering & Consultant Pvt. Ltd</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">(EPC)</div>', unsafe_allow_html=True)

    # 5 columns banaye hain: side wale khali rahenge [1.5, 3, 0.5, 3, 1.5]
    # Isse beech ke do columns (col2 aur col4) bilkul center mein aayenge
    empty1, col1, gap, col2, empty2 = st.columns([1.5, 4, 0.5, 4, 1.5])
    with col1:
        if st.button("🏗️\nProject\nSummary"):
            st.session_state.current_page = 'dashboard'
            st.rerun()

    with col2:
        if st.button("📐\nBuild Up\nArea"):
         st.session_state.current_page = 'area'
         st.rerun()

# --- PAGE 2: PROJECT SUMMARY (DASHBOARD VIEW) ---
elif st.session_state.current_page == 'dashboard':
    if st.button("⬅️ Back to Main Menu"):
        st.session_state.current_page = 'landing'
        st.rerun()

    st.title("🏗️ Post-Tender Department Management Dashboard")
    st.markdown("---")

    df_home = pd.DataFrame(projects)
    
    st.subheader("🔍 Select Project")
    selected_project = st.selectbox(
        label="", 
        options=["-- Select a Project --"] + df_home["Project Name"].tolist(),
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.subheader("Master Summary")

    # --- YAHAN FIX KIYA HAI: AB POORE 9 COLUMNS DIKHENGE ---
    # Index + 8 Data Columns = Total 9 Columns
    display_columns = [
        "Project Name", 
        "Type of Contractor", 
        "Area", 
        "Original BOQ Amount", 
        "Original Budget", 
        "Total Revised Budget", 
        "Client Bill Amount", 
        "Consumed Amount"
    ]
    
    # Data copy karke formatting apply kar rahe hain
    df_display = df_home[display_columns].copy()
    
    # Paiso waale columns ko format karne ke liye list
    money_cols = ["Original BOQ Amount", "Original Budget", "Total Revised Budget", "Client Bill Amount", "Consumed Amount"]
    
    for col in money_cols:
        df_display[col] = df_display[col].apply(lambda x: f"₹{x:,.0f}" if isinstance(x, (int, float)) else x)

    # Table display (Isme Index column automatically add ho jata hai, total 9 dikhenge)
    st.table(df_display)

    # --- TABS LOGIC (As it is) ---
    if selected_project != "-- Select a Project --":
        st.markdown("---")
        tab1, tab2 = st.tabs(["🏗️ Project Summary", "📐 Built-up Area"])

        with tab1:
            project_data = df_home[df_home["Project Name"] == selected_project].iloc[0]
            raw_url = project_data.get("Sheet_Link")
            st.subheader(f"📊 Detailed View: {selected_project}")

            if raw_url and "docs.google.com" in str(raw_url):
                try:
                    csv_url = raw_url.split("/edit")[0] + "/export?format=csv"
                    df_detail = pd.read_csv(csv_url, skiprows=5)
                    
                    # --- UPDATE 2: Detail Table Height (Scroll hat gaya) ---
                    st.dataframe(
                        df_detail, 
                        use_container_width=True, 
                        height=(len(df_detail) + 1) * 35 + 40
                    )
                except:
                    st.error("Sheet data load karne mein dikkat ho rahi hai.")
            else:
                st.info("Is project ke liye link available nahi hai.")

# --- PAGE 3: BUILT UP AREA (CLEAN VERSION) ---
elif st.session_state.current_page == 'area':
    if st.button("⬅️ Back to Main Menu"):
        st.session_state.current_page = 'landing'
        st.rerun()

    st.markdown('<div class="main-title">📐 Built-up Area Summary</div>', unsafe_allow_html=True)
    st.markdown("---")

    # Aapke Updated Google Sheet Links
    project_links = {
        "ATS BYCULLA": "https://docs.google.com/spreadsheets/d/1bN7RayW-rBo2Km6t1ImRoDZUQJvMhLjUDNI4ma6WNb4/edit?usp=sharing",
        "POLICE HOUSING": "https://docs.google.com/spreadsheets/d/14hg7Qc0xKqrhM6zn2my9FX-8Jdd-6hXmDpDQvuCFKyU/edit?usp=sharing",
        "GERA KHARADI": "https://docs.google.com/spreadsheets/d/1Da7xRWPD3EsKlUWmKnweeWGwsXqeEXdgTOXI6DnW5vM/edit?usp=sharing",
        "NAGPUR HOSTEL": "https://docs.google.com/spreadsheets/d/13mAbS-9Kq8kqMBzHp90qRn_UEgiXryeyR_72x-jiM9k/edit?usp=sharing",
        "ADMIN RATNAGIRI": "https://docs.google.com/spreadsheets/d/1XUZh68qgDmtHGh6k_ye2rs3KgaMTXADJUmRT33tgNxY/edit?usp=sharing",
        "SHIRDI COMPLEX": "https://docs.google.com/spreadsheets/d/1lC64zuM-S_wgmF9TAYGzD7Z6M5CgXhcN5RDs_0-JkMw/edit?usp=sharing",
        "CHANDRAPUR": "https://docs.google.com/spreadsheets/d/1S2t8j1g7gOVtnxZEn6S32wcOdTbCMkpJ5lU-DH1fxvg/edit?usp=sharing",
        "GERA IMPERIUM": "https://docs.google.com/spreadsheets/d/1d3UrxXAxfOlpShswUiggDWiyGUzwLS1JhkA5Xbk9NYw/edit?usp=sharing",
        "HINJEWADI": "https://docs.google.com/spreadsheets/d/1pKoLaRcDO2J8d0gKWtOK3SnCqmno_zIDpp9sijwzang/edit?usp=sharing",
        "JALGAON": "https://docs.google.com/spreadsheets/d/1klERjX1ZorvnwkulmsypdxEkFJxrD3iF6RB4kN-OGt0/edit?usp=sharing",
        "BHOJPUR": "https://docs.google.com/spreadsheets/d/1MKTFpUMxVlHAadPRkvCb5jOP1EBrMGwoxtFoJYMHPhU/edit?usp=sharing",
        "KALMBOLI": "https://docs.google.com/spreadsheets/d/16sX-cwe2H5jpUmHWd2ig1M1xKF2hHvnaIFKJZO5HQW8/edit?usp=sharing",
        "POLICE HOUSING KANDIWALI": "https://docs.google.com/spreadsheets/d/1I4oLusSWDtjMwo0i6Bf1gM9oIzDuZVxMM4Nl0AcsvDU/edit?usp=sharing",
    }

    selected_project_name = st.selectbox("📁 Select Project", list(project_links.keys()))
    sheet_url = project_links[selected_project_name]

    if sheet_url:
        try:
            # 1. URL to CSV conversion
            base_url = sheet_url.split('/edit')[0]
            csv_export_url = f"{base_url}/export?format=csv"

            # 2. Load data
            df = pd.read_csv(csv_export_url)

            # 3. Column Cleaning Logic
            # Hum saare column names ko clean (strip) kar rahe hain
            df.columns = [str(c).strip() for c in df.columns]

            # 4. Filter: Sirf aapke bataye hue 3 columns select karein
            # Hum 'fuzzy' search kar rahe hain taaki agar 'Sr.no' ya 'Sr. No.' ho toh bhi pakad le
            target_cols = []
            for col in df.columns:
                c_low = col.lower()
                if 'sr' in c_low or 'description' in c_low or 'area' in c_low:
                    target_cols.append(col)
            
            # Sirf selected columns rakhein aur khali rows (NaN) hatayein
            df_final = df[target_cols].dropna(subset=[target_cols[1]]) # Description khali nahi honi chahiye

            # 5. Display
            st.success(f"✅ {selected_project_name} Summary Loaded")
            
            # Styling: Table ko sundar dikhane ke liye
            st.dataframe(
                df_final, 
                use_container_width=True, 
                hide_index=True
            )

        except Exception as e:
            st.error(f"⚠️ Error: {e}")
            st.info("Check karein ki Sheet 'Anyone with the link' par shared hai.")
    else:
        st.warning("Is project ka link abhi add nahi kiya gaya hai.")
