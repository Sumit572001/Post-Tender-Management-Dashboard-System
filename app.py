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

# --- 3. UNIVERSAL DYNAMIC SHEET INTEGRATION ---
if selected_project != "-- Select a Project --":
    st.markdown("---")
    st.subheader(f"📊 Detailed View: {selected_project}")
    
    row = df_home[df_home["Project Name"] == selected_project].iloc[0]
    raw_url = row.get("Sheet_Link")
    
    if raw_url and "docs.google.com" in raw_url:
        try:
            csv_url = raw_url.split("/edit")[0] + "/export?format=csv"
            
            # Step 1: Pehle 20 rows read karo headers dhoondne ke liye
            temp_df = pd.read_csv(csv_url, header=None, nrows=20)
            
            header_row = 0
            for i, r in temp_df.iterrows():
                # Agar row mein 'Sr.' aur 'Particular' ya 'Description' dikhe toh wo header hai
                row_values = [str(x).lower() for x in r.values]
                if any("sr." in s for s in row_values) and any("particular" in s or "description" in s for s in row_values):
                    header_row = i
                    break
            
            # Step 2: Sahi header row se data load karo
            df_detail = pd.read_csv(csv_url, skiprows=header_row)
            
            # Clean column names (Remove newlines and extra spaces)
            df_detail.columns = [str(c).replace('\n', ' ').strip() for c in df_detail.columns]

            # Step 3: Flexible Column Finder (Har sheet ke liye)
            def find_col(possible_names):
                for col in df_detail.columns:
                    if any(name.lower() in col.lower() for name in possible_names):
                        return col
                return None

            mapping = {
                "Sr.No": find_col(["Sr. No", "Sr.No", "Sl.No"]),
                "Description": find_col(["Particular", "Description", "Items"]),
                "Original Budget": find_col(["Original Budget", "Orignal Budget", "ESTIMATION ZERO COST"]),
                "Revised Budget": find_col(["Total Revised Budget", "TENDER ZERO COST"]),
                "BOQ Amount": find_col(["Original BOQ Amount", "ZERO AMOUNT"]),
                "Client Bill": find_col(["Client Bill", "Cummulative Client"]),
                "Consumed Amount": find_col(["Consumed Amount", "Consumed Budget"])
            }

            selected_cols = [v for k, v in mapping.items() if v is not None]

            if len(selected_cols) > 2:
                final_df = df_detail[selected_cols].copy()
                
                # Styling
                def row_style(row):
                    desc_col = mapping["Description"]
                    if desc_col and "TOTAL" in str(row[desc_col]).upper():
                        return ['background-color: #28a745; color: white; font-weight: bold;'] * len(row)
                    return [''] * len(row)

                st.dataframe(final_df.style.apply(row_style, axis=1), use_container_width=True, hide_index=True)
                st.success(f"✅ Auto-detected format and loaded data for {selected_project}")
            else:
                st.warning("⚠️ Column names detect nahi ho pa rahe hain. Sheet ka header check karein.")
                st.write("Ditected Columns:", df_detail.columns.tolist())

        except Exception as e:
            st.error(f"❌ Sheet Load Error: {e}")
