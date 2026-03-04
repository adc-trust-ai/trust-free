import streamlit as st
import pandas as pd
import io
from contextlib import redirect_stdout
from trust import TRUSTRegressor

# --- 1. SETTINGS & BRANDING ---
st.set_page_config(page_title="Whitebox Lab", layout="wide")

def capture_output(func, *args, **kwargs):
    f = io.StringIO()
    with redirect_stdout(f):
        func(*args, **kwargs)
    return f.getvalue()

# --- 2. DATA & MODEL TRAINING (CACHED) ---
@st.cache_resource
def initialize_lab():
    # Load the Kaggle Medical Insurance dataset
    df = pd.read_csv("https://raw.githubusercontent.com/adc-trust-ai/trust-free/refs/heads/main/notebooks/data/insurance.csv")
    X = df.iloc[:,:-1]
    y = df.iloc[:,-1]
    
    # Train the model with depth 1
    model = TRUSTRegressor(max_depth=1)
    
    # Capture the specific training log
    train_log = capture_output(model.fit, X, y, catvar=[1, 4, 5])
    
    return model, train_log, df

model, training_log, full_df = initialize_lab()

# --- 3. THE USER INTERFACE ---
st.title("Whitebox Lab | TRUST™ Demonstration")
st.markdown("**Chief Scientist:** Albert Dorador, Ph.D. (Statistics, UW-Madison)")

# The "Audit Trail" - showing how the model was built
with st.expander("🛠️ View Model Training Audit (Live Log)"):
    st.code(training_log, language="text")

st.write("---")

# 4. INTERACTIVE AUDIT SAMPLE
if 'audit_sample' not in st.session_state:
    st.session_state.audit_sample = full_df.sample(5)

col_header, col_btn = st.columns([3, 1])
with col_header:
    st.subheader("Current Audit Sample (Insurance Holders)")
with col_btn:
    if st.button("🔄 Refresh Sample"):
        st.session_state.audit_sample = full_df.sample(5)

st.dataframe(st.session_state.audit_sample, use_container_width=True)

# 5. AUDIT TOOLS: .explain() and .compare()
st.write("---")
tab1, tab2 = st.tabs(["🔍 Single-Profile Explanation", "⚖️ Multi-Profile Comparison"])

with tab1:
    row_id = st.selectbox("Select Row ID to Audit", st.session_state.audit_sample.index)
    if st.button("Generate Report"):
        x_orig = st.session_state.audit_sample.loc[[row_id]].drop(columns=['charges'])
        
        # Capture the print output from the TRUSTRegressor class
        explain_report = capture_output(model.explain, x_orig, mode="report")
        
        st.subheader("TRUST™ Prediction Audit Report")
        st.code(explain_report, language="text")

with tab2:
    compare_ids = st.multiselect("Select 2 Row IDs to Compare", 
                                 st.session_state.audit_sample.index, 
                                 max_selections=2)
    
    if st.button("Generate Report") and len(compare_ids) == 2:
        x1 = st.session_state.audit_sample.loc[[compare_ids[0]]].drop(columns=['charges'])
        x2 = st.session_state.audit_sample.loc[[compare_ids[1]]].drop(columns=['charges'])
        
        # Capture the print output from the TRUSTRegressor class
        compare_report = capture_output(model.compare, x1, x2, mode="report")
        
        st.subheader("TRUST™ Profile Comparison Report")
        st.code(compare_report, language="text")
