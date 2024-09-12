from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
import sqlite3
import pandas as pd

# Function to fetch data from the database
def fetch_data(conn):
    try:
        query = "SELECT * FROM students"
        df = pd.read_sql(query, conn)
        return df
    except sqlite3.Error as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()

# Function to create the database connection
def create_connection(database):
    try:
        conn = sqlite3.connect(database)
        return conn
    except sqlite3.Error as e:
        print(f"Error creating connection: {e}")
        return None

# Function to create the table if it doesn't exist
def create_table(conn):
    try:
        query = '''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            fy_year TEXT,
            funder_name TEXT,
            center TEXT,
            program_name TEXT,
            verification_done TEXT,
            m_e_verified_remarks TEXT,
            m_e_verified_students TEXT,
            trained_status TEXT,
            not_interested_in_job TEXT,
            working_before_batch_joining TEXT,
            non_anudip_student_others TEXT,
            placement_remarks TEXT,
            placement_status TEXT,
            download_from_cmis TEXT
        )
        '''
        conn.execute(query)
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

class DashboardApp(App):
    def build(self):
        # Main Layout
        main_layout = BoxLayout(orientation='vertical')
        self.dropdown_layout = BoxLayout(size_hint_y=None, height=50)
        self.metrics_layout = GridLayout(cols=2, size_hint_y=None, height=300)
        self.data_layout = ScrollView(size_hint=(1, None), size=(Window.width, 400))

        # Database file path
        database = "students.db"
        self.conn = create_connection(database)

        if self.conn:
            create_table(self.conn)
            self.df = fetch_data(self.conn)
            self.filtered_df = self.df

            # Dropdowns for filtering
            self.create_dropdowns()
            main_layout.add_widget(self.dropdown_layout)
            main_layout.add_widget(self.metrics_layout)
            main_layout.add_widget(self.data_layout)

            # Display metrics
            self.update_metrics()
        else:
            main_layout.add_widget(Label(text="Cannot create database connection."))

        return main_layout

    def create_dropdowns(self):
        # Fiscal Year Dropdown
        fy_dropdown = DropDown()
        years = self.df['fy_year'].dropna().unique()
        for year in sorted(years):
            btn = Button(text=year, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: fy_dropdown.select(btn.text))
            fy_dropdown.add_widget(btn)
        fy_button = Button(text='Select FY Year')
        fy_button.bind(on_release=fy_dropdown.open)
        fy_dropdown.bind(on_select=lambda instance, x: setattr(fy_button, 'text', x))
        fy_dropdown.bind(on_select=self.on_fy_year_selected)
        self.dropdown_layout.add_widget(fy_button)

        # Funder Name Dropdown
        funder_dropdown = DropDown()
        funders = self.df['funder_name'].dropna().unique()
        for funder in sorted(funders):
            btn = Button(text=funder, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: funder_dropdown.select(btn.text))
            funder_dropdown.add_widget(btn)
        funder_button = Button(text='Select Funder Name')
        funder_button.bind(on_release=funder_dropdown.open)
        funder_dropdown.bind(on_select=lambda instance, x: setattr(funder_button, 'text', x))
        funder_dropdown.bind(on_select=self.on_funder_name_selected)
        self.dropdown_layout.add_widget(funder_button)

        # Center Dropdown
        center_dropdown = DropDown()
        centers = self.df['center'].dropna().unique()
        for center in sorted(centers):
            btn = Button(text=center, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: center_dropdown.select(btn.text))
            center_dropdown.add_widget(btn)
        center_button = Button(text='Select Center')
        center_button.bind(on_release=center_dropdown.open)
        center_dropdown.bind(on_select=lambda instance, x: setattr(center_button, 'text', x))
        center_dropdown.bind(on_select=self.on_center_selected)
        self.dropdown_layout.add_widget(center_button)

        # Program Name Dropdown
        program_dropdown = DropDown()
        programs = self.df['program_name'].dropna().unique()
        for program in sorted(programs):
            btn = Button(text=program, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: program_dropdown.select(btn.text))
            program_dropdown.add_widget(btn)
        program_button = Button(text='Select Program Name')
        program_button.bind(on_release=program_dropdown.open)
        program_dropdown.bind(on_select=lambda instance, x: setattr(program_button, 'text', x))
        program_dropdown.bind(on_select=self.on_program_name_selected)
        self.dropdown_layout.add_widget(program_button)

    def on_fy_year_selected(self, instance, fy_year):
        self.filtered_df = self.df[self.df['fy_year'] == fy_year] if fy_year else self.df
        self.update_metrics()

    def on_funder_name_selected(self, instance, funder_name):
        self.filtered_df = self.filtered_df[self.filtered_df['funder_name'] == funder_name] if funder_name else self.df
        self.update_metrics()

    def on_center_selected(self, instance, center):
        self.filtered_df = self.filtered_df[self.filtered_df['center'] == center] if center else self.df
        self.update_metrics()

    def on_program_name_selected(self, instance, program_name):
        self.filtered_df = self.filtered_df[self.filtered_df['program_name'] == program_name] if program_name else self.df
        self.update_metrics()

    def update_metrics(self):
        self.metrics_layout.clear_widgets()
        # Metrics calculation similar to the Streamlit app
        total_data = self.filtered_df['download_from_cmis'].count()
        self.metrics_layout.add_widget(Label(text=f"Total Data: {total_data}"))

        total_verification_done = self.filtered_df['verification_done'].count()
        self.metrics_layout.add_widget(Label(text=f"Verification Done: {total_verification_done}"))

        contactable = self.filtered_df[self.filtered_df['verification_done'].str.strip().str.lower() == 'yes']
        contactable_count = contactable['verification_done'].count()
        self.metrics_layout.add_widget(Label(text=f"Contactable: {contactable_count}"))

        # Add more metrics as per your requirements

    def on_stop(self):
        # Close the database connection on app stop
        if self.conn:
            self.conn.close()

if __name__ == '__main__':
    DashboardApp().run()
