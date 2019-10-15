# car =  "moving" or "stopped"
#light = "red", "yellow", "green"
# return = "go" or "stop"
from operations import traffic_light_choice

def test_light_choice_moving_red():
    assert traffic_light_choice("moving", "red") == "stop"

def test_light_choice_moving_yellow():
    assert traffic_light_choice("moving", "yellow") == "stop"

def test_light_choice_moving_green():
    assert traffic_light_choice("moving", "green") == "go"

def test_light_choice_stopped_red():
    assert traffic_light_choice("stopped", "red") == "stop"

def test_light_choice_stopped_yellow():
    assert traffic_light_choice("stopped", "yellow") == "stop"

def test_light_choice_stopped_green():
    assert traffic_light_choice("stopped", "green") == "go"