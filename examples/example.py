import streamlit as st
from streamlit_notion import NotionConnection

# Create connection
conn = st.connection("notion", type=NotionConnection, notion_api_key="secret_XjBxV6Vm9gWvFoGwmZzxXefqx2g7gSeaVJiPK9l5Kq1")

databases = conn.list_databases()

# st.write(databases)

for database in databases["results"]:
    r = conn.query(database["id"], page_size=1)
    st.write(r)