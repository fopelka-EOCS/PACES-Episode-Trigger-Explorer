import streamlit as st
import pandas as pd

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("Grouped Episodes - Grouped.csv")
    # Ensure Trigger Code is treated as string
    df["Trigger Code"] = df["Trigger Code"].astype(str)
    return df

df = load_data()

st.title("PACES Episode Trigger Explorer")

# Episode selection
episode_list = sorted(df["Episode Short Name"].dropna().unique())
episode = st.selectbox("Select an Episode Short Name:", episode_list)

# Filter data
filtered = df[df["Episode Short Name"] == episode].copy()

# Sort numerically when possible
def numeric_sort_key(x):
    try:
        return float(x)
    except:
        return float('inf')

filtered = filtered.sort_values(by="Trigger Code", key=lambda col: col.map(numeric_sort_key))

# Display results
st.subheader(f"Trigger Codes for: {episode}")
st.dataframe(
    filtered[["Trigger Code", "Long Description"]]
    .rename(columns={"Trigger Code": "CPT Code"})
)

st.markdown(
    """
    <div style="text-align: center; font-size: 0.8em; color: #666; margin-top: 2em;">
        <hr>
        <strong>Data Versions</strong><br>
        PACES Episodes: Updated with PACES v5.3 (Jan 2026 Release)<br>
        CPT Descriptions: From NHSN public release file<br><br>
        <em style="font-size: 0.75em;">
            CPT® is a registered trademark of the American Medical Association.<br>
            Descriptions shown here reflect the NHSN public release file and may not represent the full AMA CPT code set.
        </em>
    </div>
    """,
    unsafe_allow_html=True
)
