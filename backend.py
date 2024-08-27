import streamlit as st
import sqlite3
import pandas as pd
import io

# Function to create a database connection
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        st.error(f"Error creating connection to database: {e}")
    return conn

# Function to create the students table
def create_table(conn):
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS students (
        batch_code TEXT,
        alias TEXT,
        course_name TEXT,
        start_date TEXT,
        end_date TEXT,
        member_code TEXT,
        name TEXT,
        dob TEXT,
        Age INTEGER,
        gender TEXT,
        mobile_no TEXT,
        center TEXT,
        district TEXT,
        state TEXT,
        family_monthly_earning INTEGER,
        education TEXT,
        final_exam_marks INTEGER,
        trained_status TEXT,
        placement_status TEXT,
        funder_name TEXT,
        status TEXT,
        program_name TEXT,
        reason_for_rejection TEXT,
        placement_remarks TEXT,
        verification_done TEXT,
        m_e_verified_class_start TEXT,
        m_e_verified_remarks TEXT,
        file_verification_status TEXT,
        concatenate TEXT,
        download_from_cmis TEXT,
        fy_year TEXT,
        m_e_verified_students INTEGER,
        not_interested_in_job TEXT,
        working_before_batch_joining TEXT,
        non_anudip_student_others TEXT
    );
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        st.error(f"Error creating table: {e}")

# Function to upload data from the Excel file to SQLite
def upload_data(conn, df):
    try:
        df.to_sql('students', conn, if_exists='append', index=False)
        st.success("Data uploaded successfully!")
    except sqlite3.Error as e:
        st.error(f"Error uploading data: {e}")

# Streamlit application
def main():
    st.title("Upload Data to SQLite Database")

    # Step 1: File upload
    uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])
    
    if uploaded_file is not None:
        # Step 2: Read the uploaded file into a DataFrame
        df = pd.read_excel(uploaded_file)
        
        st.write("Preview of Uploaded Data:")
        st.dataframe(df)

        # Step 3: Create the SQLite database and table
        database = "students.db"
        conn = create_connection(database)

        if conn is not None:
            create_table(conn)
            
            # Step 4: Upload the DataFrame to the SQLite database
            if st.button("Upload Data to Database"):
                upload_data(conn, df)
                
            conn.close()
        else:
            st.error("Cannot create database connection.")
    
if __name__ == '__main__':
    main()
