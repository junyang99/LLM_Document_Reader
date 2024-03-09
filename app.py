import streamlit as st 

def main():
    st.set_page_config(page_title = "Chat with your PDFs", page_icon = ":books:")
    
    st.header("Skip the reading, chat with your pdf instead :books:")
    st.text_input("Ask a question about your documents:")
    
    with st.sidebar:
        st.subheader("Your documents")
        st.file_uploader('Upload PDFs here and click on "Process" ')
        st.button("Process")
    
if __name__ == '__main__':
    main()