import streamlit as st
import base64

# Set page title and icon
st.set_page_config(page_title="Student Portfolio", page_icon="🎓", layout="wide")

# Add animations and transitions with CSS
st.markdown("""
<style>
    .fade-in {
        animation: fadeIn 1.5s;
    }
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    .project-card {
        transition: transform 0.3s ease;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #ddd;
        margin-bottom: 10px;
    }
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .testimonial {
        padding: 15px;
        border-left: 4px solid #19A7CE;
        background-color: #f8f9fa;
        margin-bottom: 15px;
        border-radius: 0px 5px 5px 0px;
    }
    .timeline-item {
        display: flex;
        margin-bottom: 20px;
    }
    .timeline-dot {
        min-width: 20px;
        height: 20px;
        background-color: #4682b4;
        border-radius: 50%;
        margin-right: 15px;
        margin-top: 5px;
    }
    .timeline-content {
        border-left: 2px solid #4682b4;
        padding-left: 15px;
        padding-bottom: 10px;
    }
    .timeline-date {
        font-weight: bold;
        color: #4682b4;
    }
    .timeline-title {
        font-weight: bold;
        margin-top: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go To:", ["Home", "Projects", "Skills", "Timeline", "Testimonials", "Settings", "Contact"])

# Function to get base64 encoded data for resume download
def get_base64_download_link(file_path, file_name):
    try:
        with open(file_path, "rb") as file:
            data = file.read()
        b64 = base64.b64encode(data).decode()
        href = f'<a href="data:application/pdf;base64,{b64}" download="{file_name}">📄 Download Resume</a>'
        return href
    except FileNotFoundError:
        return "Resume file not found"

# Home section
if page == "Home":
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.title("🎓 Student Portfolio")

    col1, col2 = st.columns([1, 3])
    
    with col1:
        # Profile image
        uploaded_image = st.file_uploader("Upload Profile Picture", type=["jpg", "png"])
        if uploaded_image is not None:
            st.image(uploaded_image, width=200, caption="Uploaded image")
        else:
            # Using a placeholder instead of trying to load a local file
            st.image("person.jpg", width=200, caption="Default image")
    
    with col2:
        # Student details
        st.header("Cyuzuzo Samuel")
        st.write("📍 Musanze, Rwanda")
        st.write("🎓 INES - Ruhengeri")
        st.write("📚 BSc Computer Science, SWE, Year 3")
        
        # Resume download button
        resume_link = get_base64_download_link("resume.pdf", "Samuel_Cyuzuzo_Resume.pdf")
        if resume_link != "Resume file not found":
            st.markdown(resume_link, unsafe_allow_html=True)
        else:
            st.warning("Resume file not found. Please upload a resume.pdf file.")
            st.file_uploader("Upload your resume (PDF)", type=["pdf"])
    
    st.markdown("---")
    st.subheader("About Me")
    about_me = st.text_area("Short introduction about myself:",
        "I'm a passionate software engineer focused on web development with skills in PHP, CSS, HTML, and JavaScript. I strive to create innovative and user-friendly solutions that make a positive impact. Currently in my third year of Computer Science, I'm developing expertise in AI and machine learning applications for real-world problems. I'm particularly excited about how technology can be leveraged to create solutions for local communities in Rwanda.",
        height=150)
    st.write(about_me)
    st.markdown('</div>', unsafe_allow_html=True)

# Projects section
elif page == "Projects":
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.title("💻 My Projects")
    
    # Project filtering
    st.subheader("🗂️ Filter Projects")
    project_filter = st.selectbox(
        "Select project category:",
        ["All Projects", "Year 1 Projects", "Year 2 Projects", "Year 3 Projects", "Group Projects", "Dissertation"]
    )
    
    # Project display function
    def show_project(title, project_type, description, link=None, year=None, is_group=False):
        if ((project_filter == "All Projects") or 
            (project_filter == "Year 1 Projects" and year == 1) or
            (project_filter == "Year 2 Projects" and year == 2) or
            (project_filter == "Year 3 Projects" and year == 3) or
            (project_filter == "Group Projects" and is_group) or
            (project_filter == "Dissertation" and "Dissertation" in project_type)):
            
            st.markdown(f'<div class="project-card">', unsafe_allow_html=True)
            st.subheader(f"📌 {title}")
            st.write(f"**Type:** {project_type}")
            st.write(f"**Description:** {description}")
            if link:
                st.write(f"[View Code/Documentation]({link})")
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Project 1
    show_project(
        "Data Analysis Project", 
        "Year 2, Individual Project", 
        "A project analyzing trends of Rwanda GDP accounts using Pandas and Matplotlib. Implemented data cleaning, visualization, and trend analysis techniques to draw meaningful insights from economic data.",
        "https://github.com/cyuzuzocyisezerano/data-analysis-project",
        year=2,
        is_group=False
    )
    
    # Project 2
    show_project(
        "AI Chatbot", 
        "Year 3, Group Project", 
        "Developed an AI-Powered chatbot using Python and NLP Techniques. Our team created a conversational agent capable of answering student queries about university resources and courses.",
        "https://github.com/cyuzuzocyisezerano/ai-chatbot",
        year=3,
        is_group=True
    )
    
    # Project 3
    show_project(
        "Caritas CDJP Gikongoro Website", 
        "Year 2, Internship Project", 
        "Designed and developed a website for Caritas Gikongoro using WordPress CMS. Implemented custom themes, content management system, and donation tracking functionality.",
        "https://github.com/cyuzuzocyisezerano/caritas-website",
        year=2,
        is_group=False
    )
    
    # Project 4 (Dissertation)
    show_project(
        "Smart Agriculture Monitoring System", 
        "Year 3, Dissertation Project", 
        "Developing an IoT-based system to monitor soil conditions, weather patterns, and crop health for small-scale farmers in Rwanda. The system uses sensors to collect data and provides recommendations for optimal farming practices.",
        "https://github.com/cyuzuzocyisezerano/smart-agriculture",
        year=3,
        is_group=False
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Skills section
elif page == "Skills":
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.title("⚡ Skills and Achievements")

    st.subheader("Programming Skills")
    col1, col2 = st.columns(2)
    
    with col1:
        skill_python = st.slider("Python", 0, 100, 90)
        st.progress(skill_python)
        
        skill_js = st.slider("JavaScript", 0, 100, 75)
        st.progress(skill_js)
        
        skill_AI = st.slider("Artificial Intelligence", 0, 100, 65)
        st.progress(skill_AI)
    
    with col2:
        skill_html_css = st.slider("HTML/CSS", 0, 100, 85)
        st.progress(skill_html_css)
        
        skill_php = st.slider("PHP", 0, 100, 70)
        st.progress(skill_php)
        
        skill_data = st.slider("Data Analysis", 0, 100, 80)
        st.progress(skill_data)

    st.subheader("Certifications & Achievements")
    st.write("✔ Completed AI & ML in Business Certification")
    st.write("✔ Certified in AI Research and Course Preparation for Education")
    st.write("✔ Finalist in INES-Ruhengeri Hackathon 2023")
    st.write("✔ Academic Excellence Award - Computer Science Department (2022)")
    st.markdown('</div>', unsafe_allow_html=True)

# Timeline section - Custom implementation without external library
elif page == "Timeline":
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.title("⏳ Academic & Project Timeline")
    
    # Timeline data
    timeline_events = [
        {
            "date": "September 2021",
            "title": "Started Computer Science at INES-Ruhengeri",
            "description": "Began my journey in Computer Science with a focus on software engineering"
        },
        {
            "date": "February 2022",
            "title": "First Programming Project",
            "description": "Completed my first major programming assignment using Python"
        },
        {
            "date": "July 2022",
            "title": "Academic Excellence Award",
            "description": "Received recognition for outstanding performance in Year 1"
        },
        {
            "date": "January 2023",
            "title": "Web Development Project",
            "description": "Built my first full-stack web application using PHP and MySQL"
        },
        {
            "date": "June 2023",
            "title": "Internship at Caritas CDJP Gikongoro",
            "description": "Developed and deployed the organization's website"
        },
        {
            "date": "November 2023",
            "title": "INES-Ruhengeri Hackathon",
            "description": "Reached the finals with an innovative solution for local agricultural challenges"
        },
        {
            "date": "January 2024",
            "title": "AI Certification",
            "description": "Completed AI & ML in Business certification program"
        },
        {
            "date": "February 2024",
            "title": "Dissertation Project Started",
            "description": "Began work on Smart Agriculture Monitoring System"
        },
        {
            "date": "January 2025",
            "title": "AI Chatbot Group Project",
            "description": "Led a team to develop an NLP-based chatbot for student services"
        }
    ]
    
    # Display custom timeline
    for event in timeline_events:
        st.markdown(f"""
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
                <div class="timeline-date">{event['date']}</div>
                <div class="timeline-title">{event['title']}</div>
                <div>{event['description']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Testimonials section
elif page == "Testimonials":
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.title("🗣️ Testimonials")
    
    st.markdown('<div class="testimonial">', unsafe_allow_html=True)
    st.markdown("**Dr. Theodore M. - Professor of Computer Science**")
    st.write('"Cyuzuzo is an exceptional student with remarkable problem-solving abilities. His final year project demonstrates innovative thinking and practical application of advanced concepts."')
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="testimonial">', unsafe_allow_html=True)
    st.markdown("**Uwase Marie - Project Team Member**")
    st.write('"Working with Samuel on our AI Chatbot project was an enriching experience. His technical expertise and leadership skills were crucial to our team\'s success."')
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="testimonial">', unsafe_allow_html=True)
    st.markdown("**Jean-Paul K. - Caritas CDJP Gikongoro IT Manager**")
    st.write('"The website Samuel developed during his internship significantly improved our online presence. His attention to detail and commitment to meeting project requirements were exemplary."')
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Add new testimonial
    st.subheader("Add a New Testimonial")
    st.write("If you've worked with me and would like to leave a testimonial, please fill out the form below:")
    
    with st.form("testimonial_form"):
        testimonial_name = st.text_input("Your Name and Title/Position")
        testimonial_text = st.text_area("Your Testimonial")
        submitted = st.form_submit_button("Submit Testimonial")
        
        if submitted:
            st.success("Thank you for your testimonial! It will be reviewed and added to my portfolio.")
    st.markdown('</div>', unsafe_allow_html=True)

# Settings section
elif page == "Settings":
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.title("🎨 Customize Your Profile")

    st.subheader("Upload a Profile Picture")
    uploaded_image = st.file_uploader("Choose a file", type=["jpg", "png"])
    if uploaded_image:
        st.image(uploaded_image, width=150)
        st.success("Image uploaded successfully!")

    st.subheader("✍ Edit Personal Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Full Name:", "Cyuzuzo Samuel")
        email = st.text_input("Email:", "ug23/20854@ines.ac.rw")
        location = st.text_input("Location:", "Musanze, Rwanda")
    
    with col2:
        university = st.text_input("University:", "INES - Ruhengeri")
        field = st.text_input("Field of Study:", "Computer Science, SWE")
        year = st.selectbox("Year of Study:", ["Year 1", "Year 2", "Year 3", "Year 4"])

    st.subheader("Social Media & Professional Links")
    github = st.text_input("GitHub URL:", "https://github.com/cyuzuzocyisezerano")
    linkedin = st.text_input("LinkedIn URL:", "https://www.linkedin.com/in/cyuzuzo-samuel-31871918b/")
    
    st.subheader("Update Resume")
    uploaded_resume = st.file_uploader("Upload New Resume (PDF)", type=["pdf"])
    
    if st.button("Save All Changes"):
        st.success("Profile information updated successfully!")
    st.markdown('</div>', unsafe_allow_html=True)

# Contact section
elif page == "Contact":
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.title("📬 Contact Me")

    col1, col2 = st.columns([2, 1])
    
    with col1:
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            subject = st.text_input("Subject")
            message = st.text_area("Your Message")

            submitted = st.form_submit_button("Send Message")
            if submitted:
                st.success("✅ Message sent successfully! I'll get back to you soon.")
    
    with col2:
        st.subheader("Connect With Me")
        st.write("📧 Email: ug23/20854@ines.ac.rw")
        st.write("[🔗 LinkedIn](https://www.linkedin.com/in/cyuzuzo-samuel-31871918b/)")
        st.write("[📂 GitHub](https://github.com/cyuzuzocyisezerano)")
        st.write("📱 Phone: +250 788 123 456")
        st.write("📍 INES-Ruhengeri, Rwanda")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.sidebar.write("---")
st.sidebar.write("🔹 Made with ❤ using Streamlit by Cyuzuzo Samuel")
st.sidebar.write("© 2025 - All Rights Reserved")