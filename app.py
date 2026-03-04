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
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Total Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_Link": "ID_MUNGER"
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
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Total Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_Link": "ID_KANDIVALI"
    },
    {
        "Project Name": "RATNAGIRI AIR TERMINAL",
        "Type of Contractor": "EPC",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Total Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_Link": "ID_RAT_AIR"
    },
    {
        "Project Name": "PLATFORM BEUTIFICATION",
        "Type of Contractor": "Item rate",
        "Area": "0",
        "Original BOQ Amount": 0,
        "Original Budget": 0,
        "Total Revised Budget": 0,
        "Client Bill Amount": 0,
        "Consumed Amount": 0,
        "Sheet_Link": "ID_PLATFORM"
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

# --- DASHBOARD UI ---
st.title("🏗️ Post Tender Management Dashboard")
st.markdown("---")

# DataFrame index setup
df_home = pd.DataFrame(projects)
df_home.index = range(1, len(df_home) + 1)

# --- NEW: PROJECT SELECTION ---
st.subheader("🔍 Select Project to View Details")

# Aapne kaha tha ki "Detailed data dekhne ke liye project chunein:" wali line nahi chahiye, 
# isliye label ko khali ("") kar diya hai.
selected_project = st.selectbox(
    label="", 
    options=["-- Select a Project --"] + df_home["Project Name"].tolist(),
    label_visibility="collapsed"  # Isse label ki jagah bhi nahi gheraga
)
st.markdown("---")
st.subheader("📌 Master Project List")

# Columns jo dikhane hain
display_columns = [
    "Project Name", "Type of Contractor", "Area", 
    "Original BOQ Amount", "Original Budget", 
    "Total Revised Budget", "Client Bill Amount", "Consumed Amount"
]

# --- STATUS TEXT COLOURING ---
def format_contractor(val):
    if val == "Lumpsum": color = "#FFB433"
    elif val == "Item rate": color = "#48A111"
    else: color = "#1C4D8D"
    return f'color: {color}; font-weight: bold; background-color: white;'

# --- TABLE DISPLAY ---
styled_df = df_home[display_columns].style.map(format_contractor, subset=["Type of Contractor"]) \
            .format({
                "Original BOQ Amount": "₹{:,.0f}", 
                "Original Budget": "₹{:,.0f}", 
                "Total Revised Budget": "₹{:,.0f}",
                "Client Bill Amount": "₹{:,.0f}",
                "Consumed Amount": "₹{:,.0f}"
            })

st.dataframe(
    styled_df, 
    use_container_width=True, 
    height=(len(df_home) + 1) * 35 + 40
)

# --- 3. GOOGLE SHEET DATA INTEGRATION (HIGHLIGHT TOTAL ROW) ---
if selected_project != "-- Select a Project --":
    st.markdown("---")
    st.subheader(f"📊 Detailed View: {selected_project}")
    
    row = df_home[df_home["Project Name"] == selected_project].iloc[0]
    raw_url = row.get("Sheet_Link") if row.get("Sheet_Link") else row.get("Sheet_ID", "")
    
    if raw_url and "docs.google.com" in raw_url:
        try:
            csv_url = raw_url.split("/edit")[0] + "/export?format=csv" if "/edit" in raw_url else raw_url
            df_detail = pd.read_csv(csv_url, skiprows=5)

            def find_column(search_term, columns):
                for col in columns:
                    if search_term.lower() in col.lower(): return col
                return None

            mapping = {
                "Sr.No": find_column("Sr.No", df_detail.columns),
                "Item Description": find_column("Item Description", df_detail.columns),
                "Original Budget": find_column("Original Budget", df_detail.columns),
                "Revised Budget": find_column("Total Revised Budget", df_detail.columns),
                "BOQ Amount": find_column("Original BOQ Amount", df_detail.columns),
                "Client Bill": find_column("Cummulative Client Bill", df_detail.columns),
                "Consumed Amount": find_column("Consumed Amount", df_detail.columns)
            }

            final_columns = [v for k, v in mapping.items() if v is not None]

            if final_columns:
                display_df = df_detail[final_columns].copy()
                
                # 🛠️ UPDATED HIGHLIGHT LOGIC FOR BACKGROUND COLOUR 🛠️
                def highlight_total_row_background(row):
                    # Item Description mein "Total Project" dhoondo
                    desc_col = mapping["Item Description"]
                    if desc_col and isinstance(row[desc_col], str) and "Total Project" in row[desc_col]:
                        # 🟢 Green background, white text, bold font puri row ke liye
                        return ['background-color: #D4EDDA; color: #155724; font-weight: bold; border-color: #C3E6CB'] * len(row)
                    return [''] * len(row)

                # Styling apply karte waqt axis=1 zaroor rakhein
                styled_df = display_df.style.apply(highlight_total_row_background, axis=1)
                
                # Table display karein
                st.dataframe(styled_df, use_container_width=True, hide_index=True)
                st.success(f"✅ Data loaded! Total row highlighted.")
            else:
                st.warning("⚠️ Headers nahi mil rahe.")

        except Exception as e:
            st.error(f"❌ Error: {e}")
