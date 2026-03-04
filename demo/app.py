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
    if st.button("Generate Report", key="explain_btn"):
        x_df = st.session_state.audit_sample.loc[[row_id]].drop(columns=['charges'])
        x_orig = x_df.iloc[0]
        
        # Capture the print output from the TRUSTRegressor class
        explain_report = capture_output(model.explain, x_orig, mode="report")
        
        st.subheader("TRUST™ Prediction Audit Report")
        st.code(explain_report, language="text")

with tab2:
    compare_ids = st.multiselect("Select 2 Row IDs to Compare", 
                                 st.session_state.audit_sample.index)
    count = len(compare_ids)
    if count == 0:
        st.info("Select two rows from the table above.")
    elif count == 1:
        st.info("Select one more row to enable the comparison.")
    elif count == 2:
        st.success("Comparison ready.")
        if st.button("Generate Report", key="compare_btn"):
            x1 = st.session_state.audit_sample.loc[[compare_ids[0]]].drop(columns=['charges'])
            x2 = st.session_state.audit_sample.loc[[compare_ids[1]]].drop(columns=['charges'])
            
            # 0. Prime backend
            import matplotlib as mpl            
            mpl.use("module://matplotlib_inline.backend_inline")
            # 1. Capture the print output from the TRUSTRegressor class
            compare_report = capture_output(model.compare, x1, x2, filename="Comp_demo")
            
            # 2. Show it
            st.subheader("TRUST™ Profile Comparison Report")
            st.code(compare_report, language="text")
            
            # 3. Grab and show plots
            #import plotly.graph_objects as go
            #from plotly.io import renderers
            import os        
            from os.path import getmtime
            st.subheader("Supporting Charts")
            plot_files = [f for f in os.listdir(".") if f.endswith("Comp_demo.png")]
            if plot_files:
                plot_files.sort(key=lambda x: getmtime(x))
                cols = st.columns(2) # expects 2 plots will be generated
                for idx, plot in enumerate(plot_files):
                    with cols[idx % 2]:
                        st.image(plot, use_container_width=True)
                        os.remove(plot)
            else:
                st.info("No charts available to display.")
    else:
        st.warning(f"You have selected {count} rows. Please remove {count - 2} to proceed.")
