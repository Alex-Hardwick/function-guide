import streamlit as st

st.set_page_config(
    page_title="New Functions",
    page_icon=":bricks:",
)

st.title("Building A New Function")
st.subheader("A terrible guide by Alex 'Momo' Hardwick")
st.write("Our problem is fairly simple: What are the filenames of the most recent capture sheets?")
st.write("We're simplifying a bit here but once we've solved this it links into a much larger problem (what's actually in the sheets?)")
st.write("We'll start with our imports, we know we'll need to mess about with operating level stuff so we'll definitely need 'os', 'time' will help us with working out which files we actually want to process and 'glob' has a very silly name but it's a really useful way of iterating through the items in a folder")
st.code('''import os, time, glob''')
st.write("First we can tell our code where to start looking and we store it in the variable 'srch_dir' so we can use it later")
st.code('''srch_dir = "C:/Users/Momo/Desktop/Work Stuff/Ash Parse/Ash Cap/"''')
st.write("Time for glob. We give it the start of the search with our variable and add on a bunch of stars and slashes so it'll look for everything")
st.write("The 'recursive=True' bit means we're going to do this for every folder we find")
st.code('''glob.glob(srch_dir + "/**/*", recursive=True)''')
st.write("Which gets us... something:")
with st.expander("Output"):
    st.code('''
    ['C:/Users/Momo/Desktop/Work Stuff/Ash Parse/Ash Cap\\Feb', 
    'C:/Users/Momo/Desktop/Work Stuff/Ash Parse/Ash Cap\\Mar', 
    'C:/Users/Momo/Desktop/Work Stuff/Ash Parse/Ash Cap\\Feb\\Ash CH4006 21-02-2024 1.xlsm', 
    'C:/Users/Momo/Desktop/Work Stuff/Ash Parse/Ash Cap\\Feb\\Ash CH4006 22-02-2024 1.xlsm', 
    'C:/Users/Momo/Desktop/Work Stuff/Ash Parse/Ash Cap\\Feb\\Ash CH4006 26-02-2024 1.xlsm', 
    'C:/Users/Momo/Desktop/Work Stuff/Ash Parse/Ash Cap\\Feb\\Ash CH4006 27-02-2024 1.xlsm', 
    'C:/Users/Momo/Desktop/Work Stuff/Ash Parse/Ash Cap\\Mar\\Ash CH4006 12-03-2024 1.xlsm', 
    'C:/Users/Momo/Desktop/Work Stuff/Ash Parse/Ash Cap\\Mar\\Ash CH4006 12-03-2024 1b.xlsm', 
    'C:/Users/Momo/Desktop/Work Stuff/Ash Parse/Ash Cap\\Mar\\Ash CH4006 23-02-2024 1.xlsm']
    ''')
st.write("OK, but there's folders in that list and if we try to open a folder like a file we might have A Bad Time so we need to filter out just the files")
st.write("To do that we'll wrap up our glob function into a filter() command. We'll also pass in 'os.path.isfile' which is what we'll use to decide if it belongs in our filtered list and can either be True or False")
st.write("After the ',' we just paste in the thing that made us a list from earlier. To make it easy on ourselves we might as well store the list we'll get back in a new variable")
st.code('''
list_of_files = filter( os.path.isfile,
               glob.glob(srch_dir + "/**/*", recursive=True))
''')
with st.expander("print(list_of_files):"):
    st.code('''
    ['C:/Users/Momo/Desktop/Work Stuff/Ash Parse/Ash Cap\\Mar\\Ash CH4006 23-02-2024 1.xlsm',
    'C:/Users/Momo/Desktop/Work Stuff/Ash Parse/Ash Cap\\Mar\\Ash CH4006 12-03-2024 1.xlsm',
    'C:/Users/Momo/Desktop/Work Stuff/Ash Parse/Ash Cap\\Feb\\Ash CH4006 22-02-2024 1.xlsm',
    'C:/Users/Momo/Desktop/Work Stuff/Ash Parse/Ash Cap\\Feb\\Ash CH4006 27-02-2024 1.xlsm',
    'C:/Users/Momo/Desktop/Work Stuff/Ash Parse/Ash Cap\\Feb\\Ash CH4006 26-02-2024 1.xlsm',
    'C:/Users/Momo/Desktop/Work Stuff/Ash Parse/Ash Cap\\Mar\\Ash CH4006 12-03-2024 1b.xlsm',
    'C:/Users/Momo/Desktop/Work Stuff/Ash Parse/Ash Cap\\Feb\\Ash CH4006 21-02-2024 1.xlsm']
    ''')
st.write("Much better, but we have no idea how old any of this stuff is and we can't trust the order it's in now. We could rely on the names of the files and folders or we can just ask the operating system")
st.write("This time we'll use the sorted() function. First we give it our list of files")
st.write("Next the sorting key which is another operating system function that just returns the time stamp for when the file was last modified")
st.write("To make it a bit easier for us to read we'll flip the order so the newest one is at the top. Might as well store it all in the same variable too")
st.code('''
list_of_files = sorted( list_of_files,
                        key = os.path.getmtime,
                        reverse=True)''')
with st.expander("print(list_of_files):"):
    st.code('''
    ['C:/Users/Momo/Desktop/Work Stuff/Ash Parse/Ash Cap\\Mar\\Ash CH4006 23-02-2024 1.xlsm', 
    'C:/Users/Momo/Desktop/Work Stuff/Ash Parse/Ash Cap\\Mar\\Ash CH4006 12-03-2024 1b.xlsm', 
    'C:/Users/Momo/Desktop/Work Stuff/Ash Parse/Ash Cap\\Mar\\Ash CH4006 12-03-2024 1.xlsm', 
    'C:/Users/Momo/Desktop/Work Stuff/Ash Parse/Ash Cap\\Feb\\Ash CH4006 27-02-2024 1.xlsm', 
    'C:/Users/Momo/Desktop/Work Stuff/Ash Parse/Ash Cap\\Feb\\Ash CH4006 26-02-2024 1.xlsm', 
    'C:/Users/Momo/Desktop/Work Stuff/Ash Parse/Ash Cap\\Feb\\Ash CH4006 22-02-2024 1.xlsm', 
    'C:/Users/Momo/Desktop/Work Stuff/Ash Parse/Ash Cap\\Feb\\Ash CH4006 21-02-2024 1.xlsm']
    ''')
st.write("Perfect... I don't have all that many files to work with on my PC but we can still apply some logic about how many we want. We'll 'slice' the list using some [square brackets]")
st.write("Let's try getting the top 4 entries and printing out the timestamp for them. Time stuff looks really complicated but we won't actually need it when we use it later")
st.code('''
for file_path in list_of_files[:4]:
    timestamp_str = time.strftime(  '%d/%m/%Y @ %H:%M:%S',
                                time.gmtime(os.path.getmtime(file_path))) 
    print(timestamp_str, ' -->', file_path)    
''')
with st.expander("print(timestamp_str, ' -->', file_path):"):
    st.code('''
10/04/2024 @ 19:25:24  --> C:/Users/Momo/Desktop/Work Stuff/Ash Parse/Ash Cap\Mar\Ash CH4006 23-02-2024 1.xlsm
12/03/2024 @ 19:29:30  --> C:/Users/Momo/Desktop/Work Stuff/Ash Parse/Ash Cap\Mar\Ash CH4006 12-03-2024 1b.xlsm
12/03/2024 @ 18:08:30  --> C:/Users/Momo/Desktop/Work Stuff/Ash Parse/Ash Cap\Mar\Ash CH4006 12-03-2024 1.xlsm
28/02/2024 @ 22:15:26  --> C:/Users/Momo/Desktop/Work Stuff/Ash Parse/Ash Cap\Feb\Ash CH4006 27-02-2024 1.xlsm
    ''')
st.write("It would be nice if I could use this code all over the place so I'm going to turn it into a funtion (which is just a fancy way of not having to copy/paste all the time)")
st.write("The whole thing ends up looking a bit like this:")
with st.expander("get_ash_files.py"):
    st.code('''
    import os, time, glob
            
    def get_ash_files():
        srch_dir = "C:/Users/Momo/Desktop/Work Stuff/Ash Parse/Ash Cap"

        list_of_files = filter( os.path.isfile,
                    glob.glob(srch_dir + "/**/*", recursive=True))

        list_of_files = sorted( list_of_files,
                                key = os.path.getmtime,
                                reverse=True)
        list_of_files = list_of_files[:4]
        
        return list_of_files
''')
st.write("From here I can use that list_of_files when I'm reading spreadsheets so I know I'm always using the most recent files regardless of the folder structure. Easy 😊")
st.write("Note: If we're going to do this properly (which I will) we'll want to make it so we can choose the 'srch_dir' and how many results should be in the list that comes back. Maybe that can be part 2")
    
