
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

st.header("Headers")

"(bold management is weird : less bold, then bolder, then less bold. Uhu?)"

"""
# Level 1
Da level 1
"""


"""
## Level 2
dksldks
"""

"""
### Level 3
kjdksjdks
"""

"""#### Level 4
jdksjdks
"""

"""##### Level 5
jdskjd
"""

"""###### Level 6
kslkdsl
"""

st.header("Numbers")

1

1.0

1.0j


st.markdown("**Vector** is Displayed as a *column* matrix urk.")

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
Note that keys that can be converted to numbers are reorders but not the
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

st.header("Custom Objects")

"""
OK, AFAICT, `repr` is used by default. 
"""

class C:
    pass

C

c = C()

c

f"""
**Note for myself.** The sweet spot to output some content with inline data
intertwined could be triple quoted f-strings: `{c}` is an instance of `{C}`.
Of course then we don't get acces to any special formatting that the objects
may have The alternative being tuples with strings and variables (?)
"""

"""
Instance:""", c, """.
"""

"This is a bit fugly (in the source code)."

st.header("Mathematics")

"""
Mathematics are supported ; the generation is done KaTeX. So I can inline some stuff like 
$a=1$ or write display math such as
$$
\int_0^1 f(x) \, dx.
$$
"""

r"""
Can I use non dollar environment such as `align`? (supported by KaTeX). Of course not

\begin{align}
   a&=b+c \\
   d+e&=f
\end{align} 

And if I embed them in double dollars (\$\$)?

$$
\begin{align}
   a&=b+c \\
   d+e&=f
\end{align} 
$$

Nope, I get a KaTeX error (which is legit).

"""

"Unless I can leverage the `st.latex` function ?"

st.latex(r"""
\begin{align}
   a&=b+c \\
   d+e&=f
\end{align}""")

"""
Nope. (It's probably auto-quoting).
"""


st.header("HTML")

st.markdown("By default, HTML is escaped : <b>Am I bold?</b>")

st.markdown("We can change that with the appropriate option: <b>Am I bold?</b>", unsafe_allow_html=True)

st.markdown("scripts? Nope: <script>alert('Help !');</script>", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
st.header("Code")

"Fenced code block:"

"""
``` python
if True:
    a = True
else:
    pass
```
"""

# ------------------------------------------------------------------------------
st.header("Media (**TODO**)")

# ------------------------------------------------------------------------------
st.header("Data (**TODO**)")

# ------------------------------------------------------------------------------
st.header("Graphs (**TODO**)")

"Matplotlib:"

import matplotlib.pyplot as plt
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

# ------------------------------------------------------------------------------
st.title("Widgets (**TODO**)")

if st.button("Click"):
    st.write("stuff")
else:
    st.write("Nope")

status = st.checkbox("Checked?")

if status:
    st.write("Yep")
else:
    st.write("Nope")

genre = st.radio(
     "What's your favorite movie genre",
     ('Comedy', 'Drama', 'Documentary'))

f"{genre}"


option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))

option

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

options

from datetime import datetime
start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)

title = st.text_input('Movie title', 'Life of Brian')
title

number = st.number_input('Insert a number')
number

txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
    ''')

txt


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
