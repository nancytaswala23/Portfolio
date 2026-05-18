import streamlit as st

st.set_page_config(
    page_title="Nancy Taswala | Data Scientist",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.block-container { padding-top: 2rem; padding-bottom: 2rem; max-width: 900px; }

/* HERO */
.hero-name {
    font-size: 2.8rem; font-weight: 600; color: #1B4F8A;
    letter-spacing: -0.03em; line-height: 1.1; margin-bottom: 0.4rem;
}
.hero-title {
    font-size: 1.05rem; color: #4a4a4a; margin-bottom: 1rem; font-weight: 400;
}
.hero-summary {
    font-size: 0.95rem; color: #333; line-height: 1.7;
    max-width: 680px; margin-bottom: 1.5rem;
}
.badge {
    display: inline-block; background: #e8f0fa; color: #1B4F8A;
    padding: 4px 12px; border-radius: 20px; font-size: 0.75rem;
    font-weight: 500; margin-bottom: 1.2rem;
}

/* STATS */
.stat-grid { display: grid; grid-template-columns: repeat(4,1fr); gap: 1px; background: #e2e8f0; border-radius: 10px; overflow: hidden; margin-bottom: 2.5rem; }
.stat-cell { background: #f7f9fc; padding: 1rem; text-align: center; }
.stat-num { font-size: 1.6rem; font-weight: 600; color: #1B4F8A; font-family: monospace; }
.stat-lbl { font-size: 0.65rem; text-transform: uppercase; letter-spacing: 0.08em; color: #888; margin-top: 2px; }

/* SECTION */
.sec-label { font-size: 0.65rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.12em; color: #1B4F8A; margin-bottom: 4px; }
.sec-title { font-size: 1.3rem; font-weight: 600; color: #0f0f0f; letter-spacing: -0.02em; margin-bottom: 1.5rem; }
.sec-divider { border: none; border-top: 1.5px solid #1B4F8A; margin-bottom: 1.5rem; }

/* SKILL TAGS */
.skill-section { margin-bottom: 0.6rem; }
.skill-label { font-size: 0.75rem; font-weight: 600; color: #1B4F8A; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 6px; }
.tag-row { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 0.8rem; }
.tag { font-size: 0.72rem; padding: 3px 9px; background: #e8f0fa; color: #1B4F8A; border-radius: 4px; font-weight: 500; }
.tag-plain { font-size: 0.72rem; padding: 3px 9px; background: #f1f5f9; color: #555; border-radius: 4px; border: 1px solid #e2e8f0; }

/* EXP */
.exp-wrap { border-left: 2px solid #1B4F8A; padding-left: 1rem; margin-bottom: 1.5rem; }
.exp-role { font-size: 0.95rem; font-weight: 600; color: #0f0f0f; }
.exp-org { font-size: 0.82rem; color: #1B4F8A; font-weight: 500; margin-top: 2px; }
.exp-date { font-size: 0.75rem; color: #888; font-family: monospace; margin-top: 2px; margin-bottom: 8px; }
.exp-bullet { font-size: 0.83rem; color: #333; line-height: 1.6; margin-bottom: 5px; padding-left: 12px; position: relative; }
.exp-bullet::before { content: "—"; position: absolute; left: 0; color: #1B4F8A; }

/* PROJECT CARD */
.proj-card {
    background: #fff; border: 1px solid #e2e8f0; border-radius: 10px;
    padding: 1.2rem; margin-bottom: 1rem;
    transition: border-color 0.2s;
}
.proj-card:hover { border-color: #1B4F8A; }
.proj-name { font-size: 0.95rem; font-weight: 600; color: #0f0f0f; margin-bottom: 6px; }
.proj-desc { font-size: 0.82rem; color: #555; line-height: 1.6; margin-bottom: 8px; }
.proj-metric { font-size: 0.75rem; font-family: monospace; color: #1B4F8A; font-weight: 600; background: #e8f0fa; padding: 2px 8px; border-radius: 4px; display: inline-block; margin-bottom: 8px; }
.proj-tag-row { display: flex; flex-wrap: wrap; gap: 5px; margin-bottom: 10px; }
.proj-tag { font-size: 0.68rem; padding: 2px 7px; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 3px; color: #666; }
.proj-links { display: flex; gap: 10px; }
.proj-link { font-size: 0.78rem; color: #1B4F8A; text-decoration: none; font-weight: 500; border: 1px solid #c5d8f0; border-radius: 4px; padding: 3px 10px; }
.proj-link:hover { background: #e8f0fa; }

/* PUB */
.pub-card { border-left: 3px solid #1B4F8A; background: #f7f9fc; border-radius: 0 8px 8px 0; padding: 1rem 1.2rem; }
.pub-title { font-size: 0.9rem; font-weight: 600; color: #0f0f0f; margin-bottom: 4px; }
.pub-meta { font-size: 0.78rem; color: #555; }

/* EDU */
.edu-card { background: #f7f9fc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 1rem 1.2rem; }
.edu-degree { font-size: 0.9rem; font-weight: 600; color: #0f0f0f; }
.edu-school { font-size: 0.8rem; color: #1B4F8A; font-weight: 500; margin-top: 2px; }
.edu-dates { font-size: 0.75rem; color: #888; font-family: monospace; margin-top: 3px; }

/* CONTACT */
.contact-link { display: flex; align-items: center; gap: 8px; padding: 10px 14px; background: #f7f9fc; border: 1px solid #e2e8f0; border-radius: 8px; text-decoration: none; color: #0f0f0f; font-size: 0.85rem; margin-bottom: 8px; }
.contact-link:hover { border-color: #1B4F8A; color: #1B4F8A; }

.stApp { background: #ffffff; }
</style>
""", unsafe_allow_html=True)

# ── HERO ──────────────────────────────────────────────────────
st.markdown('<div class="badge">● Available for Full-Time Roles · Boston, MA</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-name">Nancy Ketankumar Taswala</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-title">Data Scientist · Clinical Analytics · Machine Learning · Statistical Modeling</div>', unsafe_allow_html=True)
st.markdown("""
<div class="hero-summary">
M.S. Information Systems candidate at Northeastern University with 2+ years of experience in statistical modeling, predictive analytics, machine learning, and healthcare data analysis. Proficient in Python, R, SQL, and Tableau — focused on generating hypothesis-driven insights from complex clinical and operational datasets.
</div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
with c1: st.link_button("✉ Email", "mailto:taswala.n@northeastern.edu", use_container_width=True)
with c2: st.link_button("LinkedIn", "https://linkedin.com/in/nancytaswala23", use_container_width=True)
with c3: st.link_button("GitHub", "https://github.com/nancytaswala23", use_container_width=True)
with c4: st.link_button("Portfolio", "https://nancytaswala23.github.io", use_container_width=True)

st.markdown("""
<div class="stat-grid">
  <div class="stat-cell"><div class="stat-num">2+</div><div class="stat-lbl">Years Exp.</div></div>
  <div class="stat-cell"><div class="stat-num">0.85</div><div class="stat-lbl">ROC-AUC</div></div>
  <div class="stat-cell"><div class="stat-num">82%</div><div class="stat-lbl">Model Accuracy</div></div>
  <div class="stat-cell"><div class="stat-num">3</div><div class="stat-lbl">Live Projects</div></div>
</div>
""", unsafe_allow_html=True)

# ── SKILLS ────────────────────────────────────────────────────
st.markdown('<div class="sec-label">Expertise</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">Technical Skills</div>', unsafe_allow_html=True)
st.markdown('<hr class="sec-divider">', unsafe_allow_html=True)

st.markdown("""
<div class="skill-label">Languages</div>
<div class="tag-row">
  <span class="tag">Python</span><span class="tag">R</span><span class="tag">SQL</span>
  <span class="tag-plain">JavaScript</span><span class="tag-plain">Java</span>
</div>
<div class="skill-label">Statistics & Modeling</div>
<div class="tag-row">
  <span class="tag">Hypothesis Testing</span><span class="tag">Regression (Linear/Logistic)</span>
  <span class="tag">Predictive Modeling</span><span class="tag">Numerical Optimization</span>
  <span class="tag-plain">Time-Series Analysis</span><span class="tag-plain">Anomaly Detection</span>
  <span class="tag-plain">Collaborative Filtering</span>
</div>
<div class="skill-label">ML & AI</div>
<div class="tag-row">
  <span class="tag">Scikit-learn</span><span class="tag">Gradient Boosting</span>
  <span class="tag">Random Forest</span><span class="tag">SVM</span>
  <span class="tag">SVD / Matrix Factorization</span>
  <span class="tag-plain">LLMs</span><span class="tag-plain">RAG</span>
  <span class="tag-plain">GraphRAG</span><span class="tag-plain">LangChain</span><span class="tag-plain">Neo4j</span>
</div>
<div class="skill-label">Visualization & Reporting</div>
<div class="tag-row">
  <span class="tag">Tableau</span><span class="tag">Power BI</span>
  <span class="tag-plain">Matplotlib</span><span class="tag-plain">Seaborn</span>
  <span class="tag-plain">KPI Dashboards</span><span class="tag-plain">AWS QuickSight</span>
</div>
<div class="skill-label">Databases & Cloud</div>
<div class="tag-row">
  <span class="tag">PostgreSQL</span><span class="tag">MySQL</span>
  <span class="tag-plain">SQLite</span><span class="tag-plain">AWS DynamoDB</span>
  <span class="tag-plain">Docker</span><span class="tag-plain">FastAPI</span><span class="tag-plain">GitHub CI/CD</span>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── EXPERIENCE ────────────────────────────────────────────────
st.markdown('<div class="sec-label">Work History</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">Professional Experience</div>', unsafe_allow_html=True)
st.markdown('<hr class="sec-divider">', unsafe_allow_html=True)

st.markdown("""
<div class="exp-wrap">
  <div class="exp-role">AI Engineer – Knowledge Graphs & GraphRAG</div>
  <div class="exp-org">CareerGPT</div>
  <div class="exp-date">Jan 2026 – Present · Boston, MA</div>
  <div class="exp-bullet">Analyzed complex, high-dimensional user and career datasets in Python and SQL — applied EDA, hypothesis testing, and regression analysis to detect outliers, validate data integrity, and surface patterns driving AI recommendation quality across a live system serving thousands of users.</div>
  <div class="exp-bullet">Designed and evaluated data-driven KPI metrics and predictive scoring models to measure workflow performance; optimized end-to-end data pipelines reducing processing latency by 30% while maintaining full data accuracy across every release cycle.</div>
  <div class="exp-bullet">Generated and tested hypotheses on user engagement data, interpreted results, and delivered 3+ data-driven features improving platform recommendation accuracy through structured A/B evaluation and iterative feedback cycles.</div>
</div>

<div class="exp-wrap">
  <div class="exp-role">Research Assistant – Predictive Analytics Lab</div>
  <div class="exp-org">Dept. of Data Science, Mumbai University</div>
  <div class="exp-date">Jun 2023 – Apr 2024 · Mumbai, India</div>
  <div class="exp-bullet">Built automated SQL pipelines processing 50K+ user transactions and engineered user-item interaction matrices in Python — applied data cleaning, feature modeling, and matrix factorization to address data sparsity and scale recommendations to 10,000+ user ratings.</div>
  <div class="exp-bullet">Implemented and compared collaborative filtering with SVM and Random Forest models; applied t-tests, regression, and chi-square testing to evaluate performance — improving recommendation accuracy by 35% over traditional baseline models.</div>
  <div class="exp-bullet">Designed model evaluation dashboards in Tableau and Power BI; published findings as lead researcher in IJSREM (SJIF 8.659): Improving Book Recommendation Accuracy using Collaborative Filtering with SVM and Random Forest Models.</div>
</div>
""", unsafe_allow_html=True)

# ── PROJECTS ──────────────────────────────────────────────────
st.markdown('<div class="sec-label">Portfolio</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">Data Science Projects</div>', unsafe_allow_html=True)
st.markdown('<hr class="sec-divider">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="proj-card">
      <div class="proj-name">🏥 Clinical Readmission Risk Predictor</div>
      <div class="proj-desc">Predicts 30-day hospital readmissions from 5,000+ EHR records. Random Forest & Logistic Regression ensemble with chi-square and t-tests validating key risk factors. Tableau dashboard tracking rates by diagnosis, department, and insurance.</div>
      <div class="proj-metric">82% accuracy · 0.85 ROC-AUC</div>
      <div class="proj-tag-row">
        <span class="proj-tag">Python</span><span class="proj-tag">Scikit-learn</span>
        <span class="proj-tag">SQL</span><span class="proj-tag">Tableau</span><span class="proj-tag">SciPy</span>
      </div>
      <div class="proj-links">
        <a class="proj-link" href="https://github.com/nancytaswala23/readmission-risk-predictor" target="_blank">↗ GitHub</a>
        <a class="proj-link" href="https://readmission-risk-predictor-4epqhwnqmuitqogfbblwzi.streamlit.app/" target="_blank">▶ Live Demo</a>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="proj-card">
      <div class="proj-name">🤱 Maternal Health Outcomes</div>
      <div class="proj-desc">Gradient Boosting model predicting adverse maternal outcomes from 4,000 patient records. Chi-square confirms racial health disparities; t-tests validate enhanced prenatal care — aligned with MGB OB/GYN reproductive health research.</div>
      <div class="proj-metric">0.83 ROC-AUC · 5-fold CV · p &lt; 0.05</div>
      <div class="proj-tag-row">
        <span class="proj-tag">Python</span><span class="proj-tag">R</span>
        <span class="proj-tag">Gradient Boosting</span><span class="proj-tag">SciPy</span>
      </div>
      <div class="proj-links">
        <a class="proj-link" href="https://github.com/nancytaswala23/maternal-health-outcomes" target="_blank">↗ GitHub</a>
        <a class="proj-link" href="https://maternal-health-outcome-scsetxgtebwkszchmv8dqk.streamlit.app/" target="_blank">▶ Live Demo</a>
      </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="proj-card">
      <div class="proj-name">📊 Physician & Facility Performance Analytics</div>
      <div class="proj-desc">KPI framework tracking physician productivity, bottleneck detection, and processing delays across 5 facilities. SLSQP numerical optimization redistributes patient load. ANOVA and Pearson correlation validate findings.</div>
      <div class="proj-metric">40 physicians · 5 facilities · 52-week trends</div>
      <div class="proj-tag-row">
        <span class="proj-tag">Python</span><span class="proj-tag">SQL</span>
        <span class="proj-tag">SciPy Optimize</span><span class="proj-tag">Tableau</span>
      </div>
      <div class="proj-links">
        <a class="proj-link" href="https://github.com/nancytaswala23/physician-performance-analytics" target="_blank">↗ GitHub</a>
        <a class="proj-link" href="https://physician-performance-analytics-5hbj29twbyxdzuiynkwebg.streamlit.app/" target="_blank">▶ Live Demo</a>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="proj-card">
      <div class="proj-name">📚 BookShelf – Book Recommendation System</div>
      <div class="proj-desc">Published ML research implementing collaborative filtering with SVM and Random Forest on 50K+ user transactions. Applied t-tests, regression, and chi-square testing — improved recommendation accuracy by 35%.</div>
      <div class="proj-metric">Published · IJSREM · SJIF 8.659</div>
      <div class="proj-tag-row">
        <span class="proj-tag">Python</span><span class="proj-tag">Scikit-learn</span>
        <span class="proj-tag">SVM</span><span class="proj-tag">Random Forest</span><span class="proj-tag">SQL</span>
      </div>
      <div class="proj-links">
        <a class="proj-link" href="https://github.com/nancytaswala23/BookShelf---A-Book-Recommendation-System" target="_blank">↗ GitHub</a>
        <a class="proj-link" href="https://ijsrem.com/download/bookshelf-a-book-recommendation-system-using-collaborative-filtering/" target="_blank">↗ Paper</a>
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── PUBLICATION ───────────────────────────────────────────────
st.markdown('<div class="sec-label">Research</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">Publication</div>', unsafe_allow_html=True)
st.markdown('<hr class="sec-divider">', unsafe_allow_html=True)

st.markdown("""
<div class="pub-card">
  <div class="pub-title">Improving Book Recommendation Accuracy using Collaborative Filtering with SVM and Random Forest Models</div>
  <div class="pub-meta">International Journal of Scientific Research in Engineering and Management (IJSREM) · 2024 · Peer-Reviewed · SJIF Impact Factor 8.659<br>
  Collaborative Filtering · SVM · Random Forest · Matrix Factorization · RMSE · Precision@k · Recall@k · 50K+ user transactions</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── EDUCATION ─────────────────────────────────────────────────
st.markdown('<div class="sec-label">Academic Background</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">Education</div>', unsafe_allow_html=True)
st.markdown('<hr class="sec-divider">', unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    st.markdown("""
    <div class="edu-card">
      <div class="edu-degree">M.S. Information Systems</div>
      <div class="edu-school">Northeastern University</div>
      <div class="edu-dates">Aug 2024 – Dec 2026 · Boston, MA</div>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class="edu-card">
      <div class="edu-degree">B.S. Data Science</div>
      <div class="edu-school">Mumbai University</div>
      <div class="edu-dates">Aug 2021 – May 2024 · Mumbai, India</div>
      <div class="edu-dates" style="margin-top:6px;font-style:italic;color:#555">Research Assistant · Dept. of Data Science · Jun 2023 – Apr 2024</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── CONTACT ───────────────────────────────────────────────────
st.markdown('<div class="sec-label">Get In Touch</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">Contact</div>', unsafe_allow_html=True)
st.markdown('<hr class="sec-divider">', unsafe_allow_html=True)

st.markdown("""
<p style="font-size:0.9rem;color:#555;margin-bottom:1rem;max-width:500px">
M.S. candidate graduating December 2026, actively seeking full-time Data Scientist roles. Open to relocation. Particularly interested in clinical research and healthcare analytics environments.
</p>
""", unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    st.link_button("✉ taswala.n@northeastern.edu", "mailto:taswala.n@northeastern.edu", use_container_width=True)
    st.link_button("💼 LinkedIn", "https://linkedin.com/in/nancytaswala23", use_container_width=True)
with c2:
    st.link_button("🐙 GitHub", "https://github.com/nancytaswala23", use_container_width=True)
    st.link_button("🌐 Portfolio Website", "https://nancytaswala23.github.io", use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<p style="text-align:center;font-size:0.75rem;color:#aaa">© 2026 Nancy Taswala · Data Scientist · Boston, MA</p>', unsafe_allow_html=True)
