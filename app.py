import streamlit as st 
import requests
from streamlit_lottie import st_lottie 
import json
from PIL import Image
import pandas as pd
import yaml
from getKey import  get_secret
from getObjects import getDatabaseCredentials
from databaseClient import create_database_connections
from queryEngineClient import query_engine_factory
from authenticateKnowledgeGraph import authenticateKnowledgeGraph
from page2 import page2


st.set_page_config(page_title="My webpage", page_icon=":shark:", layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def load_lottifile(file_path: str):
    with open(file_path) as f:
        return json.load(f)

def page1():
    local_css("style.css")
    
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)


    st.markdown('<div class="title">Galava</div>', unsafe_allow_html=True)
    
    lottie_file1 = load_lottifile("Animation - 1712153841213.json")

    with st.container():
        st.write("-----")
    
        left_column, right_column = st.columns(2)
        with left_column:
            unique_key = f"coding-{id(object)}"
            st_lottie(lottie_file1, speed=1, width=550, height=500, key=unique_key)
            
        
        with right_column:
            st.markdown("""
                <link href='https://fonts.googleapis.com/css?family=Aclonica' rel='stylesheet'>
                <h1 class="vault-header">Enter Vault Credentials</h1>
                """, unsafe_allow_html=True)
            st.write("##")

            with st.form(key='form1'):
                SecretName = st.text_input("Secret Name", key='name')
                access_id = st.text_input("Access Id", key='access_id')
                secret_access_id = st.text_input("Secret Access Id", key='secret_access_id')
                submit_button = st.form_submit_button(label='CONNECT TO VAULT')

            if submit_button:
                secretval= get_secret(SecretName, access_id, secret_access_id)
                print(secretval)
                dbCredentials = getDatabaseCredentials(secretval, access_id, secret_access_id)
                print(dbCredentials)
                yaml_data = yaml.safe_load(dbCredentials)
                graph = authenticateKnowledgeGraph()

                with open('data.yaml', 'w') as file:
                    yaml.dump(yaml_data, file, default_flow_style=False)

                database_connections = create_database_connections('data.yaml')

                query_engines = [query_engine_factory(conn) for conn in database_connections]

                for engine in query_engines:
                    try:
                        table_names = engine.get_table_names()
                        print(table_names)
                        #get database name from yaml file
                        db_name = yaml_data['SQLDatabases'][0]['name']
                        # graph.create_database_node(db_name)
                        # for table in table_names:
                        #     graph.create_table_node(db_name, table)
                        
                    except Exception as e:
                        print("Error retrieving table names:", e)

                st.session_state['database_connections'] = database_connections


               
                # st.session_state['page'] = 'page2'
                page2()


        st.write("-----")

if __name__ == "__main__":
    page1()



    


    
