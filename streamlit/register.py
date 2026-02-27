import streamlit as st
from datetime import date
st.title("Registration Form", text_alignment="center")

# st.write("username",st.text_input("a",label_visibility="hidden",width=20))
# st.text(st.text_input("one",args="1"),text_alignment="right")
# uname = st.text_input("username")
# password = st.text_input("Password",type="password")
# rpassword = st.text_input("Retype Password",type="password")
# gender = st.radio("Gender",["Male","Female"])

# col1,col2 = st.columns(2,vertical_alignment="top")

# with st.container(horizontal=True, horizontal_alignment="distribute"):
#     st.markdown("# Username")
#     uname = st.text_input("",key="u")

# with st.container(horizontal=True, horizontal_alignment="distribute"):
#     st.markdown("# Password")
#     password = st.text_input("",type="password",key="p")

# with st.container(horizontal=True, horizontal_alignment="distribute"):
#     st.markdown("# Retype-Password")
#     rpassword = st.text_input("",type="password",key="rp")

# with st.container(horizontal=True, horizontal_alignment="distribute"):
#     st.markdown("# Gender")
#     gender = st.radio("",["Male","Female"])

    
# with st.container(horizontal=True, horizontal_alignment="distribute"):
#     st.markdown("# Correspondence")
#     st.text_area("")           

# with col1:
#     st.markdown("# Username")
#     st.markdown("# Password")
#     st.markdown("# RetypePassword")
#     st.markdown("# Gender")
#     st.markdown("# Correspondence")
#     st.markdown("# MobileNo")
#     st.markdown("# Pincode")
#     st.markdown("# Interests")
#     st.markdown("# Date of Birth")


# with col2:
#     uname = st.text_input("username",label_visibility="hidden")
#     password = st.text_input("Password",type="password",label_visibility="hidden")
#     rpassword = st.text_input("Retype Password",type="password",label_visibility="hidden")
#     gender = st.radio("",["Male","Female"])
#     correspondence = st.text_area("")
#     mob = st.text_input("",key="two")
#     pincode = st.text_input("",key="three")
#     interests = st.text_input("",key="four")
#     dob = st.date_input("",label_visibility="hidden",key="five")


col1, col2 = st.columns([2, 2])
with col1:
        st.markdown("## Username")
with col2:
        username = st.text_input("", key="username")

    
col1, col2 = st.columns([2, 2])
with col1:
        st.markdown("## Password")
with col2:
        password = st.text_input("", type="password", key="password")

    
col1, col2 = st.columns([2, 2])
with col1:
        st.markdown("## Retype Password")
with col2:
        re_password = st.text_input("", type="password", key="repassword")

    
col1, col2 = st.columns([2, 2])
with col1:
        st.markdown("## Gender")
with col2:
        gender = st.radio("", ["Male", "Female"], horizontal=True)

    
col1, col2 = st.columns([2, 2])
with col1:
        st.markdown("## Correspondence")
with col2:
        address = st.text_area("", height=120)

    
col1, col2 = st.columns([2, 2])
with col1:
        st.markdown("## Mobile No")
with col2:
        mobile = st.text_input("", key="mobile")

    
col1, col2 = st.columns([2, 2])
with col1:
        st.markdown("## Pincode")
with col2:
        pincode = st.text_input("", key="pincode")

    
col1, col2 = st.columns([2, 2])
with col1:
        st.markdown("## Interests")
with col2:
        interests = st.text_input("", key="interests")

    
col1, col2 = st.columns([2, 2])
with col1:
        st.markdown("## Date of Birth")
with col2:
        dob = st.date_input("", min_value=date(1950, 1, 1))


col1, col2, col3 = st.columns([1,3,1])
with col2:
    if(st.button("Submit",icon="🌼",width=250)):
            if(password==re_password):
                st.markdown("## :blue[Passwords Match]",width=500)
                #st.success("passwords match")
            else:
                st.markdown("## :red[Passwords Do Not Match]",width=500)
                #st.error("passwords do not match")