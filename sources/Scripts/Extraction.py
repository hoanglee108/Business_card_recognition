import streamlit as st
import easyocr
import json
import matplotlib.pyplot as plt
import os

plt.rcParams['figure.figsize'] = 8, 16
reader = easyocr.Reader(['en'], gpu=False)

def extract_data(image):
    data = reader.readtext(image)
    name = ""
    des = ""
    phone_number = ""
    email = ""
    website = ""
    website1 = ""
    remaining = []
    for i in range(0, len(data)):
        if i == 0:
            name = data[i][1]
        elif i == 1:
            des = data[i][1]
        elif "-" in data[i][1] or "+" in data[i][1]:
            phone_number = data[i][1]
        elif "@" in data[i][1] and ".com" in data[i][1]:
            email = data[i][1]
        elif "www." in data[i][1] or ".com" in data[i][1]:
            website = data[i][1]
        elif "inc" in data[i][1].lower() or "co" in data[i][1].lower() or "&" in data[i][1]:
            company_name = data[i][1]
        else:
            remaining.append(data[i][1])
    address = ""
    company_name = ""
    for i in remaining:
        count = 0
        for j in i:
            if j in "1234567890" or j in ";:,.":
                count += 1
        if count > 0:
            address = address + i + " "
        elif i.lower() == "www":
            website = i.lower() + "." + website
        elif i.lower() == "city":
            address += " " + i
        elif i.lower() == "any":
            address = address.replace("City", "Any City")
        else:
            company_name = company_name + i + ' '

    website1 = website.replace(" ", ".")
    extracted_info = {
        "Employee Name": name,
        "Designation": des,
        "Company Name": company_name,
        "Contact Number": phone_number,
        "Email ID": email,
        "Website": website1,
        "Address": address
    }

    # Display extracted information in Streamlit
    st.subheader("Extracted information from the uploaded image.")
    st.write(f"Employee Name: {name}")
    st.write(f"Designation: {des}")
    st.write(f"Company Name: {company_name}")
    st.write(f"Contact Number: {phone_number}")
    st.write(f"Email ID: {email}")
    st.write(f"Website: {website1}")
    st.write(f"Address: {address}")

    st.subheader("Database uploadation!!")

    option = st.radio("Upload the extracted data on the database server:", (" ", "Yes", "No"))
    if option == "Yes":
        # Check if data.json exists and if the extracted_info is not already present
        if os.path.exists('data.json'):
            with open('data.json', 'r') as json_file:
                existing = json.load(json_file)
        else:
            existing = []

        exists = any(existing_info == extracted_info for existing_info in existing)
        if not exists:
            existing.append(extracted_info)
            with open('data.json', 'w') as json_file:
                json.dump(existing, json_file, indent=4)
            st.success("Uploaded Successfully!", icon='✅')
            st.balloons()
        else:
            st.warning("Data already exists in the database!")

    elif option == "No":
        with open('data.json', 'w') as json_file:
            json.dump([extracted_info], json_file, indent=4)
        st.write("Thank you!")