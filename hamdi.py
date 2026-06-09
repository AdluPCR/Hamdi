import streamlit as st

# Konfigurasi halaman utama web
st.set_page_config(page_title="Haikal Hamdi - Resume", page_icon="👨‍💻", layout="centered")

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["About Me", "Education & Family", "Experience", "Career Objective"])

# --- MENU 1: ABOUT ME ---
if menu == "About Me":
    st.title("👋 Welcome to My Profile")
    st.write("---")
    
    # Bagian Header Identitas
    st.header("Haikal Hamdi")
    st.subheader("Electronics System Engineering Student")
    
    # Detail Singkat
    st.markdown(
        """
        * **Date of Birth:** March 9, 2006
        * **Origin:** Pekanbaru, Riau, Indonesia
        * **Current Status:** Undergraduate Student at Politeknik Caltex Riau
        """
    )
    st.write(
        "I am an enthusiastic and detail-oriented Electronics System Engineering student "
        "with a passion for automation, embedded systems, and industrial technology. "
        "Born and raised in Pekanbaru, I am highly motivated to leverage my academic knowledge "
        "into real-world industrial applications."
    )

# --- MENU 2: EDUCATION & FAMILY ---
elif menu == "Education & Family":
    st.title("🎓 Education & 🏠 Family Background")
    st.write("---")
    
    st.subheader("Education")
    st.markdown(
        """
        **Politeknik Caltex Riau (PCR)**
        * *Major:* Electronics System Engineering (Teknologi Rekayasa Sistem Elektronika)
        * *Focus Areas:* Industrial Automation, Robotics, Microcontrollers, and Control Systems.
        """
    )
    
    st.write("---")
    
    st.subheader("Family Background")
    st.write(
        "I was raised in a supportive family environment in Pekanbaru. "
        "I am the **second of four siblings**, which has taught me both leadership "
        "and accountability from a young age."
    )

# --- MENU 3: EXPERIENCE (As a College Student) ---
elif menu == "Experience":
    st.title("💼 Projects & Organizational Experience")
    st.write("---")
    
    st.subheader("Academic Projects")
    st.markdown(
        """
        * **Automated Smart Home System (2025):** Designed and programmed an IoT-based home automation system using ESP32, MQTT protocol, and various sensors to optimize energy consumption.
        * **PLC-Based Miniature Conveyor Belt (2026):**
          Developed a ladder logic program for an industrial sorting mechanism using Omron PLC, simulating real-world factory automation.
        """
    )
    
    st.subheader("Organizational & Campus Activities")
    st.markdown(
        """
        * **Active Member - Student Electronics Club (Himpunan Mahasiswa):**
          Contributed to organizing technical workshops and mentoring freshmen in basic robotics and C++ programming.
        * **Participant - National Robotics Competition:**
          Represented the campus in a team-based line follower and automation challenge.
        """
    )

# --- MENU 4: CAREER OBJECTIVE (Target: PT Pertamina) ---
elif menu == "Career Objective":
    st.title("🎯 Career Objective")
    st.write("---")
    
    st.subheader("Target Company: PT Pertamina (Persero)")
    st.write(
        "My ultimate career goal is to join **PT Pertamina**, Indonesia's leading state-owned energy enterprise, "
        "specifically within the instrumentation, control systems, or automation division."
    )
    
    st.markdown(
        """
        ### Why PT Pertamina?
        As an Electronics System Engineering student, I understand that high efficiency, safety, and reliability "
        are critical in the oil, gas, and renewable energy sectors. PT Pertamina provides the perfect arena "
        to implement advanced automation and control technologies.
        
        ### What I Bring to the Table:
        * **Technical Synergy:** My background in *Teknologi Rekayasa Sistem Elektronika* aligns perfectly with Pertamina's continuous modernization of refinery and distribution controls (PLC, SCADA, and DCS systems).
        * **Local Dedication:** Being from Riau—one of Indonesia's most strategic energy hubs—I have a strong personal and professional motivation to contribute directly to the nation's energy security through Pertamina's operations in this region.
        """
    )
    
    st.info("💡 *Ready to innovate, automate, and energize the nation.*")