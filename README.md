# streamlit-bluesky

goal - to test how hard it would be to setup streamlit and bluesky to work together
<https://blueskyproject.io/bluesky/tutorial.html#before-you-begin>

<https://docs.streamlit.io/library/api-reference/charts/st.pyplot>

## errors

to avoid file watcher error add this flag
`$ python -m streamlit run app.py --server.fileWatcherType none`

this error happens when running with the RunEngine count plan
bluesky/run_engine.py", line 314, in setup_run_permit
    self._run_permit = asyncio.Event(loop=self._loop_for_kwargs)

looking for similar errors
https://github.com/bluesky/bluesky/issues?q=is%3Aissue+unexpected+keyword+argument

