import streamlit as st
import pandas as pd
import json
import os



def app():
    st.header("Database: Saved data ")

    # Get the absolute path to the 'data.json' file
    script_directory = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(script_directory, 'data.json')

    # Check if the file exists
    if not os.path.exists(data_file_path):
        st.warning(f"File '{data_file_path}' not found.")
        return

    # Reading data from JSON file
    try:
        with open(data_file_path, 'r') as json_file:
            data = json.load(json_file)
    except Exception as e:
        st.error(f"Error reading data from '{data_file_path}': {str(e)}")
        return

    df = pd.DataFrame(data)
    df['Email ID'] = df['Email ID'].astype(str)

    st.subheader("1. Press to view the existing data:card_index_dividers:")
    if not data:
        st.warning("No rows available for deletion")
    elif st.button("Press"):
        st.write(df)

    st.subheader("2. Press to delete specific business card data by row number:")
    if not data:
        st.warning("No rows available for deletion")
    else:
        row_number = st.number_input("Enter the row number to delete:", min_value=0, max_value=len(data))

        if st.button("Delete"):
            if 0 <= row_number <= len(data):
                # Remove the specified row from the loaded JSON data  
                del data[row_number]
                # Save updated data back to JSON file
                try:
                    with open(data_file_path, 'w') as json_file:
                        json.dump(data, json_file, indent=4)
                    st.success(f"Row {row_number} deleted successfully")
                except Exception as e:
                    st.error(f"Error saving data to '{data_file_path}': {str(e)}")
            else:
                st.warning("Invalid row number")

# Call the app function if running as a script
if __name__ == "main":
    app()