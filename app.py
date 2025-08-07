
import streamlit as st
import random

st.set_page_config(page_title="Lazy Mayor’s Milestone Tool", layout="centered")

# --------------------
# Embedded Milestone Data
# --------------------
milestones = [
  {
    "Milestone": "Earn Neo Simoleons",
    "Category": "neosimoleon",
    "Phase 1": 1171,
    "Phase 2": 2367,
    "Phase 3": 8462,
    "Total": 12000,
    "Phase 1+2": 3538,
    "Level": "30-99"
  },
  {
    "Milestone": "Produce and Collect Commercial Items (2)",
    "Category": "commercial",
    "Phase 1": 768,
    "Phase 2": 2590,
    "Phase 3": 8142,
    "Total": 11500,
    "Phase 1+2": 3358,
    "Level": "30-99"
  },
  {
    "Milestone": "Earn Simoleons (2)",
    "Category": "simoleons",
    "Phase 1": 1256,
    "Phase 2": 3537,
    "Phase 3": 6207,
    "Total": 11000,
    "Phase 1+2": 4793,
    "Level": "30-99"
  },
  {
    "Milestone": "Launch War Disaster",
    "Category": "war disaster",
    "Phase 1": 882,
    "Phase 2": 2970,
    "Phase 3": 7148,
    "Total": 11000,
    "Phase 1+2": 3852,
    "Level": "all"
  },
  {
    "Milestone": "Produce and Collect Industrial Items (2)",
    "Category": "industrial",
    "Phase 1": 792,
    "Phase 2": 2737,
    "Phase 3": 6972,
    "Total": 10501,
    "Phase 1+2": 3529,
    "Level": "30-99"
  },
  {
    "Milestone": "Produce and Collect OMEGA Canister",
    "Category": "omega",
    "Phase 1": 1344,
    "Phase 2": 3024,
    "Phase 3": 6132,
    "Total": 10500,
    "Phase 1+2": 4368,
    "Level": "30-99"
  },
  {
    "Milestone": "Earn War points",
    "Category": "war points",
    "Phase 1": 987,
    "Phase 2": 2780,
    "Phase 3": 6733,
    "Total": 10500,
    "Phase 1+2": 3767,
    "Level": "all"
  },
  {
    "Milestone": "Earn Golden Keys",
    "Category": "golden keys",
    "Phase 1": 779,
    "Phase 2": 3061,
    "Phase 3": 6360,
    "Total": 10200,
    "Phase 1+2": 3840,
    "Level": "all"
  },
  {
    "Milestone": "Do Cargo Ship Deliveries ",
    "Category": "cargo",
    "Phase 1": 891,
    "Phase 2": 3001,
    "Phase 3": 6108,
    "Total": 10000,
    "Phase 1+2": 3892,
    "Level": "all"
  },
  {
    "Milestone": "Do Airport Deliveries (2)",
    "Category": "airport",
    "Phase 1": 1437,
    "Phase 2": 2432,
    "Phase 3": 5131,
    "Total": 9000,
    "Phase 1+2": 3869,
    "Level": "30-99"
  },
  {
    "Milestone": "Upgrade Residential Zones",
    "Category": "residential",
    "Phase 1": 865,
    "Phase 2": 2504,
    "Phase 3": 5132,
    "Total": 8501,
    "Phase 1+2": 3369,
    "Level": "all"
  },
  {
    "Milestone": "Trade items in trade depot",
    "Category": "trade",
    "Phase 1": 727,
    "Phase 2": 2461,
    "Phase 3": 5313,
    "Total": 8501,
    "Phase 1+2": 3188,
    "Level": "all"
  },
  {
    "Milestone": "Earn Simoleons (1)",
    "Category": "simoleons",
    "Phase 1": 1020,
    "Phase 2": 2297,
    "Phase 3": 5184,
    "Total": 8501,
    "Phase 1+2": 3317,
    "Level": "15-29"
  },
  {
    "Milestone": "Do Airport Deliveries (1)",
    "Category": "airport",
    "Phase 1": 1422,
    "Phase 2": 2399,
    "Phase 3": 4179,
    "Total": 8000,
    "Phase 1+2": 3821,
    "Level": "15-29"
  },
  {
    "Milestone": "Produce and Collect Industrial Items (1)",
    "Category": "industrial",
    "Phase 1": 591,
    "Phase 2": 1883,
    "Phase 3": 5526,
    "Total": 8000,
    "Phase 1+2": 2474,
    "Level": "15-29"
  },
  {
    "Milestone": "Do War Deliveries",
    "Category": "war deliveries",
    "Phase 1": 583,
    "Phase 2": 2182,
    "Phase 3": 5234,
    "Total": 7999,
    "Phase 1+2": 2765,
    "Level": "all"
  },
  {
    "Milestone": "Produce and Collect Commercial Items (1)",
    "Category": "commercial",
    "Phase 1": 510,
    "Phase 2": 1460,
    "Phase 3": 5030,
    "Total": 7000,
    "Phase 1+2": 1970,
    "Level": "15-29"
  },
  {
    "Milestone": "Complete Rows in the Export HQ ",
    "Category": "export HQ",
    "Phase 1": 1602,
    "Phase 2": 1799,
    "Phase 3": 3100,
    "Total": 6501,
    "Phase 1+2": 3401,
    "Level": "all"
  },
  {
    "Milestone": "Vote in Design Challenge ",
    "Category": "vote",
    "Phase 1": 1037,
    "Phase 2": 1753,
    "Phase 3": 3711,
    "Total": 6501,
    "Phase 1+2": 2790,
    "Level": "all"
  },
  {
    "Milestone": "Do Airport Deliveries (0) ",
    "Category": "airport",
    "Phase 1": 1413,
    "Phase 2": 1589,
    "Phase 3": 2298,
    "Total": 5300,
    "Phase 1+2": 3002,
    "Level": "11-14"
  },
  {
    "Milestone": "Launch Vu Disasters ",
    "Category": "vu disasters",
    "Phase 1": 631,
    "Phase 2": 2127,
    "Phase 3": 3542,
    "Total": 6300,
    "Phase 1+2": 2758,
    "Level": "all"
  },
  {
    "Milestone": "Transport passengers ",
    "Category": "trains",
    "Phase 1": 720,
    "Phase 2": 1216,
    "Phase 3": 2564,
    "Total": 4500,
    "Phase 1+2": 1936,
    "Level": "all"
  },
  {
    "Milestone": "Earn Epic Points ",
    "Category": "epic",
    "Phase 1": 384,
    "Phase 2": 864,
    "Phase 3": 3551,
    "Total": 4799,
    "Phase 1+2": 1248,
    "Level": "all"
  }
]

# --------------------
# Header
# --------------------
st.markdown("## 🛌 Lazy Mayor’s Milestone Tool")

# --------------------
# City Level Input
# --------------------
city_level = st.number_input("What's your city level?", min_value=1, max_value=99, value=30)

def allowed_for_level(req, level):
    if req == "all":
        return True
    if req == "30-99":
        return level >= 30
    if req == "15-29":
        return 15 <= level <= 29
    if req == "11-14":
        return 11 <= level <= 14
    return False

# --------------------
# Filtered Milestones
# --------------------
filtered = [m for m in milestones if allowed_for_level(m["Level"], city_level)]

# --------------------
# State Handling
# --------------------
if "full" not in st.session_state:
    st.session_state.full = [None]*10
if "partial" not in st.session_state:
    st.session_state.partial = [None]*5

def clear_full(): st.session_state.full = [None]*10
def clear_partial(): st.session_state.partial = [None]*5

def randomize(section, count, avoid_cats):
    pool = [m for m in filtered if m["Category"] not in avoid_cats]
    selected = random.sample(pool, min(count, len(pool)))
    return [m["Category"] for m in selected]

def get_name(cat):
    for m in filtered:
        if m["Category"] == cat:
            return m["Milestone"]
    return "—"

def get_milestone(cat):
    for m in filtered:
        if m["Category"] == cat:
            return m
    return None

# --------------------
# Controls
# --------------------
col1, col2 = st.columns(2)
with col1:
    if st.button("🔴 Clear Full Milestones"):
        clear_full()
    if st.button("🎲 Randomize Full"):
        used = set(st.session_state.partial)
        st.session_state.full = randomize("full", 10, avoid_cats=used)
with col2:
    if st.button("🔴 Clear Partial Milestones"):
        clear_partial()
    if st.button("🎲 Randomize Partial"):
        used = set(st.session_state.full)
        st.session_state.partial = randomize("partial", 5, avoid_cats=used)

# --------------------
# Full Milestones
# --------------------
st.markdown("### ✅ Pick 10 Full Milestones (Phases 1 + 2 + 3)")
used_categories = set()

for i in range(10):
    current = st.session_state.full[i]
    options = ["—"] + [m["Category"] for m in filtered if m["Category"] not in used_categories or m["Category"] == current]
    if current in options:
        index = options.index(current)
    else:
        index = 0
    choice = st.selectbox(f"Full #{{i+1}}", options=options, format_func=get_name, index=index, key=f"full_{{i}}")
    st.session_state.full[i] = choice if choice != "—" else None
    if choice and choice != "—":
        used_categories.add(choice)

# --------------------
# Partial Milestones
# --------------------
st.markdown("### 🟡 Pick 5 Partial Milestones (Phases 1 + 2 only)")

for i in range(5):
    current = st.session_state.partial[i]
    options = ["—"] + [m["Category"] for m in filtered if m["Category"] not in used_categories or m["Category"] == current]
    if current in options:
        index = options.index(current)
    else:
        index = 0
    choice = st.selectbox(f"Partial #{{i+1}}", options=options, format_func=get_name, index=index, key=f"partial_{{i}}")
    st.session_state.partial[i] = choice if choice != "—" else None
    if choice and choice != "—":
        used_categories.add(choice)

# --------------------
# Scoring Summary
# --------------------
full_points = sum(get_milestone(cat)["Total"] for cat in st.session_state.full if cat and get_milestone(cat))
partial_points = sum(get_milestone(cat)["Phase 1+2"] for cat in st.session_state.partial if cat and get_milestone(cat))
grand_total = full_points + partial_points

st.markdown("### 📊 Live Scoring Summary")
st.markdown("🧮 Total Points:")
st.markdown(f"- Full Milestones: **{{full_points:,}}**")
st.markdown(f"- Partial Milestones: **{{partial_points:,}}**")
st.markdown(f"🎯 Grand Total: **{{grand_total:,}}**")
