import streamlit as st
import pandas as pd

# --- PAGE SETUP ---
st.set_page_config(page_title="Nyati Post-Tender Department Dashboard", layout="wide")

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

    /* 4. BUTTONS & BOXES - FIXED CENTER */
    [data-testid="stHorizontalBlock"] {
    display: flex !important;
    justify-content: center !important; 
    align-items: center !important;
    gap: 15px !important; /* Gap aur kam kar diya */
    width: 80% !important; /* Container ki width limit ki taaki center ho sake */
    margin: 0 auto !important; /* Ye sabse zaroori hai center karne ke liye */
}

    div.stButton > button {
    width: 200px !important; 
    height: 60px !important; 
    border-radius: 20px !important;
    border: 3px solid #002366 !important; 
    background-color: #f0f2f6 !important;
    color: #002366 !important;
    transition: 0.4s;
}

    div.stButton > button p {
        font-size: 20px !important; /* Font size 40px se 28px kiya */
        font-weight: 400 !important;
        line-height: 1.2 !important;
    }

    div.stButton > button:hover {
        background-color: #002366 !important;
        color: white !important;
        transform: scale(1.05);
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
    # Isko Paste Karo:
    st.markdown("""
        <div style="
            font-size: 36px; 
            font-weight: bold; 
            color: #002366; 
            text-align: center; 
            width: 100%; 
            white-space: nowrap; 
            overflow: hidden; 
            text-overflow: ellipsis;
            margin-top: 40px;
        ">
            Nyati Engineers & Consultants Pvt. Ltd.
        </div>
        <div style="
            font-size: 28px; 
            color: #444444; 
            text-align: center; 
            width: 100%; 
            margin-bottom: 40px;
        ">
            (EPC)
        </div>
    """, unsafe_allow_html=True)

    # 5 columns banaye hain: side wale khali rahenge [1.5, 3, 0.5, 3, 1.5]
    # Isse beech ke do columns (col2 aur col4) bilkul center mein aayenge
    # Gap kam karne ke liye ratio [1.5, 3.5, 0.1, 3.5, 1.5] kiya hai
    # Side columns ko bada kiya (3.5 se 3.5) taaki beech ka content center rahe
    empty1, col1, mid_gap, col2, empty2 = st.columns([3.5, 3, 0.1, 3, 3.5])
    
    with col1:
        if st.button("🏗️ Project Summary"):
            st.session_state.current_page = 'dashboard'
            st.rerun()

    with col2:
        if st.button("📐 Build Up Area"):
            st.session_state.current_page = 'area'
            st.rerun()

# --- PAGE 2: PROJECT SUMMARY (DASHBOARD VIEW) ---
elif st.session_state.current_page == 'dashboard':
    
    # Session State handle karne ke liye (Detail View logic)
    if 'view_mode' not in st.session_state:
        st.session_state.view_mode = 'table'
    if 'selected_project' not in st.session_state:
        st.session_state.selected_project = None

    # --- CASE A: AGAR DETAIL VIEW MEIN HAIN (EXCEL SHEET VIEW) ---
    if st.session_state.view_mode == 'detail' and st.session_state.selected_project:
        if st.button("⬅️ Back"):
            st.session_state.view_mode = 'table'
            st.session_state.selected_project = None
            st.rerun()

        st.title(f"📊 Detailed View: {st.session_state.selected_project}")
        st.markdown("---")

        # Aapka Original Excel Loading Logic
        df_home = pd.DataFrame(projects)
        project_data = df_home[df_home["Project Name"] == st.session_state.selected_project].iloc[0]
        raw_url = project_data.get("Sheet_Link")
        
        if raw_url and "docs.google.com" in str(raw_url):
            try:
                csv_url = raw_url.split("/edit")[0] + "/export?format=csv"
                df_raw = pd.read_csv(csv_url, header=None).head(20)
                h_idx = 0
                for i, row in df_raw.iterrows():
                    row_str = " ".join(row.astype(str)).lower()
                    if any(kw in row_str for kw in ["particular", "item description", "sr.no"]):
                        h_idx = i
                        break
                
                df_detail = pd.read_csv(csv_url, skiprows=h_idx)
                df_detail.columns = [str(c).replace('\n', ' ').strip() for c in df_detail.columns]

                mapping = {
                    "Item Description": ["particular", "item description", "items"],
                    "Original BOQ Amount": ["original boq amount", "boq amount", "tender boq"],
                    "Original Budget": ["original budget", "tender zero", "budget (with gst)"],
                    "Revised Budget": ["revised budget", "revised target"],
                    "Client Bill Amount": ["client bill amount", "client billing", "total billing"],
                    "Consumed Amount": ["consumed amount", "actual cost", "consumed budget"]
                }

                final_cols = []
                for label, keywords in mapping.items():
                    for col in df_detail.columns:
                        if any(k in col.lower() for k in keywords):
                            final_cols.append(col)
                            break
                
                if final_cols:
                    df_final_view = df_detail[final_cols].dropna(subset=[final_cols[0]]).copy()
                    
                    def style_dash(row):
                        val = str(row.iloc[0]).lower()
                        if 'total' in val:
                            return ['background-color: #90EE90; font-weight: bold; color: black'] * len(row)
                        return [''] * len(row)

                    st.dataframe(df_final_view.style.apply(style_dash, axis=1), use_container_width=True, hide_index=True)
                else:
                    st.warning("Matching columns (Budget/BOQ) nahi mile.")
            except Exception as e:
                st.error(f"Dashboard Error: {e}")

    # --- CASE B: AGAR MASTER SUMMARY MEIN HAIN (TABLE VIEW) ---
    else:
        if st.button("⬅️ Back"):
            st.session_state.current_page = 'landing'
            st.rerun()

        st.markdown('<h1 style="font-size: 28px; font-weight: bold; color: #002060; margin-bottom: 0px;">🏗️ Post-Tender Department Management Dashboard</h1>', unsafe_allow_html=True)
        st.markdown('<hr style="border: 1px solid #002060; margin-top: 5px; margin-bottom: 20px;">', unsafe_allow_html=True)

        df_home = pd.DataFrame(projects)
        
        # Master Summary Table
        st.markdown("### Master Summary")
        display_columns = ["Project Name", "Type of Contractor", "Area", "Original BOQ Amount", "Original Budget", "Total Revised Budget", "Client Bill Amount", "Consumed Amount"]
        df_display = df_home[display_columns].copy()
        
        money_cols = ["Original BOQ Amount", "Original Budget", "Total Revised Budget", "Client Bill Amount", "Consumed Amount"]
        for col in money_cols:
            df_display[col] = df_display[col].apply(lambda x: f"₹{x:,.0f}" if isinstance(x, (int, float)) else x)
        
        # --- NAYA STYLING LOGIC ADDED ---
        styled_df = df_display.style.set_table_styles([
            {
                'selector': 'th',
                'props': [
                    ('background-color', '#1f4e78'),
                    ('color', 'white'),
                    ('font-size', '18px'),
                    ('text-align', 'center'),
                    ('font-weight', 'bold')
                ]
            },
            {
                'selector': 'td',
                'props': [
                    ('font-size', '16px'),
                    ('padding', '10px')
                ]
            }
        ])

        # --- UPDATE: Height fix (Extra cells hatane ke liye) ---
        # 35.2 per row height hoti hai, humne +38 header ke liye rakha hai
        dynamic_height = (len(df_display) * 35.2) + 38

        event = st.dataframe(
            styled_df, 
            use_container_width=True, 
            hide_index=True,
            on_select="rerun",
            selection_mode="single-row", # Fixed: underscore ki jagah dash (-) lagaya
            height=int(dynamic_height)   # Integer mein convert kiya for safety
        )

        # Row Selection Logic
        if len(event.selection.rows) > 0:
            selected_row_index = event.selection.rows[0]
            project_to_open = df_display.iloc[selected_row_index]["Project Name"]
            
            st.session_state.selected_project = project_to_open
            st.session_state.view_mode = 'detail'
            st.rerun()

# --- PAGE 3: BUILT UP AREA ---
elif st.session_state.current_page == 'area':
    
    # Session State handle karne ke liye (Detail View logic)
    if 'area_view_mode' not in st.session_state:
        st.session_state.area_view_mode = 'table'
    if 'selected_project' not in st.session_state:
        st.session_state.selected_project = None

    # 1. SARE PROJECTS KE BLOCKS (Aapka Original Block)
    projects_list = [
        {
        "Sr.no": 1, "Project Name": "ADMIN BUILDING, RATNAGIRI", 
         "Area sq.m": 21735.04, 
         "Sheet_Link": "https://docs.google.com/spreadsheets/d/1XUZh68qgDmtHGh6k_ye2rs3KgaMTXADJUmRT33tgNxY/edit?usp=sharing"
         },
        {
         "Sr.no": 2, "Project Name": "ATS BYCULLA", 
         "Area sq.m": 23442.32, 
         "Sheet_Link": "https://docs.google.com/spreadsheets/d/1bN7RayW-rBo2Km6t1ImRoDZUQJvMhLjUDNI4ma6WNb4/edit?usp=sharing"
         },
        {
         "Sr.no": 3, "Project Name": "SHIRDI COMPLEX", 
         "Area sq.m": 745387, 
         "Sheet_Link": "https://docs.google.com/spreadsheets/d/1lC64zuM-S_wgmF9TAYGzD7Z6M5CgXhcN5RDs_0-JkMw/edit?usp=sharing"
        },
        {
         "Sr.no": 4, "Project Name": "POLICE HOUSING KANDIVALI", 
         "Area sq.m":  65935.19, 
         "Sheet_Link": "https://docs.google.com/spreadsheets/d/1I4oLusSWDtjMwo0i6Bf1gM9oIzDuZVxMM4Nl0AcsvDU/edit?usp=sharing"
        },
        {
         "Sr.no": 5, "Project Name": "NAGPUR HOSTEL", 
         "Area sq.m":  33150, 
         "Sheet_Link": "https://docs.google.com/spreadsheets/d/13mAbS-9Kq8kqMBzHp90qRn_UEgiXryeyR_72x-jiM9k/edit?usp=sharing"
        },
        {
         "Sr.no": 6, "Project Name": "GERA KHARADI", 
         "Area sq.m": 117339.03, 
         "Sheet_Link": "https://docs.google.com/spreadsheets/d/1Da7xRWPD3EsKlUWmKnweeWGwsXqeEXdgTOXI6DnW5vM/edit?usp=sharing"
        },
        {
         "Sr.no": 7, "Project Name": "CHANDRAPUR", 
         "Area sq.m": 69480.64, 
         "Sheet_Link": "https://docs.google.com/spreadsheets/d/1S2t8j1g7gOVtnxZEn6S32wcOdTbCMkpJ5lU-DH1fxvg/edit?usp=sharing"
        },
        {
         "Sr.no": 8, "Project Name": "GERA IMPERIUM", 
         "Area sq.m":  1351556.04, 
         "Sheet_Link": "https://docs.google.com/spreadsheets/d/1d3UrxXAxfOlpShswUiggDWiyGUzwLS1JhkA5Xbk9NYw/edit?usp=sharing"
        },
        {
         "Sr.no": 9, "Project Name": "HINJEWADI", 
         "Area sq.m":  27236.30, 
         "Sheet_Link": "https://docs.google.com/spreadsheets/d/1pKoLaRcDO2J8d0gKWtOK3SnCqmno_zIDpp9sijwzang/edit?usp=sharing"
        },
        {
         "Sr.no": 10, "Project Name": "MEDICAL COLLEGE JALGAON", 
         "Area sq.m": 104592.23, 
         "Sheet_Link": "https://docs.google.com/spreadsheets/d/1klERjX1ZorvnwkulmsypdxEkFJxrD3iF6RB4kN-OGt0/edit?usp=sharing"
        },
        {
         "Sr.no": 11, "Project Name": "MEDICAL COLLEGE BHOJPUR", 
         "Area sq.m":  109075, 
         "Sheet_Link": "https://docs.google.com/spreadsheets/d/1MKTFpUMxVlHAadPRkvCb5jOP1EBrMGwoxtFoJYMHPhU/edit?usp=sharing"
        },
        {
         "Sr.no": 12, "Project Name": "INCUBATION CENTER KALAMBOLI", 
         "Area sq.m":  71616.06, 
         "Sheet_Link": "https://docs.google.com/spreadsheets/d/16sX-cwe2H5jpUmHWd2ig1M1xKF2hHvnaIFKJZO5HQW8/edit?usp=sharing"
        }
    ]

    # --- CASE A: AGAR DETAIL VIEW MEIN HAIN (EXCEL SHEET VIEW) ---
    if st.session_state.area_view_mode == 'detail' and st.session_state.selected_project:
        if st.button("⬅️ Back"):
            st.session_state.area_view_mode = 'table'
            st.session_state.selected_project = None
            st.rerun()

        st.title(f"📐 Detailed Area View: {st.session_state.selected_project}")
        st.markdown(f'<h2 style="font-size: 24px;">📐 Detailed Area View: {st.session_state.selected_project}</h2>', unsafe_allow_html=True)

        try:
            # Selected project ka link nikalna
            link = next(p["Sheet_Link"] for p in projects_list if p["Project Name"] == st.session_state.selected_project)
            csv_url = link.split('/edit')[0] + "/export?format=csv"
            
            # Header dhundne ka logic
            raw_data = pd.read_csv(csv_url, header=None).head(20)
            h_idx = 0
            for i, row in raw_data.iterrows():
                row_str = " ".join(row.astype(str)).lower()
                if any(kw in row_str for kw in ["description", "particular", "area", "sq.m", "sqft"]):
                    h_idx = i
                    break
            
            df_detail = pd.read_csv(csv_url, skiprows=h_idx)
            df_detail.columns = [str(c).strip() for c in df_detail.columns]
            
            # Relevant columns filter karna
            a_cols = [c for c in df_detail.columns if any(x in c.lower() for x in ['sr', 'desc', 'particular', 'area', 'sqm', 'sqft'])]
            
            if len(a_cols) >= 2:
                df_f = df_detail[a_cols].dropna(subset=[a_cols[1]]).copy()
                st.dataframe(df_f, use_container_width=True, hide_index=True)
            else:
                st.warning("Area details columns nahi mile.")
        except Exception as e:
            st.error(f"Area Error: {e}")

    # --- CASE B: AGAR MASTER SUMMARY MEIN HAIN (TABLE VIEW) ---
    else:
        if st.button("⬅️ Back"):
            st.session_state.current_page = 'landing'
            st.rerun()

        # Purani lines:
# st.markdown('<div class="main-title">📐 Built-up Area Summary</div>', unsafe_allow_html=True)
# st.markdown("---")

# Naya updated code (Size chota aur clean):
        st.markdown('<h2 style="font-size: 24px !important; font-weight: bold; color: #002060; margin-bottom: 5px;">📐 Built-up Area Summary</h2>', unsafe_allow_html=True)
        st.markdown('<hr style="border: 1px solid #002060; margin-top: 0px; margin-bottom: 20px;">', unsafe_allow_html=True)

        # Master Summary Table
        st.subheader("📊 Master Summary")
        df_area_sum = pd.DataFrame(projects_list)[["Sr.no", "Project Name", "Area sq.m"]]

        # Styling
        styled_area_df = df_area_sum.style.set_table_styles([
            {'selector': 'th', 'props': [('background-color', '#002060'), ('color', 'white'), ('font-size', '18px'), ('text-align', 'center'), ('font-weight', 'bold')]},
            {'selector': 'td', 'props': [('font-size', '16px'), ('padding', '10px')]}
        ])
        
        # Dynamic height to remove blank cells
        dynamic_height = (len(df_area_sum) * 35.2) + 38

        # Interactive Table
        event = st.dataframe(
            styled_area_df,
            use_container_width=True,
            hide_index=True,
            on_select="rerun",
            selection_mode="single-row",
            height=int(dynamic_height)
        )

        # Row Selection Logic (Isse naya page khulega)
        if len(event.selection.rows) > 0:
            selected_row_index = event.selection.rows[0]
            project_to_open = df_area_sum.iloc[selected_row_index]["Project Name"]
            
            st.session_state.selected_project = project_to_open
            st.session_state.area_view_mode = 'detail'
            st.rerun()
