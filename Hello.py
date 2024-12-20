# import streamlit as st
# from streamlit.logger import get_logger
# import pandas as pd
# import psycopg2
# from datetime import datetime


# LOGGER = get_logger(__name__)



# # Function to connect to AWS RDS database
# def create_connection():
#     conn = psycopg2.connect(
#         database="concentration",
#         user="alpro",
#         password="l33hJC7Ys2n4zr6u63zo",
#         host="dataacquisition.cc4idrhev5xz.eu-north-1.rds.amazonaws.com",
#         port="5432")
#     return conn

# # Create table if not exists
# def create_table(conn):
#     cursor = conn.cursor()
#     cursor.execute('''CREATE TABLE IF NOT EXISTS research_data
#                     (id SERIAL PRIMARY KEY,
#                      datetime TIMESTAMP,
#                      dry_weight FLOAT);''')
#     conn.commit()

# # Function to insert data into database
# def insert_data(conn, datetime, dry_weight):
#     cursor = conn.cursor()
#     cursor.execute('''INSERT INTO research_data (datetime, dry_weight)
#                       VALUES (%s, %s);''', (datetime, dry_weight))
#     conn.commit()
#     st.success("Data inserted successfully!")

# # Main function
# def main():
#     # Set page layout
#     st.set_page_config(page_title="Research Data Entry", page_icon=":bar_chart:")

#     # Upload and display company logo at the header
#     st.image("public-logo.png", width=150)
#     # README section with centralized title
#     st.markdown("""
#     <div style="text-align: center;">
#         <h1 style="margin-bottom: 0; color: green;">AlProtein Data Entry 👨🏻‍💻</h1>
#         <hr style="margin-top: 0;">
#     """, unsafe_allow_html=True)


#     # README section
#     st.markdown("""
#     🚀 Welcome to the Research Data Entry App! 🚀

#     This app is your go-to tool for empowering both the R&D and AI teams. Here's how:

#     🔍 **For R&D Team:**
#     Easily enter and manage research data in a structured format. The app securely stores this valuable information in an AWS RDS database, ensuring data integrity and accessibility. Remember to use the datetime format (YYYY/MM/DD HH:mm:ss:) when inputting data.

#     🤖 **For AI Team:**
#     Harness the power of labeled sensor data! With this app, you can effortlessly label sensor data with precise timestamps and dry weight values. These labeled data points are the building blocks for enhancing the AIPredict model, enabling accurate predictions of dry weight based on sensor data.

#     🚀 Ready to get started? Simply enter the required data below and hit the "Submit" button to supercharge your research and AI initiatives!
#     """)



#     # Get current year and month
#     current_year = datetime.now().year
#     current_month = datetime.now().month

#     # Default datetime to current year and month
#     default_datetime = f"{current_year}-{current_month:02}-01 00:00:00"

#     # Input fields for datetime and dry weight
#     st.markdown("### Enter Research Data 👇")
#     datetime_input = st.text_input("Enter Datetime ⏰⏰:", default_datetime)
#     dry_weight_input = st.number_input("Enter Dry Weight ⚖️⚖️:", min_value=0.0)

#     # Button to submit data
#     if st.button("Submit"):
#         try:
#             # Add default seconds if not specified
#             if len(datetime_input) == 16:
#                 datetime_input += ":00"

#             # Validate datetime format
#             pd.to_datetime(datetime_input, format='%Y-%m-%d %H:%M:%S')
#         except ValueError:
#             st.error("Please enter datetime in the format YYYY-MM-DD HH:MM")
#             return

#         # Insert data into database
#         conn = create_connection()
#         create_table(conn)
#         insert_data(conn, datetime_input, dry_weight_input)
#         conn.close()

# # Run the app
# if __name__ == "__main__":
#     main()




import streamlit as st
from streamlit.logger import get_logger
import pandas as pd
import psycopg2
from datetime import datetime

LOGGER = get_logger(__name__)

# Function to connect to AWS RDS database
def create_connection():
    conn = psycopg2.connect(
        database="research",
        user="alpro",
        password="PVtgs8mtGsThUEl2NjR0",
        host="research.c2bcka4zvdxd.us-east-1.rds.amazonaws.com",
        port="5432"
    )
    return conn

# Create table if not exists
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS research_data
                    (id SERIAL PRIMARY KEY,
                     datetime TIMESTAMP,
                     dry_weight FLOAT,
                     ph FLOAT);''')
    cursor.execute('''ALTER TABLE research_data
                    ADD COLUMN IF NOT EXISTS ph FLOAT;''')
    conn.commit()

# Function to insert data into database
def insert_data(conn, datetime, dry_weight, ph):
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO research_data (datetime, dry_weight, ph)
                      VALUES (%s, %s, %s);''', (datetime, dry_weight, ph))
    conn.commit()
    st.success("Data inserted successfully!")

# Function to fetch data from the database
def fetch_data(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM research_data;')
    data = cursor.fetchall()
    return data

# Main function
def main():
    # Set page layout
    st.set_page_config(page_title="Research Data Entry", page_icon=":bar_chart:")

    # Upload and display company logo at the header
    st.image("public-logo.png", width=150)
    # README section with centralized title
    st.markdown("""
    <div style="text-align: center;">
        <h1 style="margin-bottom: 0; color: green;">AlProtein Data Entry 👨🏻‍💻</h1>
        <hr style="margin-top: 0;">
    </div>
    """, unsafe_allow_html=True)

    # README section
    st.markdown("""
    🚀 Welcome to the Research Data Entry App! 🚀

    This app is your go-to tool for empowering both the R&D and AI teams. Here's how:

    🔍 **For R&D Team:**
    Easily enter and manage research data in a structured format. The app securely stores this valuable information in an AWS RDS database, ensuring data integrity and accessibility. Remember to use the datetime format (YYYY-MM-DD HH:mm:ss) when inputting data.

    🤖 **For AI Team:**
    Harness the power of labeled sensor data! With this app, you can effortlessly label sensor data with precise timestamps, dry weight, and pH values. These labeled data points are the building blocks for enhancing the AIPredict model, enabling accurate predictions.

    🚀 Ready to get started? Simply enter the required data below and hit the "Submit" button to supercharge your research and AI initiatives!
    """)

    # Get current year and month
    current_year = datetime.now().year
    current_month = datetime.now().month

    # Default datetime to current year and month
    default_datetime = f"{current_year}-{current_month:02}-01 00:00:00"

    # Input fields for datetime, dry weight, and pH
    st.markdown("### Enter Research Data 👇")
    datetime_input = st.text_input("Enter Datetime ⏰⏰:", default_datetime)
    dry_weight_input = st.number_input("Enter Dry Weight ⚖️⚖️:", min_value=0.0)
    ph_input = st.number_input("Enter pH 🧪🧪:", min_value=0.0, max_value=14.0, step=0.01)

    # Button to submit data
    if st.button("Submit"):
        try:
            # Add default seconds if not specified
            if len(datetime_input) == 16:
                datetime_input += ":00"

            # Validate datetime format
            pd.to_datetime(datetime_input, format='%Y-%m-%d %H:%M:%S')
        except ValueError:
            st.error("Please enter datetime in the format YYYY-MM-DD HH:MM")
            return

        # Validate pH range
        if not (0 <= ph_input <= 14):
            st.error("Please enter a valid pH value between 0 and 14.")
            return

        # Insert data into database
        conn = create_connection()
        create_table(conn)
        insert_data(conn, datetime_input, dry_weight_input, ph_input)
        conn.close()

    # Button to view data
    if st.button("View Data"):
        conn = create_connection()
        data = fetch_data(conn)
        conn.close()

        # Create a DataFrame for display
        df = pd.DataFrame(data, columns=['ID', 'Datetime', 'Dry Weight', 'pH'])
        st.dataframe(df)

# Run the app
if __name__ == "__main__":
    main()
