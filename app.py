import streamlit as st
import pandas as pd
import sqlite3
from backend import create_connection, create_table

# Function to fetch data from the database
def fetch_data(conn):
    try:
        query = "SELECT * FROM students"
        df = pd.read_sql(query, conn)
        return df
    except sqlite3.Error as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame()

# Metric box function
def metric_box(label, value, color, width="100%"):
    st.markdown(f"""
    <div style="background-color: {color}; padding: 3px; border-radius: 5px; text-align: center; width: {width};">
        <h5 style="color: white; margin: 0; font-size: 8px;">{label}</h5>
        <h3 style="color: white; margin: 0; font-size: 16px;">{value}</h3>
    </div>
    """, unsafe_allow_html=True)

# Main Streamlit application
def main():
    st.title("Dashboard with SQLite Database")

    # Database file path
    database = "students.db"
    conn = create_connection(database)

    if conn is not None:
        try:
            # Create the students table if it doesn't exist
            create_table(conn)
        except sqlite3.Error as e:
            st.error(f"Error creating table: {e}")

        # Fetch data from SQLite database for dashboard
        df = fetch_data(conn)

        if not df.empty:
            st.title('')

            col1, col2, col3, col4 = st.columns(4)

            with col4:
                years = df['fy_year'].dropna().unique()
                fy_years = st.multiselect("FY-Year", [""] + sorted(years))

            filtered_df = df[df['fy_year'].isin(fy_years)] if fy_years else df

            with col1:
                funder_names = st.multiselect("Funder Name", [""] + sorted(filtered_df['funder_name'].dropna().unique()))

            with col2:
                filtered_df_center = filtered_df[filtered_df['funder_name'].isin(funder_names)] if funder_names else filtered_df
                centers = filtered_df_center['center'].dropna().unique()
                selected_centers = st.multiselect("Center", [""] + sorted(centers))

            with col3:
                filtered_df_program = filtered_df_center[filtered_df_center['center'].isin(selected_centers)] if selected_centers else filtered_df_center
                programs = filtered_df_program['program_name'].dropna().unique()
                selected_programs = st.multiselect("Program Name", [""] + sorted(programs))

            filtered_df = filtered_df_program[filtered_df_program['program_name'].isin(selected_programs)] if selected_programs else filtered_df_program

            if not filtered_df.empty:
                st.write("")

                # Metrics Section
                col1, col2, col3, col4, col5, col6 = st.columns(6)

                with col1:
                    total_ids = filtered_df['download_from_cmis'].count()
                    metric_box("Total Data", total_ids, "#007B7F")

                with col2:
                    total_verification = filtered_df['verification_done'].count()
                    metric_box("Verification Done", total_verification, "#007B7F")

                with col3:
                    contactable_df = filtered_df[filtered_df['verification_done'].str.strip().str.lower() == 'yes']
                    contact = contactable_df['verification_done'].count()
                    metric_box("Contactable", contact, "#007B7F")

                with col4:
                    ae_verified = filtered_df[filtered_df['m_e_verified_remarks'].str.strip().str.lower() == 'verified by a&e team']
                    aeve = ae_verified['m_e_verified_remarks'].count()
                    metric_box("Verified By A&E", aeve, "#007B7F")

                with col5:
                    not_con = filtered_df[filtered_df['verification_done'].str.strip().str.lower() == 'no']
                    not_conta = not_con['verification_done'].count()
                    metric_box("Not Contactable", not_conta, "#007B7F")

                with col6:
                    total_verification_done = filtered_df['verification_done'].count()
                    total_verification_done_yes = filtered_df[filtered_df['verification_done'].str.strip().str.lower() == 'yes']['verification_done'].count()
                    contactable_percentage = (total_verification_done_yes / total_verification_done) * 100 if total_verification_done > 0 else 0
                    metric_box("Total Contactable %", f"{contactable_percentage:.2f}%", "#007B7F")

                st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

                col1, col2, col3, col4, col5, col6 = st.columns(6)

                with col1:
                    me_verified = filtered_df[filtered_df['m_e_verified_students'].str.strip().str.lower() == 'yes']
                    me_verified_s = me_verified['m_e_verified_students'].count()
                    metric_box("M&E Verified Enroll", me_verified_s, "#007B7F")

                with col2:
                    trained_a = filtered_df[filtered_df['trained_status'].str.strip().str.lower() == 'passed']
                    me_trained = trained_a['trained_status'].count()
                    metric_box("Total Trained", me_trained, "#007B7F")

                with col3:
                    left_the_c = filtered_df[filtered_df['m_e_verified_remarks'].str.strip().str.lower() == 'left the course']
                    cour_le = left_the_c['m_e_verified_remarks'].count()
                    metric_box("Left The Course", cour_le, "#007B7F")

                with col4:
                    inter_in_job = filtered_df[filtered_df['not_interested_in_job'].str.strip().str.lower() == 'yes']
                    job = inter_in_job['not_interested_in_job'].count()
                    metric_box("Not-Interest In Job", job, "#007B7F")

                with col5:
                    work = filtered_df[filtered_df['working_before_batch_joining'].str.strip().str.lower() == 'yes']
                    before_w = work['working_before_batch_joining'].count()
                    metric_box("Working Before", before_w, "#007B7F")

                with col6:
                    not_s = filtered_df[filtered_df['non_anudip_student_others'].str.strip().str.lower() == 'yes']
                    students_n = not_s['non_anudip_student_others'].count()
                    metric_box("Non-Anudip,Others", students_n, "#007B7F")

                st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

                col1, col2, col3, col4, col5, col6 = st.columns(6)

                with col1:
                    verifi = filtered_df[filtered_df['placement_remarks'].str.strip().str.lower() != ' ']
                    plac_veri = verifi['placement_remarks'].count()
                    metric_box("Placement Verified Done", plac_veri, "#034a7e")

                with col2:
                    verifi = filtered_df[filtered_df['placement_remarks'].str.strip().str.lower() != 'unable_to_track']
                    plac_veri = verifi['placement_remarks'].count()
                    metric_box("Total Contactable-(Plac)", plac_veri, "#034a7e")

                with col3:
                    verifi = filtered_df[filtered_df['placement_remarks'].str.strip().str.lower() == 'unable_to_track']
                    plac_veri = verifi['placement_remarks'].count()
                    metric_box("Total Not Contactable", plac_veri, "#034a7e")

                with col4:
                    verifi = filtered_df[filtered_df['placement_remarks'].str.strip().str.lower() == 'not_working_at_all']
                    plac_veri = verifi['placement_remarks'].count()
                    metric_box("Not working at all(Over Contactable)", plac_veri, "#034a7e")

                with col5:
                    verifi = filtered_df[filtered_df['placement_status'].str.strip().str.lower() == 'yes']
                    plac_veri = verifi['placement_status'].count()
                    metric_box("Total M&E Verified Placed", plac_veri, "#034a7e")

                with col6:
                    total_verification_done = filtered_df['placement_status'].count()
                    total_verification_done_yes = filtered_df[filtered_df['placement_status'].str.strip().str.lower() == 'yes']['placement_status'].count()
                    contactable_percentage = (total_verification_done_yes / total_verification_done) * 100 if total_verification_done > 0 else 0
                    metric_box("Total Verified Placement %", f"{contactable_percentage:.2f}%", "#034a7e")

                st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

                # Create a datagram table
                metrics_df = filtered_df.groupby('funder_name').agg(
                    Total_Data=('download_from_cmis', 'count'),
                    M_E_Verified_Enrollment=('m_e_verified_students', lambda x: (x.str.strip().str.lower() == 'yes').sum()),
                    Total_Trained=('trained_status', lambda x: (x.str.strip().str.lower() == 'passed').sum()),
                    M_E_Verified_Placed=('placement_status', lambda x: (x.str.strip().str.lower() == 'yes').sum())
                ).reset_index()

                metrics_df['Enrollment_%'] = (metrics_df['M_E_Verified_Enrollment'] / metrics_df['Total_Data']) * 100
                metrics_df['Placement_%'] = (metrics_df['M_E_Verified_Placed'] / metrics_df['Total_Data']) * 100

                # Format percentages
                metrics_df['Enrollment_%'] = metrics_df['Enrollment_%'].apply(lambda x: f"{x:.2f}%")
                metrics_df['Placement_%'] = metrics_df['Placement_%'].apply(lambda x: f"{x:.2f}%")

                st.write("**Funder-wise Metrics Table**")
                st.dataframe(metrics_df, use_container_width=True)

        # Close the database connection
        if conn:
            conn.close()
    else:
        st.error("Cannot create database connection.")

if __name__ == '__main__':
    main()
