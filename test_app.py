from app import app


# test if the header exisits 
def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#header", timeout=10)

#test if the graph exists 
def test_graph_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#selected-figure", timeout=10)

# test if the radio to pick region exists
def test_radio_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-radio", timeout=10)