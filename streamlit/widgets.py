import streamlit as st
import time

st.audio("song.mp3",width="stretch",autoplay=False,loop=True)

aud = st.audio_input("voice",sample_rate=44100,width="stretch")
st.audio(aud)
# song=st.audio("song.mp3")

st.badge("badge",icon="😜",color="yellow")
# st.balloons()
# st.snow()

# picture = st.camera_input("Take a picture",width=500)

# if picture:
#     st.image(picture)

st.caption("this is a caption")
st.caption("A caption with _italics_ :blue[colors] and emojis :sunglasses:")
with st.expander("code",icon="👨🏻‍💻"):
    st.code('''import streamlit as st

    st.audio("song.mp3",width="stretch",autoplay=False,loop=True)

    aud = st.audio_input("voice",sample_rate=44100,width="stretch")
    st.audio(aud)

    st.badge("badge",icon="😜",color="yellow")
    st.balloons()
    st.snow()''',language="python",line_numbers=True)

    st.code('''System.out.println("hello from java")''',language="java")

    # st.download_button("download song",data="song.mp3",file_name="song.mp3",mime="audio/mpeg",icon="⬇️")

st.link_button("google",url="https://www.google.com/")

#st.pdf("https://www.halvorsen.blog/documents/programming/python/resources/Python%20Programming.pdf")

# pdf = "https://www.halvorsen.blog/documents/programming/python/resources/Python%20Programming.pdf" 
# st.markdown( f'<iframe src="{pdf}" crossorigin="anonymous" width="700" height="1000"></iframe>' , unsafe_allow_html=True)

res = st.pills("pills",["one","two","three"],selection_mode="multi")
st.write(res)

bar =st.progress(0,text="progress bar")

# for i in range(100):
#     time.sleep(0.5)
#     bar.progress(i+1,text="progress bar")


slider = st.slider("slider",0,10,format="plain")
st.write(slider)


with st.spinner("Wait", show_time=True):
    time.sleep(5)

st.status("status",state="complete")