""" Example of using the Notion API with Streamlit """
import streamlit as st
from streamlit_notion import NotionConnection

# Create connection
conn = st.connection("notion", type=NotionConnection)

databases = conn.list_databases()

# st.write(databases)

for database in databases["results"]:
    r = conn.query(database["id"], page_size=1)
    st.write(r)
