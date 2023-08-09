import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(np.random.randn(1000).cumsum())
ticks = ax.set_xticks([0, 250, 500, 750, 1000])
labels = ax.set_xticklabels(['하나','둘','셋','넷','다섯'],
                            rotation = 30)


def desc():
    global fig
    st.pyplot(fig)