import streamlit as st
import pandas as pd

# --- PAGE SETUP ---
st.set_page_config(page_title="Post Tender Dashboard", layout="wide")

# --- 2. CUSTOM CSS (Isse styling aur animation aayegi) ---
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    thead tr th { background-color: #002366 !important; color: white !important; font-weight: bold !important; }
    tbody tr:hover { background-color: #e6f0ff !important; transition: 0.3s; }
    .metric-card { 
        background-color: #f8f9fa; border-radius: 10px; padding: 15px; 
        border-left: 5px solid #002366; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); 
    }
    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
    .main-container { animation: fadeIn 1s; }
    </style>
    """, unsafe_allow_html=True)

# --- 1. PROJECT DATA (SAAF BLOCKS FORMAT) ---
projects = [
    {
        "Project Name": "ATS BYCULLA",
        "Type of Contractor": "Lumpsum",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Last Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_ID": "ID_ATS"
    },
    {
        "Project Name": "GERA IMPERIUM GATEWAY",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Last Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_ID": "ID_GERA_GATEWAY"
    },
    {
        "Project Name": "GERA KHARADI POJ",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Last Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_ID": "ID_GERA_KHARADI"
    },
    {
        "Project Name": "MEDICAL COLLEGE BHOJPUR",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Last Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_ID": "ID_BHOJPUR"
    },
    {
        "Project Name": "MEDICAL COLLEGE JALGAON",
        "Type of Contractor": "EPC",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Last Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_ID": "ID_JALGAON"
    },
    {
        "Project Name": "NAGPUR SYMBIOSIS-HOSTEL",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Last Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_ID": "ID_NAGPUR_SYM"
    },
    {
        "Project Name": "TATA REALTY",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Last Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_ID": "ID_TATA"
    },
    {
        "Project Name": "ADMIN BUILDING, RATNAGIRI",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Last Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_ID": "ID_ADMIN_RAT"
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
        "Last Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_ID": "ID_KHAJAJI"
    },
    {
        "Project Name": "MEDICAL COLLEGE MUNGER",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Last Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_ID": "ID_MUNGER"
    },
    {
        "Project Name": "MEDICAL COLLEGE SATARA",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Last Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_ID": "ID_SATARA"
    },
    {
        "Project Name": "POLICE HOUSING KANDIVALI",
        "Type of Contractor": "Lumpsum",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Last Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_ID": "ID_KANDIVALI"
    },
    {
        "Project Name": "RATNAGIRI AIR TERMINAL",
        "Type of Contractor": "EPC",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Last Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_ID": "ID_RAT_AIR"
    },
    {
        "Project Name": "PLATFORM BEUTIFICATION",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Last Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_ID": "ID_PLATFORM"
    },
    {
        "Project Name": "RATNAGIRI RAILWAY STATION",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Last Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_ID": "ID_RAT_RAIL"
    },
    {
        "Project Name": "SMART CITY RATNAGIRI",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Last Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_ID": "ID_SMART_CITY"
    },
    {
        "Project Name": "BMC T&C HUB DAHISAR",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Last Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_ID": "ID_DAHISAR"
    },
    {
        "Project Name": "SYMBIOSIS CANTEEN BUILDING",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Last Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_ID": "ID_SYM_CANTEEN"
    },
    {
        "Project Name": "SYMBIOSIS WORLD SCHOOL",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Last Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_ID": "ID_SYM_SCHOOL"
    },
    {
        "Project Name": "SYMBIOSIS 944 HOSTEL",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Last Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_ID": "ID_SYM_944"
    },
    {
        "Project Name": "SYMBIOSIS 1320 HOSTEL",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Last Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_ID": "ID_SYM_1320"
    },
    {
        "Project Name": "UDAIPUR AIR TERMINAL",
        "Type of Contractor": "EPC",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Last Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_ID": "ID_UDAIPUR"
    },
    {
        "Project Name": "MEDITATION CENTRE SYMBIOSIS NAGPUR",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Last Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_ID": "ID_SYM_MED"
    },
    {
        "Project Name": "SYMBIOSIS 1320 HOSTEL LAVALE",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Last Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_ID": "ID_LAVALE_1320"
    },
    {
        "Project Name": "SYMBIOSIS SIBM EXTENSION LAVALE",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Last Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_ID": "ID_SIBM_EXT"
    },
    {
        "Project Name": "IICT CAMPUS - GOREGAON",
        "Type of Contractor": "Lumpsum",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Last Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_ID": "ID_GOREGAON"
    }
]

# --- DASHBOARD UI ---
st.title("🏗️ Post Tender Management Dashboard System")
st.markdown("---")

# DataFrame index setup (1 se start karne ke liye)
df_home = pd.DataFrame(projects)
df_home.index = range(1, len(df_home) + 1)

# Seedha Table wala Section shuru
st.subheader("📌 Master Project List")

# Columns jo dikhane hain
display_columns = [
    "Project Name", "Type of Contractor", "Area", 
    "Original BOQ Amount", "Original Budget", 
    "Last Revised Budget", "Client Bill Amount", "Consumed Amount"
]

# --- STATUS TEXT COLOURING (Pills/Background Hatane ke liye) ---
def format_contractor(val):
    # Sirf text ka color change hoga, background white hi rahega
    if val == "Lumpsum": 
        color = "#FFB433"  # Dark Gold/Brass (White background par saaf dikhega)
    elif val == "Item rate": 
        color = "#48A111"  # Dark Green
    else: 
        color = "#1C4D8D"  # Dark Royal Blue (EPC ke liye)
        
    return f'color: {color}; font-weight: bold; background-color: white;'

# --- TABLE DISPLAY ---
# Baaki styling aur format same rahega
styled_df = df_home[display_columns].style.map(format_contractor, subset=["Type of Contractor"]) \
            .format({
                "Original BOQ Amount": "₹{:,.0f}", 
                "Original Budget": "₹{:,.0f}", 
                "Last Revised Budget": "₹{:,.0f}",
                "Client Bill Amount": "₹{:,.0f}",
                "Consumed Amount": "₹{:,.0f}"
            })

st.dataframe(
    styled_df, 
    use_container_width=True, 
    height=(len(df_home) + 1) * 35 + 40
)
