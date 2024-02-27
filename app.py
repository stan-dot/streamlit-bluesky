import streamlit as st
from bluesky.utils import ProgressBarManager
from databroker import Broker
from ophyd.sim import det1, det2

from bluesky.plans import count
import pandas as pd
from bluesky.callbacks.best_effort import BestEffortCallback

from bluesky import RunEngine

st.title("Hello World")


df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})

df


RE = RunEngine({})
bec = BestEffortCallback()
RE.subscribe(bec)


db = Broker.named("temp")
RE.subscribe(db.insert)

RE.waiting_hook = ProgressBarManager()

dets = [det1, det2]

res = RE(count(dets))

ProgressBarManager

st.divider()

res

