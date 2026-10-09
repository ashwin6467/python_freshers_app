import io
import traceback
from contextlib import redirect_stdout
from datetime import datetime

import streamlit as st

from db import (
    init_db,
    create_user,
    verify_user,
    mark_lesson_complete,
    get_completed_lessons,
    get_completion_percent,
    save_quiz_attempt,
    submit_project,
    get_all_project_submissions,
    get_all_quiz_attempts,
    get_user_progress_summary,
    get_all_users,
    get_announcements,
)
from lessons import LESSONS, QUIZ_BANK, PROJECT_IDEAS

st.set_page_config(
    page_title="Python Freshers Academy",
    page_icon="🐍",
    layout="wide",
)

init_db()

st.markdown(
    """
<style>
    .main {
        background: #0f172a;
    }
    .stApp {
        background: linear-gradient(135deg, #0f172a, #111827);
    }
    .card {
        background: #1f2937;
        border: 1px solid #374151;
        border-radius: 14px;
        padding: 1rem 1.2rem;
        margin-bottom: 1rem;
    }
    .info-box {
        background: #172554;
        border: 1px solid #2563eb;
        border-radius: 12px;
        padding: 0.8rem 1rem;
        color: #dbeafe;
    }
    .success-box {
        background: #052e16;
        border: 1px solid #166534;
        border-radius: 12px;
        padding: 0.8rem 1rem;
        color: #dcfce7;
    }
    .warning-box {
        background: #451a03;
        border: 1px solid #b45309;
        border-radius: 12px;
        padding: 0.8rem 1rem;
        color: #fef3c7;
    }
    h1, h2, h3, h4 {
        color: #f8fafc;
    }
    p, div, li {
        color: #e5e7eb;
    }
</style>
""",
    unsafe_allow_html=True,
)

if "user" not in st.session_state:
    st.session_state.user = None


def render_lesson(lesson, user_id):
    st.title(lesson["title"])
    st.caption(f"Level: {lesson['level']}")
    st.markdown(f"### Objective\n{lesson['objective']}")
    st.markdown("### Concept")
    st.write(lesson["concept"])
    st.markdown("### Example")
    st.code(lesson["example"], language="python")
    st.markdown("### Explanation")
    st.write(lesson["explanation"])
    st.markdown("### Practice Exercise")
    st.info(lesson["exercise"])

    completed = lesson["id"] in get_completed_lessons(user_id)
    if completed:
        st.success("Lesson completed.")
    else:
        if st.button("Mark as completed"):
            mark_lesson_complete(user_id, lesson["id"])
            st.success("Lesson marked complete.")
            st.rerun()


def auth_page():
    st.title("🐍 Python Freshers Academy")
    st.subheader("Login or create an account")

    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")
        if st.button("Login"):
            user = verify_user(username, password)
            if user:
                st.session_state.user = user
                st.success("Login successful.")
                st.rerun()
            else:
                st.error("Invalid username or password.")

    with tab2:
        new_username = st.text_input("Choose username", key="register_username")
        new_password = st.text_input("Choose password", type="password", key="register_password")
        if st.button("Create Account"):
            created = create_user(new_username, new_password)
            if created:
                st.success("Account created successfully. Please login.")
            else:
                st.error("Username already exists or fields are empty.")


def admin_dashboard():
    user = st.session_state.user
    if user["role"] != "admin":
        st.warning("You do not have admin access.")
        return

    st.title("Admin Dashboard")

    users = get_all_users()
    progress_summary = get_user_progress_summary()
    project_submissions = get_all_project_submissions()
    quiz_attempts = get_all_quiz_attempts()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Users", len(users))
    with col2:
        st.metric("Project Submissions", len(project_submissions))
    with col3:
        st.metric("Quiz Attempts", len(quiz_attempts))

    st.subheader("User Progress")
    for row in progress_summary:
        username = row["username"]
        completed_count = row["completed_count"] or 0
        pct = round((completed_count / len(LESSONS)) * 100, 1)
        st.progress(min(pct / 100, 1.0))
        st.write(f"{username}: {completed_count}/{len(LESSONS)} ({pct}%)")

    st.subheader("Project Submissions")
    if project_submissions:
        for item in project_submissions[:10]:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.write(f"**User:** {item['username']}")
            st.write(f"**Project:** {item['project_name']}")
            st.write(f"**Description:** {item['description']}")
            st.write(f"**Submitted:** {item['created_at']}")
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("No project submissions yet.")

    st.subheader("Quiz Attempts")
    if quiz_attempts:
        for item in quiz_attempts[:10]:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.write(f"**User:** {item['username']}")
            st.write(f"**Topic:** {item['topic']}")
            st.write(f"**Score:** {item['score']}/{item['total']}")
            st.write(f"**Attempted At:** {item['attempted_at']}")
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("No quiz attempts yet.")


def main_app():
    user = st.session_state.user
    user_id = user["id"]
    username = user["username"]
    role = user["role"]
    progress_pct = get_completion_percent(user_id, len(LESSONS))
    completed = get_completed_lessons(user_id)

    st.sidebar.title(f"Welcome, {username}")
    st.sidebar.write(f"Role: {role}")

    nav = st.sidebar.radio(
        "Navigation",
        ["Dashboard", "Roadmap", "Lessons", "Code Playground", "Quiz", "Projects", "Certificate", "Admin"],
    )

    if st.sidebar.button("Logout"):
        st.session_state.user = None
        st.rerun()

    if nav == "Dashboard":
        st.title("Dashboard")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Lessons", len(LESSONS))
        with col2:
            st.metric("Completed", len(completed))
        with col3:
            st.metric("Progress", f"{progress_pct}%")

        st.subheader("Announcements")
        announcements = get_announcements(5)
        if announcements:
            for message, created_at in announcements:
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.write(message)
                st.caption(created_at)
                st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.info("No announcements yet.")

    elif nav == "Roadmap":
        st.title("Learning Roadmap")
        st.progress(progress_pct / 100)
        st.write(f"Overall progress: {progress_pct}%")

        for lesson in LESSONS:
            lesson_id = lesson["id"]
            status = "✅ Completed" if lesson_id in completed else "⏳ Not completed"
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown(f"### {lesson['title']}")
            st.write(f"**Goal:** {lesson['objective']}")
            st.write(f"**Status:** {status}")
            st.markdown("</div>", unsafe_allow_html=True)

    elif nav == "Lessons":
        st.title("Python Lessons")
        selected_id = st.selectbox("Choose a lesson", [lesson["id"] for lesson in LESSONS], index=0)
        selected_lesson = next(lesson for lesson in LESSONS if lesson["id"] == selected_id)
        render_lesson(selected_lesson, user_id)

    elif nav == "Code Playground":
        st.title("Code Playground")
        default_code = '''
name = "Priya"
age = 21
print("Hello,", name)
print("Age:", age)
'''
        code = st.text_area("Write Python code here", value=default_code, height=260)

        if st.button("Run Code"):
            try:
                output = io.StringIO()
                with redirect_stdout(output):
                    exec(code, {})
                result = output.getvalue()
                if result.strip():
                    st.code(result, language="python")
                else:
                    st.info("Code executed successfully but produced no output.")
            except Exception:
                st.error("There is an error in your code.")
                st.code(traceback.format_exc(), language="python")

        st.markdown(
            """
        Suggested examples:
        - print("Hello, World!")
        - for i in range(1, 6): print(i)
        - numbers = [1, 2, 3]; print(sum(numbers))
        """
        )

    elif nav == "Quiz":
        st.title("Quiz")
        topic = st.selectbox("Choose topic", list(QUIZ_BANK.keys()))
        questions = QUIZ_BANK[topic]

        answers = {}
        for idx, q in enumerate(questions, start=1):
            st.markdown(f"### Q{idx}. {q['question']}")
            answers[idx] = st.radio("Choose one", q["options"], key=f"{topic}_{idx}", horizontal=False)

        if st.button("Submit Quiz"):
            score = 0
            total = len(questions)
            for idx, q in enumerate(questions, start=1):
                if answers.get(idx) == q["answer"]:
                    score += 1

            percentage = round((score / total) * 100, 1)
            save_quiz_attempt(user_id, topic, score, total)

            st.success(f"Your score: {score}/{total} ({percentage}%)")

            if percentage >= 70:
                st.balloons()
                st.write("Excellent! You understand the topic well.")
            elif percentage >= 50:
                st.write("Good effort. Review the lesson and try again.")
            else:
                st.write("Keep practicing. You can do it.")

    elif nav == "Projects":
        st.title("Mini Project Ideas")
        for project in PROJECT_IDEAS:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown(f"### {project}")
            st.write("Try building this project after completing the basics.")
            st.markdown("</div>", unsafe_allow_html=True)

        st.subheader("Submit a Project Idea")
        project_name = st.text_input("Project Name")
        project_description = st.text_area("Describe the idea")

        if st.button("Submit Idea"):
            if project_name and project_description:
                submit_project(user_id, project_name, project_description)
                st.success("Project idea submitted successfully.")
            else:
                st.warning("Please enter both the project name and description.")

    elif nav == "Certificate":
        st.title("Certificate")
        if progress_pct >= 70:
            cert_name = st.text_input("Enter your name", value=username)
            if st.button("Generate Certificate"):
                st.markdown(
                    f"""
                    <div style="
                        background: #f8fafc;
                        color: #0f172a;
                        border: 3px solid #f59e0b;
                        border-radius: 18px;
                        padding: 2rem;
                        text-align: center;
                    ">
                        <h1>Certificate of Completion</h1>
                        <p>This certificate is proudly awarded to</p>
                        <h2 style='color:#1d4ed8;'>{cert_name}</h2>
                        <p>for successfully completing the Python Freshers Learning Program.</p>
                        <p><strong>Progress:</strong> {progress_pct}%</p>
                        <p>Issued on: {datetime.now().strftime('%Y-%m-%d')}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        else:
            st.warning("You need at least 70% completion to generate the certificate.")

    elif nav == "Admin":
        admin_dashboard()


if st.session_state.user is None:
    auth_page()
else:
    main_app()
