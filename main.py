
import streamlit as st
import pandas as pd
import numpy as np


# ------------------------------------------------------------------------------

st.title("Magic")

s = "This is **magic**"
s

"I can tell"

"Let's try some other Python objects"



### Mmm how do I display a string OBJECT with the quotes then?

t = repr(s)
t

repr(s) # doesn't show
repr(s) + "" # does show. Lol. Magic is quite britle ...

b"BYTE\x00Z"

st.header("Numbers")

1

1.0

1.0j


st.markdown("**Vector** is Displayed as a *column* matrix ... urk.")

x = np.zeros(6)
x

"**Row vector.** Displayed as a row vector (matrix). Here makes sense."

st.write(np.zeros((1, 6)))

"**Matrix**"

A = np.ones((2,3))
A

"**Tensor**"

T = np.ones((2, 3 , 4))
T

st.header("Containers")

st.subheader("Lists")

[1, 2, 3]

[1, 2, [3, 4, [5]]]

st.subheader("Dictionary")

'Let\'s see what `{"a": 5, "b": 8, 9: "caramba!", "dict": {0: 2, 1: 3}, "list": [2,3]}` looks like.'

{"a": 5, "b": 8, 9: "caramba!", "dict": {0: 2, 1: 3}, "list": [2,3]}

"""
Dafuq. Streamlits quotes my integer keys! And reorder my key-value pairs!!!
**BAD!**
"""

"Ah! Here tuple value converted as list: `{'struct': (1,1,1)}`"

{"struct": (1,1,1)}

"""
But `{(0,1): 42}` won't work, because it want to display something that it can
convert to JSON. Oh my! 
"""

{(0,1): 42}

'''
The number-to-string conversion can be fucked up quite easily, see e.g.
`{99: 99, "z": 1, "a": 2, 0: 0, "0": "'0'", "1": True}`
'''

{99: 99, "z": 1, "a": 2, 0: 0, "0": "'0'", "1": True}

"""
Note that keys that can be converted to numbers are reorders ... but not the
string keys (???)
"""

st.subheader("Tuples")

"Literal tuple"

(6, 6, "skid", "🐤") # Note the same !!!

"Tuple assigned to variable, then display variable:", (6, 6, "skid", "🐤")

st.write("Explicit `st.write`:", (6, 6, "skid", "🐤"))

# Lol. Why is this different ?

"""Ah, I see; since streamlit wants to be able to do magic on multiple element,
it *interprets* literal tuples, not as an object, but as an instruction to 
magically `st.write` multiple things."""

# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
sh = st.empty()
m = st.empty()
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
sh.subheader('Map of all pickups at %s:00' % hour_to_filter)
m.map(filtered_data)
