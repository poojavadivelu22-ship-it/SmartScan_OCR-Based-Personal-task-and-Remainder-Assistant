import streamlit as st
from ocr import extract_text
from database import add_task, get_tasks, update_task_status, delete_task
from datetime import date, time

st.set_page_config(
    page_title="SmartScan",
    page_icon="",
    layout="centered"
)

st.title(" SmartScan")
st.subheader("OCR-Based Task and Reminder Assistant")

st.write("Upload an image and convert the text into a task.")


# -------------------------------
# IMAGE UPLOAD
# -------------------------------

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

extracted_text = ""

if uploaded_file is not None:

    st.image(
        uploaded_file,
        caption="Uploaded Image",
        use_container_width=True
    )

    if st.button(" Extract Text"):

        extracted_text = extract_text(uploaded_file)

        st.session_state["extracted_text"] = extracted_text

        if extracted_text.strip():
            st.success("Text extracted successfully!")
        else:
            st.warning("No text detected.")


# -------------------------------
# SHOW EXTRACTED TEXT
# -------------------------------

if "extracted_text" in st.session_state:

    st.subheader(" Extracted Text")

    st.text_area(
        "OCR Result",
        st.session_state["extracted_text"],
        height=150
    )


# -------------------------------
# CREATE TASK
# -------------------------------

st.divider()

st.subheader(" Create Task")

task_name = st.text_input(
    "Task Name",
    value=st.session_state.get("extracted_text", "").strip()
)

task_date = st.date_input(
    "Task Date",
    min_value=date.today()
)

task_time = st.time_input(
    "Reminder Time",
    value=time(9, 0)
)


if st.button(" Add Task"):

    if task_name.strip() == "":
        st.error("Please enter a task.")

    else:

        add_task(
            task_name,
            str(task_date),
            str(task_time)
        )

        st.success("Task added successfully!")


# -------------------------------
# DISPLAY TASKS
# -------------------------------

st.divider()

st.subheader(" My Tasks")

tasks = get_tasks()

if not tasks:

    st.info("No tasks available.")

else:

    for task in tasks:

        task_id = task[0]
        task_name = task[1]
        task_date = task[2]
        task_time = task[3]
        status = task[4]

        st.write(f"###  {task_name}")

        st.write(f"Date: {task_date}")
        st.write(f" Time: {task_time}")
        st.write(f"Status: **{status}**")

        col1, col2 = st.columns(2)

        with col1:

            if status == "Pending":

                if st.button(
                    " Complete",
                    key=f"complete_{task_id}"
                ):

                    update_task_status(task_id)

                    st.rerun()

        with col2:

            if st.button(
                " Delete",
                key=f"delete_{task_id}"
            ):

                delete_task(task_id)

                st.rerun()

        st.divider()